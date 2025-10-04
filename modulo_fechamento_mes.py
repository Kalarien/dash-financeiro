#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MÓDULO FECHAMENTO DO MÊS
Dashboard executivo com análise completa do último mês fechado
"""

import streamlit as st
import pandas as pd

def formatar_moeda_br(valor):
    """Formata valor em moeda brasileira"""
    if pd.isna(valor) or valor == 0:
        return "R$ 0,00"
    return f"R$ {valor:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')

def criar_metrica_card(label, valor, detalhe="", cor="neutral"):
    """Cria card de métrica estilizado"""
    cores = {
        'positive': '#10b981',
        'negative': '#ef4444',
        'neutral': '#6366f1',
        'warning': '#f59e0b'
    }

    cor_hex = cores.get(cor, cores['neutral'])

    return f"""
    <div style="
        background: #f9fafb;
        border: 1px solid #e5e7eb;
        border-left: 4px solid {cor_hex};
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 15px;
    ">
        <div style="color: #6b7280; font-size: 0.875rem; text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 8px;">
            {label}
        </div>
        <div style="font-size: 1.75rem; font-weight: bold; color: #111827; margin-bottom: 5px;">
            {valor}
        </div>
        <div style="color: #9ca3af; font-size: 0.875rem;">
            {detalhe}
        </div>
    </div>
    """

def main_fechamento_mes():
    """Módulo principal de fechamento do mês"""

    st.title("📊 Fechamento do Mês")
    st.markdown("### Análise Completa - Setembro 2025")

    # Header com data
    st.info("📅 **Última atualização:** 04/10/2025 | **Período:** Setembro 2025 (mês completo)")

    # ==================== SEÇÃO FATURAMENTO ====================
    st.markdown("---")
    st.markdown("## 📈 Faturamento")
    st.caption("Vendas realizadas e processadas em Setembro/2025")

    # Métricas principais de faturamento
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown(criar_metrica_card(
            "Faturamento Total",
            "R$ 257.074,18",
            "68 transações + B2B",
            "positive"
        ), unsafe_allow_html=True)

    with col2:
        st.markdown(criar_metrica_card(
            "Faturamento B2B",
            "R$ 120.000,00",
            "Vendas corporativas",
            "neutral"
        ), unsafe_allow_html=True)

    with col3:
        st.markdown(criar_metrica_card(
            "Faturamento B2C",
            "R$ 137.074,18",
            "68 transações",
            "positive"
        ), unsafe_allow_html=True)

    with col4:
        st.markdown(criar_metrica_card(
            "Taxa Média B2C",
            "2,78%",
            "Sobre vendas B2C",
            "neutral"
        ), unsafe_allow_html=True)

    # Tabela de faturamento por adquirente
    st.markdown("#### Faturamento por Adquirente")

    df_faturamento = pd.DataFrame([
        {
            'Adquirente': 'B2B Corporativo',
            'Transações': '-',
            'Faturamento': 120000.00,
            '%': '46,7%',
            'Ticket Médio': '-',
            'Taxa': '-',
            'Status': '🟢 Empresarial'
        },
        {
            'Adquirente': 'Pagar.me',
            'Transações': '52',
            'Faturamento': 101901.78,
            '%': '39,6%',
            'Ticket Médio': 'R$ 1.959,65',
            'Taxa': '3,04%',
            'Status': '🟢 Nacional'
        },
        {
            'Adquirente': 'Stripe',
            'Transações': '5',
            'Faturamento': 11992.00,
            '%': '4,7%',
            'Ticket Médio': 'R$ 2.398,40',
            'Taxa': '4,01%',
            'Status': '🔵 Internacional'
        },
        {
            'Adquirente': 'Crypto',
            'Transações': '11',
            'Faturamento': 23180.40,
            '%': '9,0%',
            'Ticket Médio': 'R$ 2.107,31',
            'Taxa': '~1,00%',
            'Status': '🟡 Cripto'
        }
    ])

    # Formata coluna de faturamento
    df_faturamento_display = df_faturamento.copy()
    df_faturamento_display['Faturamento'] = df_faturamento_display['Faturamento'].apply(formatar_moeda_br)

    st.dataframe(
        df_faturamento_display,
        use_container_width=True,
        hide_index=True
    )

    # Distribuição visual do faturamento
    st.markdown("#### 📊 Distribuição do Faturamento")

    for idx, row in df_faturamento.iterrows():
        percentual = float(row['%'].replace('%', '').replace(',', '.'))
        st.markdown(f"**{row['Adquirente']}** - {row['%']}")
        st.progress(percentual / 100)

    # ==================== SEÇÃO CAIXA ====================
    st.markdown("---")
    st.markdown("## 💰 Fluxo de Caixa")
    st.caption("Valores efetivamente recebidos no extrato bancário")

    # Métricas principais de caixa
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown(criar_metrica_card(
            "Total Bruto Recebido",
            "R$ 485.718,40",
            "Incluindo antecipações",
            "positive"
        ), unsafe_allow_html=True)

    with col2:
        st.markdown(criar_metrica_card(
            "Total de Taxas Pagas",
            "R$ 56.965,19",
            "11,73% do bruto",
            "negative"
        ), unsafe_allow_html=True)

    with col3:
        st.markdown(criar_metrica_card(
            "Valor Líquido",
            "R$ 428.753,21",
            "Após todas as taxas",
            "positive"
        ), unsafe_allow_html=True)

    with col4:
        st.markdown(criar_metrica_card(
            "Antecipações",
            "R$ 256.464,47",
            "Recebíveis adiantados",
            "warning"
        ), unsafe_allow_html=True)

    # Tabela de caixa por adquirente
    st.markdown("#### Caixa por Adquirente")

    df_caixa = pd.DataFrame([
        {
            'Adquirente': 'Asaas',
            'Valor Bruto': 332874.07,
            'Taxas Pagas': 46617.34,
            'Taxa %': '14,00%',
            'Valor Líquido': 286256.73,
            'Tipo': '🟡 Com Antecipação'
        },
        {
            'Adquirente': 'Pagar.me',
            'Valor Bruto': 117671.93,
            'Taxas Pagas': 9635.62,
            'Taxa %': '8,19%',
            'Valor Líquido': 108036.31,
            'Tipo': '🟡 Com Antecipação'
        },
        {
            'Adquirente': 'Crypto',
            'Valor Bruto': 23180.40,
            'Taxas Pagas': 231.80,
            'Taxa %': '1,00%',
            'Valor Líquido': 22948.60,
            'Tipo': '🟢 Estimado'
        },
        {
            'Adquirente': 'Stripe',
            'Valor Bruto': 11992.00,
            'Taxas Pagas': 480.43,
            'Taxa %': '4,01%',
            'Valor Líquido': 11511.57,
            'Tipo': '🔵 Confirmado'
        }
    ])

    # Formata valores
    df_caixa_display = df_caixa.copy()
    df_caixa_display['Valor Bruto'] = df_caixa_display['Valor Bruto'].apply(formatar_moeda_br)
    df_caixa_display['Taxas Pagas'] = df_caixa_display['Taxas Pagas'].apply(formatar_moeda_br)
    df_caixa_display['Valor Líquido'] = df_caixa_display['Valor Líquido'].apply(formatar_moeda_br)

    st.dataframe(
        df_caixa_display,
        use_container_width=True,
        hide_index=True
    )

    # Composição das taxas
    st.markdown("#### 💸 Composição das Taxas Pagas")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Taxa de Cobrança (Asaas)", "R$ 13.099,41")
    with col2:
        st.metric("Taxa de Antecipação", "R$ 40.815,23")
    with col3:
        st.metric("Taxa de Operação (Pagar.me)", "R$ 2.338,32")
    with col4:
        st.metric("Outras Taxas", "R$ 712,23")

    # ==================== COMPARATIVO ====================
    st.markdown("---")
    st.markdown("## ⚖️ Faturamento vs Caixa")
    st.caption("Comparação entre vendas realizadas e valores recebidos")

    df_comparativo = pd.DataFrame([
        {
            'Adquirente': 'B2B Corporativo',
            'Faturamento': 120000.00,
            'Recebido': 10000.00,
            'Diferença': -110000.00,
            'Observação': 'R$ 10k recebido via Pagar.me / R$ 110k a receber'
        },
        {
            'Adquirente': 'Pagar.me',
            'Faturamento': 101901.78,
            'Recebido': 117671.93,
            'Diferença': 15770.15,
            'Observação': 'Parcelas anteriores + R$ 10k B2B'
        },
        {
            'Adquirente': 'Asaas',
            'Faturamento': 0.00,
            'Recebido': 332874.07,
            'Diferença': 332874.07,
            'Observação': 'Recebimentos de meses anteriores'
        },
        {
            'Adquirente': 'Stripe',
            'Faturamento': 11992.00,
            'Recebido': 11992.00,
            'Diferença': 0.00,
            'Observação': 'Valores conferem'
        },
        {
            'Adquirente': 'Crypto',
            'Faturamento': 23180.40,
            'Recebido': 23180.40,
            'Diferença': 0.00,
            'Observação': 'Valores conferem'
        }
    ])

    # Formata valores
    df_comparativo_display = df_comparativo.copy()
    df_comparativo_display['Faturamento'] = df_comparativo_display['Faturamento'].apply(formatar_moeda_br)
    df_comparativo_display['Recebido'] = df_comparativo_display['Recebido'].apply(formatar_moeda_br)
    df_comparativo_display['Diferença'] = df_comparativo_display['Diferença'].apply(formatar_moeda_br)

    st.dataframe(
        df_comparativo_display,
        use_container_width=True,
        hide_index=True
    )

    # ==================== RESUMO EXECUTIVO ====================
    st.markdown("---")
    st.markdown("## 📋 Resumo Executivo")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 30px; border-radius: 12px; text-align: center;">
            <h3 style="margin: 0; font-size: 2rem;">R$ 257.074</h3>
            <p style="margin: 10px 0 0 0; opacity: 0.9;">Faturamento Total</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #10b981 0%, #059669 100%); color: white; padding: 30px; border-radius: 12px; text-align: center;">
            <h3 style="margin: 0; font-size: 2rem;">R$ 485.718</h3>
            <p style="margin: 10px 0 0 0; opacity: 0.9;">Total Recebido</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #ef4444 0%, #dc2626 100%); color: white; padding: 30px; border-radius: 12px; text-align: center;">
            <h3 style="margin: 0; font-size: 2rem;">R$ 56.965</h3>
            <p style="margin: 10px 0 0 0; opacity: 0.9;">Total de Taxas</p>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #6366f1 0%, #4f46e5 100%); color: white; padding: 30px; border-radius: 12px; text-align: center;">
            <h3 style="margin: 0; font-size: 2rem;">R$ 428.753</h3>
            <p style="margin: 10px 0 0 0; opacity: 0.9;">Valor Líquido</p>
        </div>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    main_fechamento_mes()
