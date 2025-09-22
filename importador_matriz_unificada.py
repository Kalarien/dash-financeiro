#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
IMPORTADOR DE MATRIZ FINANCEIRA UNIFICADA
Sistema que importa uma planilha única já formatada e organizada
"""

import pandas as pd
import numpy as np
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

class ImportadorMatrizUnificada:
    def __init__(self, arquivo="Matriz financeira.xlsx", aba="Matriz Detalhada"):
        """Inicializa o importador com arquivo padrão"""
        self.arquivo = arquivo
        self.aba = aba
        self.df_original = None
        self.dados_processados = {
            'receitas': None,
            'custos': None, 
            'impostos': None,
            'despesas': None,
            'resumo': None
        }
        
    def carregar_matriz(self):
        """Carrega a matriz financeira do arquivo"""
        try:
            print(f" Carregando matriz de: {self.arquivo}")
            self.df_original = pd.read_excel(self.arquivo, sheet_name=self.aba)
            
            print(f" Matriz carregada: {self.df_original.shape}")
            print(f" Periodo: {self.df_original.shape[1]-2} meses de projecao")
            
            return True
            
        except Exception as e:
            print(f"ERRO ao carregar matriz: {e}")
            return False
    
    def identificar_colunas_data(self):
        """Identifica automaticamente as colunas de data"""
        colunas_data = []
        for col in self.df_original.columns:
            if isinstance(col, datetime):
                colunas_data.append(col)
        
        print(f" Encontradas {len(colunas_data)} colunas de data")
        return sorted(colunas_data)
    
    def processar_receitas(self, colunas_data):
        """Processa dados de receitas de forma unificada"""
        receitas = []
        
        # Receitas Realizado
        linha_real = self.df_original[self.df_original['Categoria'] == 'Receitas Realizado']
        if not linha_real.empty:
            for col in colunas_data:
                valor = linha_real[col].iloc[0]
                if pd.notna(valor) and valor > 0:
                    receitas.append({
                        'Data': col,
                        'Tipo': 'Receita',
                        'Status': 'Realizado', 
                        'Valor': float(valor),
                        'Mes_Ano': col.strftime('%Y-%m')
                    })
        
        # Receitas Projetado
        linha_proj = self.df_original[self.df_original['Categoria'] == 'Receitas Projetado']
        if not linha_proj.empty:
            for col in colunas_data:
                valor = linha_proj[col].iloc[0]
                if pd.notna(valor) and valor > 0:
                    receitas.append({
                        'Data': col,
                        'Tipo': 'Receita',
                        'Status': 'Projetado',
                        'Valor': float(valor),
                        'Mes_Ano': col.strftime('%Y-%m')
                    })
        
        # B2B Projetado
        linha_b2b = self.df_original[self.df_original['Categoria'] == 'B2B Projetado']
        if not linha_b2b.empty:
            for col in colunas_data:
                valor = linha_b2b[col].iloc[0]
                if pd.notna(valor) and valor > 0:
                    receitas.append({
                        'Data': col,
                        'Tipo': 'Receita_B2B',
                        'Status': 'Projetado',
                        'Valor': float(valor),
                        'Mes_Ano': col.strftime('%Y-%m')
                    })
        
        return pd.DataFrame(receitas)
    
    def processar_custos(self, colunas_data):
        """Processa custos operacionais"""
        custos = []
        
        # Tarifa Adquirente
        linha_adq = self.df_original[self.df_original['Categoria'].str.contains('Tarifa Adquirente', na=False)]
        if not linha_adq.empty:
            for col in colunas_data:
                valor = linha_adq[col].iloc[0]
                if pd.notna(valor) and valor > 0:
                    custos.append({
                        'Data': col,
                        'Categoria': 'Tarifa_Adquirente',
                        'Valor': float(valor),
                        'Mes_Ano': col.strftime('%Y-%m')
                    })
        
        # Tarifa Antecipação
        linha_ant = self.df_original[self.df_original['Categoria'].str.contains('Tarifa Antecipa', na=False)]
        if not linha_ant.empty:
            for col in colunas_data:
                valor = linha_ant[col].iloc[0]
                if pd.notna(valor) and valor > 0:
                    custos.append({
                        'Data': col,
                        'Categoria': 'Tarifa_Antecipacao',
                        'Valor': float(valor),
                        'Mes_Ano': col.strftime('%Y-%m')
                    })
        
        return pd.DataFrame(custos)
    
    def processar_despesas(self, colunas_data):
        """Processa despesas operacionais"""
        despesas = []
        
        # Identifica linhas de despesas (exclui headers, totais e receitas/custos)
        linhas_despesas = self.df_original[
            (~self.df_original['Categoria'].isin([
                'RECEITAS', 'CUSTOS', 'DESPESAS', 'IMPOSTOS',
                'TOTAL RECEITAS', 'TOTAL CUSTOS', 'TOTAL DESPESAS', 'TOTAL IMPOSTOS',
                'RESULTADO LÍQUIDO'
            ])) &
            (~self.df_original['Categoria'].str.contains('Receitas|Tarifa|B2B', na=False)) &
            (~self.df_original['Categoria'].isna())
        ]
        
        for _, row in linhas_despesas.iterrows():
            categoria = str(row['Categoria']).strip()
            
            # Determina se é categoria principal ou subcategoria
            if categoria.startswith('  → '):
                categoria_tipo = 'Subcategoria'
                categoria_nome = categoria.replace('  → ', '').strip()
            else:
                categoria_tipo = 'Categoria'
                categoria_nome = categoria
            
            for col in colunas_data:
                valor = row[col]
                if pd.notna(valor) and valor > 0:
                    despesas.append({
                        'Data': col,
                        'Categoria': categoria_nome,
                        'Categoria_Tipo': categoria_tipo,
                        'Valor': float(valor),
                        'Mes_Ano': col.strftime('%Y-%m')
                    })
        
        return pd.DataFrame(despesas)
    
    def calcular_impostos_brasileiros(self, df_receitas, colunas_data):
        """Calcula impostos conforme legislação brasileira (Lucro Presumido)"""
        impostos = []
        
        for col in colunas_data:
            # Receitas do mês
            receitas_mes = df_receitas[df_receitas['Data'] == col]['Valor'].sum()
            
            if receitas_mes > 0:
                # 50% serviços, 50% livros (livros isentos de alguns impostos)
                receita_servicos = receitas_mes * 0.5
                receita_livros = receitas_mes * 0.5
                
                # ISS - apenas sobre serviços
                iss = receita_servicos * 0.05
                if iss > 0:
                    impostos.append({
                        'Data': col,
                        'Imposto': 'ISS',
                        'Base_Calculo': receita_servicos,
                        'Aliquota': 5.0,
                        'Valor': iss,
                        'Mes_Ano': col.strftime('%Y-%m')
                    })
                
                # PIS - sobre total (livros isentos na prática, mas simplificado)
                pis = receitas_mes * 0.0065
                impostos.append({
                    'Data': col,
                    'Imposto': 'PIS',
                    'Base_Calculo': receitas_mes,
                    'Aliquota': 0.65,
                    'Valor': pis,
                    'Mes_Ano': col.strftime('%Y-%m')
                })
                
                # COFINS - sobre total
                cofins = receitas_mes * 0.03
                impostos.append({
                    'Data': col,
                    'Imposto': 'COFINS',
                    'Base_Calculo': receitas_mes,
                    'Aliquota': 3.0,
                    'Valor': cofins,
                    'Mes_Ano': col.strftime('%Y-%m')
                })
                
                # CSLL - 9% sobre 32% da receita
                base_csll = receitas_mes * 0.32
                csll = base_csll * 0.09
                impostos.append({
                    'Data': col,
                    'Imposto': 'CSLL',
                    'Base_Calculo': base_csll,
                    'Aliquota': 9.0,
                    'Valor': csll,
                    'Mes_Ano': col.strftime('%Y-%m')
                })
                
                # IRPJ - 15% + 10% sobre excesso
                base_irpj = receitas_mes * 0.32
                irpj = base_irpj * 0.15
                if base_irpj > 20000:  # Adicional de 10%
                    irpj += (base_irpj - 20000) * 0.10
                
                impostos.append({
                    'Data': col,
                    'Imposto': 'IRPJ',
                    'Base_Calculo': base_irpj,
                    'Aliquota': 15.0,
                    'Valor': irpj,
                    'Mes_Ano': col.strftime('%Y-%m')
                })
        
        return pd.DataFrame(impostos)
    
    def gerar_resumo_anual(self):
        """Gera resumo consolidado por ano"""
        resumos = []
        
        for ano in range(2025, 2031):
            resumo_ano = {
                'Ano': ano,
                'Receitas_Total': 0,
                'Custos_Total': 0,
                'Impostos_Total': 0,
                'Despesas_Total': 0,
                'Resultado_Liquido': 0,
                'Margem_Liquida': 0
            }
            
            # Receitas do ano
            if self.dados_processados['receitas'] is not None:
                receitas_ano = self.dados_processados['receitas'][
                    self.dados_processados['receitas']['Data'].dt.year == ano
                ]['Valor'].sum()
                resumo_ano['Receitas_Total'] = receitas_ano
            
            # Custos do ano  
            if self.dados_processados['custos'] is not None:
                custos_ano = self.dados_processados['custos'][
                    self.dados_processados['custos']['Data'].dt.year == ano
                ]['Valor'].sum()
                resumo_ano['Custos_Total'] = custos_ano
            
            # Impostos do ano
            if self.dados_processados['impostos'] is not None:
                impostos_ano = self.dados_processados['impostos'][
                    self.dados_processados['impostos']['Data'].dt.year == ano
                ]['Valor'].sum()
                resumo_ano['Impostos_Total'] = impostos_ano
            
            # Despesas do ano
            if self.dados_processados['despesas'] is not None:
                despesas_ano = self.dados_processados['despesas'][
                    self.dados_processados['despesas']['Data'].dt.year == ano
                ]['Valor'].sum()
                resumo_ano['Despesas_Total'] = despesas_ano
            
            # Resultado líquido
            resultado = (resumo_ano['Receitas_Total'] - 
                        resumo_ano['Custos_Total'] - 
                        resumo_ano['Impostos_Total'] - 
                        resumo_ano['Despesas_Total'])
            resumo_ano['Resultado_Liquido'] = resultado
            
            # Margem líquida
            if resumo_ano['Receitas_Total'] > 0:
                margem = (resultado / resumo_ano['Receitas_Total']) * 100
                resumo_ano['Margem_Liquida'] = margem
            
            resumos.append(resumo_ano)
        
        return pd.DataFrame(resumos)
    
    def processar_matriz_completa(self):
        """Processa a matriz completa de forma unificada"""
        print("\n INICIANDO PROCESSAMENTO DA MATRIZ UNIFICADA")
        print("=" * 60)
        
        # Carrega matriz
        if not self.carregar_matriz():
            return False
        
        # Identifica colunas de data
        colunas_data = self.identificar_colunas_data()
        if not colunas_data:
            print("ERRO: Nenhuma coluna de data encontrada")
            return False
        
        print(f"\n Processando dados para {len(colunas_data)} meses...")
        
        # Processa cada seção
        print(" Processando receitas...")
        self.dados_processados['receitas'] = self.processar_receitas(colunas_data)
        
        print(" Processando custos...")
        self.dados_processados['custos'] = self.processar_custos(colunas_data)
        
        print(" Processando despesas...")
        self.dados_processados['despesas'] = self.processar_despesas(colunas_data)
        
        print(" Calculando impostos...")
        self.dados_processados['impostos'] = self.calcular_impostos_brasileiros(
            self.dados_processados['receitas'], colunas_data
        )
        
        print(" Gerando resumo anual...")
        self.dados_processados['resumo'] = self.gerar_resumo_anual()
        
        # Estatísticas finais
        print(f"\n PROCESSAMENTO CONCLUIDO!")
        print(f" Receitas: {len(self.dados_processados['receitas'])} registros")
        print(f" Custos: {len(self.dados_processados['custos'])} registros")
        print(f" Impostos: {len(self.dados_processados['impostos'])} registros")
        print(f" Despesas: {len(self.dados_processados['despesas'])} registros")
        print(f" Resumo: {len(self.dados_processados['resumo'])} anos")
        
        return True
    
    def exportar_dados_unificados(self, arquivo_saida="matriz_unificada_processada.xlsx"):
        """Exporta todos os dados processados para Excel"""
        try:
            print(f"\n Exportando dados unificados para: {arquivo_saida}")
            
            with pd.ExcelWriter(arquivo_saida, engine='openpyxl') as writer:
                
                # Receitas
                if self.dados_processados['receitas'] is not None:
                    df_rec = self.dados_processados['receitas'].copy()
                    df_rec['Data'] = df_rec['Data'].dt.strftime('%d/%m/%Y')
                    df_rec.to_excel(writer, sheet_name='Receitas', index=False)
                
                # Custos
                if self.dados_processados['custos'] is not None:
                    df_cus = self.dados_processados['custos'].copy()
                    df_cus['Data'] = df_cus['Data'].dt.strftime('%d/%m/%Y')
                    df_cus.to_excel(writer, sheet_name='Custos', index=False)
                
                # Impostos
                if self.dados_processados['impostos'] is not None:
                    df_imp = self.dados_processados['impostos'].copy()
                    df_imp['Data'] = df_imp['Data'].dt.strftime('%d/%m/%Y')
                    df_imp.to_excel(writer, sheet_name='Impostos', index=False)
                
                # Despesas
                if self.dados_processados['despesas'] is not None:
                    df_desp = self.dados_processados['despesas'].copy()
                    df_desp['Data'] = df_desp['Data'].dt.strftime('%d/%m/%Y')
                    df_desp.to_excel(writer, sheet_name='Despesas', index=False)
                
                # Resumo anual
                if self.dados_processados['resumo'] is not None:
                    self.dados_processados['resumo'].to_excel(writer, sheet_name='Resumo_Anual', index=False)
                
                # Dashboard data (formato otimizado para o dashboard)
                self.gerar_dados_dashboard().to_excel(writer, sheet_name='Dashboard_Data', index=False)
            
            print(f" Dados exportados com sucesso!")
            return True
            
        except Exception as e:
            print(f"ERRO ao exportar: {e}")
            return False
    
    def gerar_dados_dashboard(self):
        """Gera dados otimizados para o dashboard"""
        dados_dashboard = []
        
        # Agrupa todos os dados por mês
        if self.dados_processados['receitas'] is not None:
            receitas_mensais = self.dados_processados['receitas'].groupby('Mes_Ano')['Valor'].sum()
            
            for mes_ano, valor in receitas_mensais.items():
                dados_dashboard.append({
                    'Mes_Ano': mes_ano,
                    'Tipo': 'Receita',
                    'Valor': valor
                })
        
        # Adiciona custos, impostos e despesas...
        # (continua a lógica)
        
        return pd.DataFrame(dados_dashboard)
    
    def obter_dados(self, tipo):
        """Retorna dados processados por tipo"""
        return self.dados_processados.get(tipo)

def main():
    """Função principal para teste"""
    importador = ImportadorMatrizUnificada()
    
    if importador.processar_matriz_completa():
        importador.exportar_dados_unificados()
        
        print("\n MATRIZ UNIFICADA PROCESSADA COM SUCESSO!")
        print("Agora voce tem todos os dados organizados e prontos para uso!")
    else:
        print("ERRO no processamento da matriz")

if __name__ == "__main__":
    main()