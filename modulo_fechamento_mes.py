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
    """Cria card de métrica estilizado com design moderno"""
    cores = {
        'positive': {
            'gradient': 'linear-gradient(135deg, #10b981 0%, #059669 100%)',
            'icon': '↗'
        },
        'negative': {
            'gradient': 'linear-gradient(135deg, #ef4444 0%, #dc2626 100%)',
            'icon': '↘'
        },
        'neutral': {
            'gradient': 'linear-gradient(135deg, #6366f1 0%, #4f46e5 100%)',
            'icon': '='
        },
        'warning': {
            'gradient': 'linear-gradient(135deg, #f59e0b 0%, #d97706 100%)',
            'icon': '!'
        }
    }

    config = cores.get(cor, cores['neutral'])

    return f"""
    <div style="
        background: {config['gradient']};
        border-radius: 12px;
        padding: 16px;
        margin-bottom: 12px;
        box-shadow: 0 6px 15px rgba(0, 0, 0, 0.12);
        border: 1px solid rgba(255, 255, 255, 0.1);
        min-height: 95px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    ">
        <div style="
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            margin-bottom: 6px;
        ">
            <div style="
                color: rgba(255, 255, 255, 0.9);
                font-size: 0.75rem;
                text-transform: uppercase;
                letter-spacing: 0.5px;
                font-weight: 500;
            ">
                {label}
            </div>
            <div style="font-size: 1.1rem; opacity: 0.7;">
                {config['icon']}
            </div>
        </div>
        <div>
            <div style="
                font-size: 1.5rem;
                font-weight: bold;
                color: white;
                margin-bottom: 4px;
                text-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
            ">
                {valor}
            </div>
            <div style="
                color: rgba(255, 255, 255, 0.85);
                font-size: 0.7rem;
                font-weight: 400;
            ">
                {detalhe}
            </div>
        </div>
    </div>
    """

