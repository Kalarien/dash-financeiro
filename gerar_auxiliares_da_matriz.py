#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GERADOR DE ARQUIVOS AUXILIARES
Gera despesas_processadas_correto.xlsx e sistema_financeiro_integrado.xlsx
a partir da Matriz financeira.xlsx
"""

import pandas as pd
import numpy as np
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

def carregar_matriz():
    """Carrega a Matriz financeira.xlsx"""
    try:
        print("📥 Carregando Matriz financeira.xlsx...")
        df_matriz = pd.read_excel('Matriz financeira.xlsx', sheet_name='Matriz Detalhada')
        print(f"✅ Matriz carregada: {df_matriz.shape}")
        return df_matriz
    except Exception as e:
        print(f"❌ Erro ao carregar matriz: {e}")
        return None

def identificar_colunas_data(df_matriz):
    """Identifica colunas de data"""
    colunas_data = []
    for col in df_matriz.columns:
        if isinstance(col, datetime):
            colunas_data.append(col)
    print(f"📅 Encontradas {len(colunas_data)} colunas de data")
    return sorted(colunas_data)

def gerar_receitas(df_matriz, colunas_data):
    """Gera arquivo de receitas"""
    try:
        print("📊 Processando receitas...")
        receitas = []

        # Receitas Realizado
        linha_real = df_matriz[df_matriz['Categoria'] == 'Receitas Realizado']
        if not linha_real.empty:
            for col in colunas_data:
                valor = linha_real[col].iloc[0]
                if pd.notna(valor) and valor > 0:
                    receitas.append({
                        'Data': col.strftime('%d/%m/%Y'),
                        'Tipo': 'Receita',
                        'Status': 'Realizado',
                        'Valor': float(valor),
                        'Mes_Ano': col.strftime('%Y-%m')
                    })

        # Receitas Projetado
        linha_proj = df_matriz[df_matriz['Categoria'] == 'Receitas Projetado']
        if not linha_proj.empty:
            for col in colunas_data:
                valor = linha_proj[col].iloc[0]
                if pd.notna(valor) and valor > 0:
                    receitas.append({
                        'Data': col.strftime('%d/%m/%Y'),
                        'Tipo': 'Receita',
                        'Status': 'Projetado',
                        'Valor': float(valor),
                        'Mes_Ano': col.strftime('%Y-%m')
                    })

        # B2B Projetado
        linha_b2b = df_matriz[df_matriz['Categoria'] == 'B2B Projetado']
        if not linha_b2b.empty:
            for col in colunas_data:
                valor = linha_b2b[col].iloc[0]
                if pd.notna(valor) and valor > 0:
                    receitas.append({
                        'Data': col.strftime('%d/%m/%Y'),
                        'Tipo': 'Receita_B2B',
                        'Status': 'Projetado',
                        'Valor': float(valor),
                        'Mes_Ano': col.strftime('%Y-%m')
                    })

        df_receitas = pd.DataFrame(receitas)
        print(f"✅ Receitas: {len(df_receitas)} registros")
        return df_receitas

    except Exception as e:
        print(f"❌ Erro ao gerar receitas: {e}")
        return pd.DataFrame()

def gerar_despesas(df_matriz, colunas_data):
    """Gera arquivo de despesas"""
    try:
        print("📊 Processando despesas...")
        despesas = []

        categoria_atual = None
        na_secao_despesas = False

        for idx, row in df_matriz.iterrows():
            categoria = row['Categoria']

            # Pula NaN
            if pd.isna(categoria):
                continue

            categoria = str(categoria)  # NÃO faz strip para preservar espaços

            # Identifica início da seção de despesas
            if categoria.strip() == 'DESPESAS':
                na_secao_despesas = True
                continue

            # Termina quando encontra TOTAL DESPESAS
            if categoria.strip() in ['TOTAL DESPESAS', 'RESULTADO LÍQUIDO']:
                break

            # Só processa se estiver na seção de despesas
            if not na_secao_despesas:
                continue

            # Determina categoria e descrição
            if categoria.startswith('  → '):
                # Item detalhado
                descricao = categoria.replace('  → ', '').strip()
                cat_final = categoria_atual if categoria_atual else 'Outros'

                # Processa valores por mês
                for col in colunas_data:
                    valor = row[col]
                    if pd.notna(valor) and valor > 0:
                        # Determina status baseado na coluna Tipo
                        tipo = row.get('Tipo', '')
                        if pd.notna(tipo) and tipo == 'Realizado':
                            status = 'Realizado'
                        elif pd.notna(tipo) and tipo == 'Projetado':
                            status = 'Projetado'
                        else:
                            # Se não tem tipo, considera realizado até setembro/2025, projetado depois
                            status = 'Realizado' if col <= datetime(2025, 9, 30) else 'Projetado'

                        despesas.append({
                            'Data': col.strftime('%Y-%m-%d'),
                            'Categoria': cat_final,
                            'Area': 'Matriz',
                            'Descricao': descricao,
                            'Valor': float(valor),
                            'Status': status,
                            'Mes': col.strftime('%b').lower(),
                            'Continuidade': 'Matriz_Financeira'
                        })
            else:
                # Categoria principal (sem →)
                categoria_atual = categoria

        df_despesas = pd.DataFrame(despesas)
        print(f"✅ Despesas: {len(df_despesas)} registros")
        return df_despesas

    except Exception as e:
        print(f"❌ Erro ao gerar despesas: {e}")
        import traceback
        traceback.print_exc()
        return pd.DataFrame()

def gerar_fluxo_diario(df_receitas):
    """Gera fluxo diário simplificado"""
    try:
        print("📊 Gerando fluxo diário...")

        if df_receitas.empty:
            return pd.DataFrame()

        # Converte datas
        df_fluxo = df_receitas.copy()
        df_fluxo['Data'] = pd.to_datetime(df_fluxo['Data'], format='%d/%m/%Y')

        # Adiciona coluna de descrição
        df_fluxo['Descricao'] = df_fluxo.apply(
            lambda x: f"{x['Tipo']} - {x['Status']}", axis=1
        )

        # Formata data de volta
        df_fluxo['Data'] = df_fluxo['Data'].dt.strftime('%d/%m/%Y')

        # Reordena colunas
        df_fluxo = df_fluxo[['Data', 'Descricao', 'Valor', 'Status']]

        print(f"✅ Fluxo diário: {len(df_fluxo)} registros")
        return df_fluxo

    except Exception as e:
        print(f"❌ Erro ao gerar fluxo: {e}")
        return pd.DataFrame()

def exportar_arquivos(df_despesas, df_receitas):
    """Exporta arquivos auxiliares"""
    try:
        print("\n💾 Exportando arquivos auxiliares...")

        # Backup dos arquivos existentes
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')

        try:
            df_backup = pd.read_excel('despesas_processadas_correto.xlsx', sheet_name='Despesas_Completas')
            df_backup.to_excel(f'backup_despesas_{timestamp}.xlsx', index=False)
            print(f"📦 Backup despesas: backup_despesas_{timestamp}.xlsx")
        except:
            print("⚠️ Arquivo despesas não existe (será criado)")

        try:
            df_backup = pd.read_excel('sistema_financeiro_integrado.xlsx', sheet_name='Receitas')
            df_backup.to_excel(f'backup_receitas_{timestamp}.xlsx', index=False)
            print(f"📦 Backup receitas: backup_receitas_{timestamp}.xlsx")
        except:
            print("⚠️ Arquivo sistema integrado não existe (será criado)")

        # Exporta despesas_processadas_correto.xlsx
        if not df_despesas.empty:
            with pd.ExcelWriter('despesas_processadas_correto.xlsx', engine='openpyxl') as writer:
                df_despesas.to_excel(writer, sheet_name='Despesas_Completas', index=False)
            print("✅ despesas_processadas_correto.xlsx atualizado")

        # Exporta sistema_financeiro_integrado.xlsx
        if not df_receitas.empty:
            df_fluxo = gerar_fluxo_diario(df_receitas)

            with pd.ExcelWriter('sistema_financeiro_integrado.xlsx', engine='openpyxl') as writer:
                df_receitas.to_excel(writer, sheet_name='Receitas', index=False)
                if not df_fluxo.empty:
                    df_fluxo.to_excel(writer, sheet_name='Fluxo_Diario', index=False)
            print("✅ sistema_financeiro_integrado.xlsx atualizado")

        return True

    except Exception as e:
        print(f"❌ Erro ao exportar: {e}")
        import traceback
        traceback.print_exc()
        return False

def limpar_cache_streamlit():
    """Limpa cache do Streamlit"""
    try:
        with open('trigger_reload.txt', 'w') as f:
            f.write(datetime.now().isoformat())
        print("🔄 Cache do Streamlit limpo")
        return True
    except:
        return False

def main():
    """Função principal"""
    print("=" * 70)
    print("    GERADOR DE ARQUIVOS AUXILIARES DA MATRIZ FINANCEIRA")
    print("=" * 70)

    # 1. Carrega matriz
    df_matriz = carregar_matriz()
    if df_matriz is None:
        print("❌ Não foi possível carregar a matriz")
        return

    # 2. Identifica colunas de data
    colunas_data = identificar_colunas_data(df_matriz)
    if not colunas_data:
        print("❌ Nenhuma coluna de data encontrada")
        return

    # 3. Gera receitas
    df_receitas = gerar_receitas(df_matriz, colunas_data)

    # 4. Gera despesas
    df_despesas = gerar_despesas(df_matriz, colunas_data)

    # 5. Exporta arquivos
    if exportar_arquivos(df_despesas, df_receitas):
        print("\n🎉 ARQUIVOS AUXILIARES GERADOS COM SUCESSO!")
        print(f"\n📊 Resumo:")
        print(f"   • Receitas: {len(df_receitas)} registros")
        print(f"   • Despesas: {len(df_despesas)} registros")
        print(f"   • Período: {colunas_data[0].strftime('%m/%Y')} a {colunas_data[-1].strftime('%m/%Y')}")

        # 6. Limpa cache
        limpar_cache_streamlit()

        print(f"\n📋 Próximos passos:")
        print(f"   1. 🔄 Recarregue o dashboard (F5)")
        print(f"   2. ✅ Verifique as abas Realizado, Gráficos e Fluxo de Caixa")

    else:
        print("\n❌ Erro ao gerar arquivos auxiliares")

if __name__ == "__main__":
    main()
