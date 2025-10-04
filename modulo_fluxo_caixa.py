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
    """Tab de projeções baseadas na Matriz Financeira"""
    from datetime import datetime

    st.markdown("### 🔮 Projeções de Fluxo de Caixa")

    try:
        # Carrega a Matriz Financeira
        df_matriz = pd.read_excel('Matriz financeira.xlsx', sheet_name='Matriz Detalhada')

        # Identifica colunas de data (outubro, novembro, dezembro)
        colunas_data = []
        for col in df_matriz.columns:
            if isinstance(col, datetime):
                if col.year == 2025 and col.month >= 10:
                    colunas_data.append(col)

        # Pega outubro, novembro, dezembro
        meses_projecao = sorted(colunas_data)[:3]

        # Extrai dados da matriz
        linha_receitas = df_matriz[df_matriz['Categoria'] == 'TOTAL RECEITAS']
        linha_custos = df_matriz[df_matriz['Categoria'] == 'TOTAL CUSTOS']
        linha_despesas = df_matriz[df_matriz['Categoria'] == 'TOTAL DESPESAS']
        linha_resultado = df_matriz[df_matriz['Categoria'] == 'RESULTADO LÍQUIDO']

        # Saldo inicial (em conta + a receber)
        saldo_inicial = 364907.89 + 300586.56  # Total atual

        # Calcula projeção acumulada
        projecoes = []
        saldo_acumulado = saldo_inicial

        for mes in meses_projecao:
            receita = linha_receitas[mes].iloc[0] if not linha_receitas.empty and pd.notna(linha_receitas[mes].iloc[0]) else 0
            custo = linha_custos[mes].iloc[0] if not linha_custos.empty and pd.notna(linha_custos[mes].iloc[0]) else 0
            despesa = linha_despesas[mes].iloc[0] if not linha_despesas.empty and pd.notna(linha_despesas[mes].iloc[0]) else 0
            resultado = receita - custo - despesa

            saldo_acumulado += resultado

            projecoes.append({
                'mes': mes,
                'mes_nome': mes.strftime('%B/%Y'),
                'receita': receita,
                'custo': custo,
                'despesa': despesa,
                'resultado': resultado,
                'saldo_projetado': saldo_acumulado
            })

        # Cards de projeção
        st.info(f"📅 **Saldo inicial:** {formatar_moeda_br(saldo_inicial)} (Em conta + A receber)")

        cols = st.columns(3)
        cores = ['#10b981', '#6366f1', '#8b5cf6']

        for idx, proj in enumerate(projecoes):
            with cols[idx]:
                st.markdown(f"""
                <div style="background: linear-gradient(135deg, {cores[idx]} 0%, {cores[idx]}dd 100%);
                            color: white; padding: 20px; border-radius: 12px; text-align: center;">
                    <div style="font-size: 0.875rem; opacity: 0.9; margin-bottom: 8px;">{proj['mes_nome'].upper()}</div>
                    <div style="font-size: 1.5rem; font-weight: bold;">{formatar_moeda_br(proj['saldo_projetado'])}</div>
                    <div style="font-size: 0.75rem; opacity: 0.8; margin-top: 5px;">
                        {'+' if proj['resultado'] >= 0 else ''}{formatar_moeda_br(proj['resultado'])} no mês
                    </div>
                </div>
                """, unsafe_allow_html=True)

        # Tabela detalhada
        st.markdown("---")
        st.markdown("#### 📊 Detalhamento Mensal")

        df_projecao = pd.DataFrame(projecoes)
        df_display = df_projecao[['mes_nome', 'receita', 'custo', 'despesa', 'resultado', 'saldo_projetado']].copy()
        df_display.columns = ['Mês', 'Receitas', 'Custos', 'Despesas', 'Resultado', 'Saldo Projetado']

        # Formata valores
        for col in ['Receitas', 'Custos', 'Despesas', 'Resultado', 'Saldo Projetado']:
            df_display[col] = df_display[col].apply(formatar_moeda_br)

        st.dataframe(df_display, use_container_width=True, hide_index=True)

        # Gráficos
        st.markdown("---")
        st.markdown("#### 📈 Visualização do Crescimento")

        import plotly.graph_objects as go
        from plotly.subplots import make_subplots

        # Gráfico 1: Evolução do Saldo
        fig_saldo = go.Figure()

        fig_saldo.add_trace(go.Scatter(
            x=[p['mes_nome'] for p in projecoes],
            y=[saldo_inicial] + [p['saldo_projetado'] for p in projecoes[:-1]],
            mode='lines+markers',
            name='Saldo Inicial',
            line=dict(color='#94a3b8', width=2, dash='dash'),
            marker=dict(size=8)
        ))

        fig_saldo.add_trace(go.Scatter(
            x=[p['mes_nome'] for p in projecoes],
            y=[p['saldo_projetado'] for p in projecoes],
            mode='lines+markers',
            name='Saldo Projetado',
            line=dict(color='#10b981', width=3),
            marker=dict(size=10),
            fill='tonexty',
            fillcolor='rgba(16, 185, 129, 0.1)'
        ))

        fig_saldo.update_layout(
            title='Evolução do Saldo de Caixa',
            xaxis_title='Mês',
            yaxis_title='Saldo (R$)',
            hovermode='x unified',
            template='plotly_white',
            height=400
        )

        st.plotly_chart(fig_saldo, use_container_width=True)

        # Gráfico 2: Receitas vs Despesas
        fig_receitas = go.Figure()

        fig_receitas.add_trace(go.Bar(
            name='Receitas',
            x=[p['mes_nome'] for p in projecoes],
            y=[p['receita'] for p in projecoes],
            marker_color='#10b981'
        ))

        fig_receitas.add_trace(go.Bar(
            name='Custos',
            x=[p['mes_nome'] for p in projecoes],
            y=[p['custo'] for p in projecoes],
            marker_color='#f59e0b'
        ))

        fig_receitas.add_trace(go.Bar(
            name='Despesas',
            x=[p['mes_nome'] for p in projecoes],
            y=[p['despesa'] for p in projecoes],
            marker_color='#ef4444'
        ))

        fig_receitas.update_layout(
            title='Receitas vs Custos vs Despesas',
            xaxis_title='Mês',
            yaxis_title='Valor (R$)',
            barmode='group',
            template='plotly_white',
            height=400
        )

        st.plotly_chart(fig_receitas, use_container_width=True)

        # Observações
        st.markdown("---")
        st.markdown("#### 📋 Premissas da Projeção")
        st.success("""
        ✅ **Projeção baseada em:**
        - Saldo atual em conta: R$ 364.907,89
        - Recebíveis confirmados: R$ 300.586,56
        - Receitas projetadas da Matriz Financeira
        - Custos e despesas planejados
        """)

        # Variação total
        variacao_total = projecoes[-1]['saldo_projetado'] - saldo_inicial
        cor_variacao = '#10b981' if variacao_total >= 0 else '#ef4444'

        st.markdown(f"""
        <div style="background: linear-gradient(135deg, {cor_variacao} 0%, {cor_variacao}dd 100%);
                    color: white; padding: 20px; border-radius: 12px; text-align: center; margin-top: 20px;">
            <div style="font-size: 0.875rem; opacity: 0.9; margin-bottom: 8px;">VARIAÇÃO TOTAL (3 MESES)</div>
            <div style="font-size: 2rem; font-weight: bold;">
                {'+' if variacao_total >= 0 else ''}{formatar_moeda_br(variacao_total)}
            </div>
        </div>
        """, unsafe_allow_html=True)

    except Exception as e:
        st.error(f"❌ Erro ao carregar projeções: {e}")
        st.info("Verifique se o arquivo Matriz financeira.xlsx está disponível")

def main_fluxo_caixa():
    """Módulo principal de fluxo de caixa"""

    st.title("💰 Fluxo de Caixa")

    # Cria 2 tabs (Análise Temporal oculta)
    tab1, tab2 = st.tabs(["📊 Resumo", "🔮 Projeções"])

    with tab1:
        tab_resumo()

    with tab2:
        tab_projecoes()

if __name__ == "__main__":
    main_fluxo_caixa()
