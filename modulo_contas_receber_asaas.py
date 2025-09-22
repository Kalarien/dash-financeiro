import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import streamlit as st

class ContasReceberAsaas:
    def __init__(self):
        self.df_vendas = None
        self.df_extrato = None
        
    def carregar_dados(self, arquivo_cobrancas, arquivo_extrato):
        """
        Carrega e processa os dados dos arquivos do Asaas
        
        Args:
            arquivo_cobrancas: Arquivo Excel de cobranças (vendas)
            arquivo_extrato: Arquivo Excel do extrato Asaas (movimentações)
        """
        try:
            # Carregar vendas (competência)
            self.df_vendas = pd.read_excel(arquivo_cobrancas, sheet_name=0)
            self._processar_vendas()
            
            # Carregar extrato (caixa)
            self.df_extrato = pd.read_excel(arquivo_extrato, sheet_name=0, skiprows=2)
            self._processar_extrato()
            
            return True
            
        except Exception as e:
            st.error(f"Erro ao carregar dados: {e}")
            return False
    
    def _processar_vendas(self):
        """Processa dados de vendas (competência)"""
        # Converter datas
        self.df_vendas['Data de criação'] = pd.to_datetime(
            self.df_vendas['Data de criação'], 
            dayfirst=True, 
            errors='coerce'
        )
        
        # Converter valores
        self.df_vendas['Valor'] = pd.to_numeric(self.df_vendas['Valor'], errors='coerce')
        self.df_vendas['Valor Líquido'] = pd.to_numeric(self.df_vendas['Valor Líquido'], errors='coerce')
        
        # Filtrar apenas vendas válidas
        self.df_vendas = self.df_vendas[
            self.df_vendas['Data de criação'].notna() & 
            self.df_vendas['Valor'].notna()
        ]
        
        # Adicionar campos auxiliares
        self.df_vendas['Ano_Mes'] = self.df_vendas['Data de criação'].dt.to_period('M')
        self.df_vendas['Data_Venda'] = self.df_vendas['Data de criação'].dt.date
        
    def _processar_extrato(self):
        """Processa dados do extrato (caixa)"""
        # Limpar dados vazios
        self.df_extrato = self.df_extrato.dropna(how='all')
        self.df_extrato = self.df_extrato[self.df_extrato['Data'].notna()]
        
        # Converter datas
        self.df_extrato['Data'] = pd.to_datetime(
            self.df_extrato['Data'], 
            dayfirst=True, 
            errors='coerce'
        )
        
        # Converter valores
        self.df_extrato['Valor'] = pd.to_numeric(self.df_extrato['Valor'], errors='coerce')
        
        # Filtrar movimentações válidas
        self.df_extrato = self.df_extrato[
            self.df_extrato['Data'].notna() & 
            self.df_extrato['Valor'].notna()
        ]
        
        # Adicionar campos auxiliares
        self.df_extrato['Ano_Mes'] = self.df_extrato['Data'].dt.to_period('M')
        self.df_extrato['Data_Movimento'] = self.df_extrato['Data'].dt.date
        
    def obter_vendas_competencia(self, data_inicio=None, data_fim=None):
        """
        Retorna vendas por competência (quando foram feitas)
        
        Args:
            data_inicio: Data início do período
            data_fim: Data fim do período
        """
        if self.df_vendas is None:
            return pd.DataFrame()
            
        df_filtered = self.df_vendas.copy()
        
        if data_inicio:
            df_filtered = df_filtered[df_filtered['Data de criação'] >= pd.to_datetime(data_inicio)]
        if data_fim:
            df_filtered = df_filtered[df_filtered['Data de criação'] <= pd.to_datetime(data_fim)]
            
        # Agrupar por período
        vendas_competencia = df_filtered.groupby('Data_Venda').agg({
            'Valor': 'sum',
            'Valor Líquido': 'sum',
            'Identificador': 'count',
            'Forma de pagamento': lambda x: ', '.join(x.unique()[:3])
        }).rename(columns={
            'Valor': 'Valor_Bruto',
            'Valor Líquido': 'Valor_Liquido', 
            'Identificador': 'Qtd_Vendas',
            'Forma de pagamento': 'Formas_Pagamento'
        })
        
        return vendas_competencia.reset_index()
        
    def obter_recebimentos_caixa(self, data_inicio=None, data_fim=None):
        """
        Retorna recebimentos efetivos no caixa
        
        Args:
            data_inicio: Data início do período  
            data_fim: Data fim do período
        """
        if self.df_extrato is None:
            return pd.DataFrame()
            
        # Filtrar apenas recebimentos (créditos de cobrança)
        recebimentos = self.df_extrato[
            (self.df_extrato['Tipo do lançamento'] == 'Crédito') & 
            (self.df_extrato['Tipo de transação'] == 'Cobrança recebida')
        ].copy()
        
        if data_inicio:
            recebimentos = recebimentos[recebimentos['Data'] >= pd.to_datetime(data_inicio)]
        if data_fim:
            recebimentos = recebimentos[recebimentos['Data'] <= pd.to_datetime(data_fim)]
            
        # Agrupar por data
        recebimentos_caixa = recebimentos.groupby('Data_Movimento').agg({
            'Valor': 'sum',
            'Transação': 'count'
        }).rename(columns={
            'Valor': 'Valor_Recebido',
            'Transação': 'Qtd_Recebimentos'
        })
        
        return recebimentos_caixa.reset_index()
        
    def obter_antecipacoes(self, data_inicio=None, data_fim=None):
        """
        Retorna antecipações de recebíveis
        
        Args:
            data_inicio: Data início do período
            data_fim: Data fim do período  
        """
        if self.df_extrato is None:
            return pd.DataFrame()
            
        # Filtrar antecipações
        antecipacoes = self.df_extrato[
            self.df_extrato['Tipo de transação'] == 'Antecipação de parcelamento ou cobrança'
        ].copy()
        
        if data_inicio:
            antecipacoes = antecipacoes[antecipacoes['Data'] >= pd.to_datetime(data_inicio)]
        if data_fim:
            antecipacoes = antecipacoes[antecipacoes['Data'] <= pd.to_datetime(data_fim)]
            
        # Agrupar por data
        antecipacoes_resumo = antecipacoes.groupby('Data_Movimento').agg({
            'Valor': 'sum',
            'Transação': 'count'
        }).rename(columns={
            'Valor': 'Valor_Antecipado',
            'Transação': 'Qtd_Antecipacoes'
        })
        
        return antecipacoes_resumo.reset_index()
        
    def obter_taxas_antecipacao(self, data_inicio=None, data_fim=None):
        """
        Retorna taxas cobradas nas antecipações
        """
        if self.df_extrato is None:
            return pd.DataFrame()
            
        # Filtrar taxas de antecipação (débitos)
        taxas = self.df_extrato[
            self.df_extrato['Tipo de transação'] == 'Taxa de antecipação de parcelamento ou cobrança'
        ].copy()
        
        if data_inicio:
            taxas = taxas[taxas['Data'] >= pd.to_datetime(data_inicio)]
        if data_fim:
            taxas = taxas[taxas['Data'] <= pd.to_datetime(data_fim)]
            
        return taxas.groupby('Data_Movimento')['Valor'].sum().reset_index().rename(columns={'Valor': 'Taxa_Antecipacao'})
        
    def reconciliar_vendas_recebimentos(self, data_inicio=None, data_fim=None):
        """
        Reconcilia vendas (competência) com recebimentos (caixa)
        """
        vendas = self.obter_vendas_competencia(data_inicio, data_fim)
        recebimentos = self.obter_recebimentos_caixa(data_inicio, data_fim)
        antecipacoes = self.obter_antecipacoes(data_inicio, data_fim)
        taxas = self.obter_taxas_antecipacao(data_inicio, data_fim)
        
        # Criar resumo consolidado
        resumo = {
            'total_vendas_competencia': vendas['Valor_Bruto'].sum() if not vendas.empty else 0,
            'total_vendas_liquido': vendas['Valor_Liquido'].sum() if not vendas.empty else 0,
            'total_recebido_caixa': recebimentos['Valor_Recebido'].sum() if not recebimentos.empty else 0,
            'total_antecipado': antecipacoes['Valor_Antecipado'].sum() if not antecipacoes.empty else 0,
            'total_taxas_antecipacao': abs(taxas['Taxa_Antecipacao'].sum()) if not taxas.empty else 0,
            'saldo_a_receber': 0
        }
        
        # Calcular saldo a receber
        resumo['saldo_a_receber'] = (
            resumo['total_vendas_competencia'] - 
            resumo['total_recebido_caixa'] - 
            resumo['total_antecipado']
        )
        
        return {
            'resumo': resumo,
            'vendas_detalhadas': vendas,
            'recebimentos_detalhados': recebimentos,
            'antecipacoes_detalhadas': antecipacoes,
            'taxas_detalhadas': taxas
        }
        
    def obter_metricas_dashboard(self, periodo='completo'):
        """
        Retorna métricas consolidadas para o dashboard
        
        Args:
            periodo: 'completo', 'mes_atual' ou 'customizado'
        """
        if self.df_vendas is None or self.df_extrato is None:
            return {}
            
        if periodo == 'completo':
            # Período completo dos dados
            reconciliacao = self.reconciliar_vendas_recebimentos()
        else:
            # Período atual (último mês com dados)
            data_max = max(self.df_vendas['Data de criação'].max(), self.df_extrato['Data'].max())
            data_inicio_mes = data_max.replace(day=1)
            reconciliacao = self.reconciliar_vendas_recebimentos(data_inicio_mes, data_max)
        
        return {
            'vendas_mes': reconciliacao['resumo']['total_vendas_competencia'],
            'recebido_mes': reconciliacao['resumo']['total_recebido_caixa'],
            'antecipado_mes': reconciliacao['resumo']['total_antecipado'],
            'a_receber': reconciliacao['resumo']['saldo_a_receber'],
            'taxa_antecipacao_mes': reconciliacao['resumo']['total_taxas_antecipacao'],
            'detalhes': reconciliacao,
            'periodo_dados': {
                'vendas_min': self.df_vendas['Data de criação'].min(),
                'vendas_max': self.df_vendas['Data de criação'].max(),
                'extrato_min': self.df_extrato['Data'].min(),
                'extrato_max': self.df_extrato['Data'].max()
            }
        }