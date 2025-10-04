#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MÓDULO FLUXO DE CAIXA
Dashboard com saldos em conta e a receber por gateway
"""

import streamlit as st
import pandas as pd

def formatar_moeda_br(valor):
    """Formata valor em moeda brasileira"""
    if pd.isna(valor) or valor == 0:
        return "R$ 0,00"
    return f"R$ {valor:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')

def tab_resumo():
    """Tab de resumo consolidado"""
    st.markdown("### Posição Consolidada - Outubro 2025")
    st.info("📅 **Última atualização:** 04/10/2025")

    # Dados atualizados
    dados_gateways = [
        {
            'Gateway': 'Asaas',
            'Em Conta': 199242.36,
            'A Receber': 180404.30,
            'Total': 199242.36 + 180404.30,
            'Status': '🟢 Ativo',
            'Cor': '#10b981'
        },
        {
            'Gateway': 'Pagar.me',
            'Em Conta': 121974.33,
            'A Receber': 5182.26,
            'Total': 121974.33 + 5182.26,
            'Status': '🟢 Ativo',
            'Cor': '#3b82f6'
        },
        {
            'Gateway': 'Stripe',
            'Em Conta': 11992.00,
            'A Receber': 0.00,
            'Total': 11992.00,
            'Status': '🔵 Internacional',
            'Cor': '#8b5cf6'
        },
        {
            'Gateway': 'Cripto',
            'Em Conta': 31699.20,
            'A Receber': 0.00,
            'Total': 31699.20,
            'Status': '🟡 Cripto',
            'Cor': '#f59e0b'
        },
        {
            'Gateway': 'B2B Corporativo',
            'Em Conta': 0.00,
            'A Receber': 115000.00,
            'Total': 115000.00,
            'Status': '⏳ Aguardando',
            'Cor': '#ef4444'
        }
    ]

    # Calcula totais
    total_em_conta = sum([d['Em Conta'] for d in dados_gateways])
    total_a_receber = sum([d['A Receber'] for d in dados_gateways])
    total_geral = total_em_conta + total_a_receber

    # ==================== CARDS DE RESUMO ====================
    st.markdown("---")
    st.markdown("## 💵 Resumo Consolidado")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(f"""
        <div style="
            background: linear-gradient(135deg, #10b981 0%, #059669 100%);
            color: white; padding: 30px; border-radius: 12px; text-align: center;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        ">
            <div style="font-size: 0.875rem; opacity: 0.9; margin-bottom: 8px;">💰 EM CONTA</div>
            <div style="font-size: 2rem; font-weight: bold;">{formatar_moeda_br(total_em_conta)}</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div style="
            background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%);
            color: white; padding: 30px; border-radius: 12px; text-align: center;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        ">
            <div style="font-size: 0.875rem; opacity: 0.9; margin-bottom: 8px;">⏳ A RECEBER</div>
            <div style="font-size: 2rem; font-weight: bold;">{formatar_moeda_br(total_a_receber)}</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
        <div style="
            background: linear-gradient(135deg, #6366f1 0%, #4f46e5 100%);
            color: white; padding: 30px; border-radius: 12px; text-align: center;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        ">
            <div style="font-size: 0.875rem; opacity: 0.9; margin-bottom: 8px;">📊 TOTAL</div>
            <div style="font-size: 2rem; font-weight: bold;">{formatar_moeda_br(total_geral)}</div>
        </div>
        """, unsafe_allow_html=True)

    # ==================== DETALHAMENTO POR GATEWAY ====================
    st.markdown("---")
    st.markdown("## 🏦 Detalhamento por Gateway")

    for gateway in dados_gateways:
        st.markdown(f"""
        <div style="
            background: linear-gradient(145deg, #ffffff 0%, #f8fafc 100%);
            border: 1px solid #e5e7eb;
            border-left: 4px solid {gateway['Cor']};
            border-radius: 12px;
            padding: 20px;
            margin-bottom: 15px;
        ">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 15px;">
                <div>
                    <div style="font-size: 1.25rem; font-weight: bold; color: #111827;">
                        {gateway['Gateway']}
                    </div>
                    <div style="font-size: 0.875rem; color: #6b7280; margin-top: 4px;">
                        {gateway['Status']}
                    </div>
                </div>
                <div style="text-align: right;">
                    <div style="font-size: 0.875rem; color: #6b7280;">Total Disponível</div>
                    <div style="font-size: 1.5rem; font-weight: bold; color: {gateway['Cor']};">
                        {formatar_moeda_br(gateway['Total'])}
                    </div>
                </div>
            </div>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; margin-top: 15px;">
                <div style="background: #f9fafb; padding: 15px; border-radius: 8px;">
                    <div style="font-size: 0.75rem; color: #6b7280; text-transform: uppercase; margin-bottom: 5px;">
                        💰 Em Conta
                    </div>
                    <div style="font-size: 1.25rem; font-weight: bold; color: #10b981;">
                        {formatar_moeda_br(gateway['Em Conta'])}
                    </div>
                </div>
                <div style="background: #f9fafb; padding: 15px; border-radius: 8px;">
                    <div style="font-size: 0.75rem; color: #6b7280; text-transform: uppercase; margin-bottom: 5px;">
                        ⏳ A Receber
                    </div>
                    <div style="font-size: 1.25rem; font-weight: bold; color: #f59e0b;">
                        {formatar_moeda_br(gateway['A Receber'])}
                    </div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # ==================== DISTRIBUIÇÃO ====================
    st.markdown("---")
    st.markdown("## 📊 Distribuição dos Recursos")

    # Tabela resumida
    df_tabela = pd.DataFrame(dados_gateways)
    df_tabela_display = df_tabela[['Gateway', 'Em Conta', 'A Receber', 'Total', 'Status']].copy()

    # Formata valores
    df_tabela_display['Em Conta'] = df_tabela_display['Em Conta'].apply(formatar_moeda_br)
    df_tabela_display['A Receber'] = df_tabela_display['A Receber'].apply(formatar_moeda_br)
    df_tabela_display['Total'] = df_tabela_display['Total'].apply(formatar_moeda_br)

    st.dataframe(
        df_tabela_display,
        use_container_width=True,
        hide_index=True
    )

    # Observações
    st.markdown("---")
    st.markdown("### 📝 Observações")

    col1, col2 = st.columns(2)

    with col1:
        st.info("""
        **🟢 Liquidez Imediata:**
        - Total em conta: R$ 364.907,89
        - Disponível para uso imediato
        """)

    with col2:
        st.warning("""
        **⏳ A Receber:**
        - Total a receber: R$ 300.586,56
        - Principais: B2B (R$ 115.000) e Asaas (R$ 180.404)
        """)

def tab_analise_temporal():
    """Tab de análise temporal"""
    st.markdown("### 📈 Análise Temporal do Fluxo de Caixa")

    st.info("🔄 **Funcionalidade em desenvolvimento** - Será implementada com histórico de movimentações")

    st.markdown("""
    **Esta seção incluirá:**
    - 📊 Gráfico de evolução do saldo ao longo do tempo
    - 💹 Análise de entradas e saídas mensais
    - 📉 Tendências e padrões de fluxo
    - 🔍 Filtros por período e gateway
    """)

def tab_projecoes():
    """Tab de projeções"""
    st.markdown("### 🔮 Projeções de Fluxo de Caixa")

    st.info("📅 **Projeção para próximos 90 dias**")

    # Dados de projeção simples
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #10b981 0%, #059669 100%);
                    color: white; padding: 20px; border-radius: 12px; text-align: center;">
            <div style="font-size: 0.875rem; opacity: 0.9; margin-bottom: 8px;">30 DIAS</div>
            <div style="font-size: 1.5rem; font-weight: bold;">R$ 550.000</div>
            <div style="font-size: 0.75rem; opacity: 0.8; margin-top: 5px;">Projeção conservadora</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #6366f1 0%, #4f46e5 100%);
                    color: white; padding: 20px; border-radius: 12px; text-align: center;">
            <div style="font-size: 0.875rem; opacity: 0.9; margin-bottom: 8px;">60 DIAS</div>
            <div style="font-size: 1.5rem; font-weight: bold;">R$ 700.000</div>
            <div style="font-size: 0.75rem; opacity: 0.8; margin-top: 5px;">Baseado em histórico</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #8b5cf6 0%, #7c3aed 100%);
                    color: white; padding: 20px; border-radius: 12px; text-align: center;">
            <div style="font-size: 0.875rem; opacity: 0.9; margin-bottom: 8px;">90 DIAS</div>
            <div style="font-size: 1.5rem; font-weight: bold;">R$ 850.000</div>
            <div style="font-size: 0.75rem; opacity: 0.8; margin-top: 5px;">Com novos contratos</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("#### 📋 Premissas da Projeção")
    st.markdown("""
    - **Recebíveis atuais:** R$ 300.586,56 (confirmados)
    - **B2B pipeline:** R$ 115.000,00 (30-60 dias)
    - **Receita recorrente estimada:** R$ 250.000/mês
    - **Taxa de conversão:** 85%
    - **Crescimento mensal:** 10-15%
    """)

    st.warning("""
    ⚠️ **Nota:** Projeções são estimativas baseadas em dados históricos e podem variar
    conforme sazonalidade, novos contratos e condições de mercado.
    """)

def main_fluxo_caixa():
    """Módulo principal de fluxo de caixa"""

    st.title("💰 Fluxo de Caixa")

    # Cria as 3 tabs
    tab1, tab2, tab3 = st.tabs(["📊 Resumo", "📈 Análise Temporal", "🔮 Projeções"])

    with tab1:
        tab_resumo()

    with tab2:
        tab_analise_temporal()

    with tab3:
        tab_projecoes()

if __name__ == "__main__":
    main_fluxo_caixa()