def main_fechamento_mes():
    """Módulo principal de fechamento do mês"""

    st.title("Fechamento do Mês")
    st.markdown("### Análise Completa - Outubro 2025")

    # Header com data
    st.info("**Última atualização:** 05/11/2025 | **Período:** Outubro 2025 (mês completo)")

    # ==================== SEÇÃO FATURAMENTO ====================
    st.markdown("---")
    st.markdown("## Faturamento")
    st.caption("Vendas realizadas e processadas em Outubro/2025")

    # Métricas principais de faturamento
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown(criar_metrica_card(
            "Faturamento Total",
            "R$ 159.565,41",
            "104 transações B2C",
            "positive"
        ), unsafe_allow_html=True)

    with col2:
        st.markdown(criar_metrica_card(
            "Faturamento B2B",
            "R$ 0,00",
            "Sem vendas B2B",
            "neutral"
        ), unsafe_allow_html=True)

    with col3:
        st.markdown(criar_metrica_card(
            "Faturamento B2C",
            "R$ 159.565,41",
            "104 transações",
            "positive"
        ), unsafe_allow_html=True)

    with col4:
        st.markdown(criar_metrica_card(
            "Ticket Médio",
            "R$ 1.534,28",
            "Média por transação",
            "neutral"
        ), unsafe_allow_html=True)

    # Tabela de faturamento por adquirente
    st.markdown("#### Faturamento por Adquirente")

    df_faturamento = pd.DataFrame([
        {
            'Adquirente': 'Pagar.me',
            'Transações': '97',
            'Faturamento': 144576.41,
            '%': '90,6%',
            'Ticket Médio': 'R$ 1.490,48',
            'Taxa': '9,20%',
            'Status': 'Nacional'
        },
        {
            'Adquirente': 'Crypto',
            'Transações': '6',
            'Faturamento': 11991.00,
            '%': '7,5%',
            'Ticket Médio': 'R$ 1.998,50',
            'Taxa': '~1,00%',
            'Status': 'Cripto'
        },
        {
            'Adquirente': 'Stripe',
            'Transações': '1',
            'Faturamento': 2998.00,
            '%': '1,9%',
            'Ticket Médio': 'R$ 2.998,00',
            'Taxa': '~4,00%',
            'Status': 'Internacional'
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
    st.markdown("#### Distribuição do Faturamento")

    for idx, row in df_faturamento.iterrows():
        percentual = float(row['%'].replace('%', '').replace(',', '.'))
        st.markdown(f"**{row['Adquirente']}** - {row['%']}")
        st.progress(percentual / 100)

    # ==================== SEÇÃO CAIXA ====================
    st.markdown("---")
    st.markdown("## Fluxo de Caixa")
    st.caption("Valores efetivamente recebidos no extrato bancário")

    # Métricas principais de caixa
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown(criar_metrica_card(
            "Total Bruto Recebido",
            "R$ 144.576,41",
            "Pagar.me gateway",
            "positive"
        ), unsafe_allow_html=True)

    with col2:
        st.markdown(criar_metrica_card(
            "Total de Taxas Pagas",
            "R$ 13.299,11",
            "9,20% do bruto",
            "negative"
        ), unsafe_allow_html=True)

    with col3:
        st.markdown(criar_metrica_card(
            "Valor Líquido",
            "R$ 122.540,21",
            "Após taxas e chargebacks",
            "positive"
        ), unsafe_allow_html=True)

    with col4:
        st.markdown(criar_metrica_card(
            "Chargebacks",
            "R$ 2.157,84",
            "Contestações",
            "warning"
        ), unsafe_allow_html=True)

    # Tabela de caixa por adquirente
    st.markdown("#### Caixa por Adquirente")

    df_caixa = pd.DataFrame([
        {
            'Adquirente': 'Pagar.me',
            'Valor Bruto': 144576.41,
            'Taxas Pagas': 13299.11,
            'Taxa %': '9,20%',
            'Valor Líquido': 122540.21,
            'Tipo': 'Confirmado'
        },
        {
            'Adquirente': 'Crypto',
            'Valor Bruto': 11991.00,
            'Taxas Pagas': 119.91,
            'Taxa %': '~1,00%',
            'Valor Líquido': 11871.09,
            'Tipo': 'Estimado'
        },
        {
            'Adquirente': 'Stripe',
            'Valor Bruto': 2998.00,
            'Taxas Pagas': 119.92,
            'Taxa %': '~4,00%',
            'Valor Líquido': 2878.08,
            'Tipo': 'Estimado'
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
    st.markdown("#### Composição das Taxas Pagas")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Taxa Adquirente (3.25%)", "R$ 5.185,88")
    with col2:
        st.metric("Taxa Antecipação (8.31%)", "R$ 8.113,23")
    with col3:
        st.metric("Chargebacks", "R$ 2.157,84")
    with col4:
        st.metric("Gateway (Pagar.me)", "R$ 13.299,11")

    # ==================== COMPARATIVO ====================
    st.markdown("---")
    st.markdown("## Faturamento vs Caixa")
    st.caption("Comparação entre vendas realizadas e valores recebidos")

    df_comparativo = pd.DataFrame([
        {
            'Adquirente': 'Pagar.me',
            'Faturamento': 144576.41,
            'Recebido': 144576.41,
            'Diferença': 0.00,
            'Observação': 'Recebimento do mês'
        },
        {
            'Adquirente': 'Crypto',
            'Faturamento': 11991.00,
            'Recebido': 0.00,
            'Diferença': -11991.00,
            'Observação': 'A receber'
        },
        {
            'Adquirente': 'Stripe',
            'Faturamento': 2998.00,
            'Recebido': 0.00,
            'Diferença': -2998.00,
            'Observação': 'A receber'
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
    st.markdown("## Resumo Executivo")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 30px; border-radius: 12px; text-align: center;">
            <h3 style="margin: 0; font-size: 2rem;">R$ 159.565</h3>
            <p style="margin: 10px 0 0 0; opacity: 0.9;">Faturamento Total</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #10b981 0%, #059669 100%); color: white; padding: 30px; border-radius: 12px; text-align: center;">
            <h3 style="margin: 0; font-size: 2rem;">R$ 144.576</h3>
            <p style="margin: 10px 0 0 0; opacity: 0.9;">Total Recebido</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #ef4444 0%, #dc2626 100%); color: white; padding: 30px; border-radius: 12px; text-align: center;">
            <h3 style="margin: 0; font-size: 2rem;">R$ 13.299</h3>
            <p style="margin: 10px 0 0 0; opacity: 0.9;">Total de Taxas</p>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #6366f1 0%, #4f46e5 100%); color: white; padding: 30px; border-radius: 12px; text-align: center;">
            <h3 style="margin: 0; font-size: 2rem;">R$ 122.540</h3>
            <p style="margin: 10px 0 0 0; opacity: 0.9;">Valor Líquido</p>
        </div>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    main_fechamento_mes()
