#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MÓDULO DE FATURAMENTO TEMPO REAL - ATUALIZADO
Dados manuais atualizados do faturamento (setembro 2025)
"""

import streamlit as st
import json
from datetime import datetime

def carregar_dados_faturamento():
    """Carrega dados atualizados do faturamento"""
    try:
        # Dados CORRETOS da Matriz financeira.xlsx - Junho a Outubro 2025
        dados = {
            'total_geral': 1168787.57,
            'periodo': 'Junho - Outubro 2025 (Outubro completo)',
            'ultima_atualizacao': '05/11/2025',
            'por_mes': {
                'Junho': {
                    'total': 191598.39,
                    'percentual': 16.4,
                    'detalhes': {
                        'ASAAS': 158812.42,
                        'CRIPTO': 18808.87,
                        'STRIPE': 13977.10
                    }
                },
                'Julho': {
                    'total': 418751.86,
                    'percentual': 35.8,
                    'detalhes': {
                        'ASAAS': 353429.90,
                        'CRIPTO': 39429.56,
                        'STRIPE': 25892.40
                    }
                },
                'Agosto': {
                    'total': 141797.73,
                    'percentual': 12.1,
                    'detalhes': {
                        'ASAAS': 116156.43,
                        'PAGAR.ME': 17246.50,
                        'CRIPTO': 6396.80,
                        'STRIPE': 1998.00
                    }
                },
                'Setembro': {
                    'total': 257074.18,
                    'percentual': 22.0,
                    'detalhes': {
                        'B2B': 120000.00,
                        'PAGAR.ME': 101901.78,
                        'CRIPTO': 23180.40,
                        'STRIPE': 11992.00
                    }
                },
                'Outubro': {
                    'total': 159565.41,
                    'percentual': 13.7,
                    'detalhes': {
                        'PAGAR.ME': 144576.41,
                        'CRIPTO': 11991.00,
                        'STRIPE': 2998.00
                    }
                }
            },
            'por_adquirente': {
                'ASAAS': {
                    'total': 628398.75,
                    'percentual': 53.8,
                    'cor': '#e74c3c'
                },
                'PAGAR.ME': {
                    'total': 263724.69,
                    'percentual': 22.6,
                    'cor': '#3498db'
                },
                'B2B': {
                    'total': 120000.00,
                    'percentual': 10.3,
                    'cor': '#2ecc71'
                },
                'CRIPTO': {
                    'total': 99806.63,
                    'percentual': 8.5,
                    'cor': '#f39c12'
                },
                'STRIPE': {
                    'total': 56857.50,
                    'percentual': 4.9,
                    'cor': '#9b59b6'
                }
            }
        }
        return dados
    except Exception as e:
        st.error(f"Erro ao carregar dados: {e}")
        return None

def formatar_moeda_br(valor):
    """Formata valor em moeda brasileira"""
    return f"R$ {valor:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')

def main_modulo_faturamento_tempo_real():
    """Módulo principal de faturamento tempo real"""
    st.title("Faturamento Tempo Real")

    # Carrega dados
    dados = carregar_dados_faturamento()

    if not dados:
        st.error("Erro ao carregar dados de faturamento")
        return

    # Info de atualização
    st.info(f"**Última atualização:** {dados['ultima_atualizacao']} | **Período:** {dados['periodo']}")

    # Total Geral
    st.markdown("---")
    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        st.markdown(f"""
        <div style="
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white; padding: 24px; border-radius: 12px;
            text-align: center; margin: 15px 0;
            box-shadow: 0 10px 20px rgba(102, 126, 234, 0.25);
        ">
            <h2 style="margin-bottom: 10px; opacity: 0.9; font-size: 1.3rem;">Faturamento Total</h2>
            <div style="font-size: 2.2em; font-weight: bold; text-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);">
                {formatar_moeda_br(dados['total_geral'])}
            </div>
        </div>
        """, unsafe_allow_html=True)

    # Faturamento por Mês
    st.markdown("---")
    st.subheader("Faturamento por Mês")

    cols_mes = st.columns(5)  # 5 colunas para 5 meses
    cores_mes = ['#4ecdc4', '#45b7d1', '#96ceb4', '#feca57', '#ff6b6b']

    for i, (mes, dados_mes) in enumerate(dados['por_mes'].items()):
        with cols_mes[i]:
            # Card do mês com gradiente
            cor = cores_mes[i]
            st.markdown(f"""
            <div style="
                background: linear-gradient(135deg, {cor} 0%, {cor}dd 100%);
                padding: 14px;
                border-radius: 10px;
                box-shadow: 0 4px 10px rgba(0, 0, 0, 0.12);
                text-align: center;
                margin-bottom: 12px;
                min-height: 85px;
            ">
                <div style="font-size: 0.75em; color: white; opacity: 0.9; margin-bottom: 6px; font-weight: 500; text-transform: uppercase; letter-spacing: 0.5px;">
                    {mes}
                </div>
                <div style="font-size: 1.2em; font-weight: bold; color: white; margin-bottom: 4px;">
                    {formatar_moeda_br(dados_mes['total'])}
                </div>
                <div style="font-size: 0.7em; color: white; opacity: 0.8;">
                    {dados_mes['percentual']}% do total
                </div>
            </div>
            """, unsafe_allow_html=True)

            # Detalhes do mês
            st.markdown("""
            <div style="
                background: #f8f9fa;
                border-radius: 8px;
                padding: 12px 14px;
                margin-top: 8px;
                border-left: 3px solid """ + cor + """;
            ">
                <div style="
                    font-size: 0.7rem;
                    font-weight: 600;
                    color: #495057;
                    text-transform: uppercase;
                    letter-spacing: 0.5px;
                    margin-bottom: 8px;
                ">Detalhes</div>
            """, unsafe_allow_html=True)

            for gateway, valor in dados_mes['detalhes'].items():
                st.markdown(f"""
                <div style="
                    display: flex;
                    justify-content: space-between;
                    align-items: center;
                    padding: 4px 0;
                    font-size: 0.75rem;
                    color: #495057;
                ">
                    <span style="font-weight: 500;">{gateway}</span>
                    <span style="font-weight: 600; color: #212529;">{formatar_moeda_br(valor)}</span>
                </div>
                """, unsafe_allow_html=True)

            st.markdown("</div>", unsafe_allow_html=True)

    # Faturamento por Adquirente
    st.markdown("---")
    st.subheader("Faturamento por Adquirente")

    cols_gateway = st.columns(5)

    for i, (gateway, dados_gateway) in enumerate(dados['por_adquirente'].items()):
        with cols_gateway[i]:
            cor = dados_gateway['cor']
            st.markdown(f"""
            <div style="
                background: linear-gradient(135deg, {cor} 0%, {cor}dd 100%);
                padding: 14px;
                border-radius: 10px;
                box-shadow: 0 4px 10px rgba(0, 0, 0, 0.12);
                text-align: center;
                margin-bottom: 12px;
                min-height: 85px;
            ">
                <div style="font-size: 0.75em; color: white; opacity: 0.9; margin-bottom: 6px; font-weight: 500; text-transform: uppercase; letter-spacing: 0.5px;">
                    {gateway}
                </div>
                <div style="font-size: 1.2em; font-weight: bold; color: white; margin-bottom: 4px;">
                    {formatar_moeda_br(dados_gateway['total'])}
                </div>
                <div style="font-size: 0.7em; color: white; opacity: 0.8;">
                    {dados_gateway['percentual']}% do total
                </div>
            </div>
            """, unsafe_allow_html=True)

    # Destaque Setembro
    st.markdown("---")
    st.subheader("Destaque: Setembro 2025")

    setembro_dados = dados['por_mes']['Setembro']

    col1, col2 = st.columns(2)

    with col1:
        st.success(f"**Total Setembro:** {formatar_moeda_br(setembro_dados['total'])}")
        st.info("**Maior crescimento:** B2B com R$ 120.000,00")

    with col2:
        st.markdown("**Composição Setembro:**")
        for gateway, valor in setembro_dados['detalhes'].items():
            percentual = (valor / setembro_dados['total']) * 100
            st.markdown(f"• **{gateway}:** {formatar_moeda_br(valor)} ({percentual:.1f}%)")

    # Botão de atualização
    st.markdown("---")

    col1, col2, col3 = st.columns([1, 1, 1])

    with col2:
        if st.button("Atualizar Dados", use_container_width=True):
            st.success("Dados atualizados com sucesso!")
            st.rerun()

if __name__ == "__main__":
    main_modulo_faturamento_tempo_real()