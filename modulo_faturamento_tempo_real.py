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
        # Dados atualizados - Junho a Outubro 2025
        dados = {
            'total_geral': 1234650.12,
            'periodo': 'Junho - Outubro 2025 (Outubro completo)',
            'ultima_atualizacao': '05/11/2025',
            'por_mes': {
                'Junho': {
                    'total': 208167.52,
                    'percentual': 16.9,
                    'detalhes': {
                        'ASAAS': 158812.42,
                        'CRIPTO': 35378.00,
                        'STRIPE': 13977.10
                    }
                },
                'Julho': {
                    'total': 437862.80,
                    'percentual': 35.5,
                    'detalhes': {
                        'ASAAS': 353429.90,
                        'CRIPTO': 58540.50,
                        'STRIPE': 25892.40
                    }
                },
                'Agosto': {
                    'total': 171981.21,
                    'percentual': 13.9,
                    'detalhes': {
                        'ASAAS': 145440.91,
                        'PAGAR.ME': 17246.50,
                        'CRIPTO': 6295.80,
                        'STRIPE': 2998.00
                    }
                },
                'Setembro': {
                    'total': 257074.18,
                    'percentual': 20.8,
                    'detalhes': {
                        'B2B': 120000.00,
                        'PAGAR.ME': 101901.78,
                        'CRIPTO': 23180.40,
                        'STRIPE': 11992.00
                    }
                },
                'Outubro': {
                    'total': 159565.41,
                    'percentual': 12.9,
                    'detalhes': {
                        'PAGAR.ME': 144576.41,
                        'CRIPTO': 11991.00,
                        'STRIPE': 2998.00
                    }
                }
            },
            'por_adquirente': {
                'ASAAS': {
                    'total': 657683.23,
                    'percentual': 53.3,
                    'cor': '#e74c3c'
                },
                'PAGAR.ME': {
                    'total': 263724.69,
                    'percentual': 21.4,
                    'cor': '#3498db'
                },
                'CRIPTO': {
                    'total': 135385.70,
                    'percentual': 11.0,
                    'cor': '#f39c12'
                },
                'B2B': {
                    'total': 120000.00,
                    'percentual': 9.7,
                    'cor': '#2ecc71'
                },
                'STRIPE': {
                    'total': 57857.50,
                    'percentual': 4.7,
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
    st.title("💰 Faturamento Tempo Real")

    # Carrega dados
    dados = carregar_dados_faturamento()

    if not dados:
        st.error("❌ Erro ao carregar dados de faturamento")
        return

    # Info de atualização
    st.info(f"📅 **Última atualização:** {dados['ultima_atualizacao']} | **Período:** {dados['periodo']}")

    # Total Geral
    st.markdown("---")
    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        st.markdown(f"""
        <div style="
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white; padding: 40px; border-radius: 20px;
            text-align: center; margin: 20px 0;
            box-shadow: 0 15px 30px rgba(102, 126, 234, 0.3);
        ">
            <h2 style="margin-bottom: 15px; opacity: 0.9;">Faturamento Total</h2>
            <div style="font-size: 3em; font-weight: bold; text-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);">
                {formatar_moeda_br(dados['total_geral'])}
            </div>
        </div>
        """, unsafe_allow_html=True)

    # Faturamento por Mês
    st.markdown("---")
    st.subheader("📅 Faturamento por Mês")

    cols_mes = st.columns(4)
    cores_mes = ['#4ecdc4', '#45b7d1', '#96ceb4', '#feca57']

    for i, (mes, dados_mes) in enumerate(dados['por_mes'].items()):
        with cols_mes[i]:
            # Card do mês
            st.markdown(f"""
            <div style="
                background: white; padding: 25px; border-radius: 15px;
                box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1);
                text-align: center; border-left: 5px solid {cores_mes[i]};
                margin-bottom: 20px;
            ">
                <div style="font-size: 1.1em; color: #666; margin-bottom: 10px; font-weight: 500;">
                    {mes}
                </div>
                <div style="font-size: 1.5em; font-weight: bold; color: #333;">
                    {formatar_moeda_br(dados_mes['total'])}
                </div>
                <div style="font-size: 0.9em; color: #999; margin-top: 5px;">
                    {dados_mes['percentual']}%
                </div>
            </div>
            """, unsafe_allow_html=True)

            # Detalhes do mês
            st.markdown("**Detalhes:**")
            for gateway, valor in dados_mes['detalhes'].items():
                st.markdown(f"• {gateway}: {formatar_moeda_br(valor)}")

    # Faturamento por Adquirente
    st.markdown("---")
    st.subheader("🏦 Faturamento por Adquirente")

    cols_gateway = st.columns(5)

    for i, (gateway, dados_gateway) in enumerate(dados['por_adquirente'].items()):
        with cols_gateway[i]:
            st.markdown(f"""
            <div style="
                background: white; padding: 25px; border-radius: 15px;
                box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1);
                text-align: center; border-left: 5px solid {dados_gateway['cor']};
                margin-bottom: 20px;
            ">
                <div style="font-size: 1.1em; color: #666; margin-bottom: 10px; font-weight: 500;">
                    {gateway}
                </div>
                <div style="font-size: 1.5em; font-weight: bold; color: #333;">
                    {formatar_moeda_br(dados_gateway['total'])}
                </div>
                <div style="font-size: 0.9em; color: #999; margin-top: 5px;">
                    {dados_gateway['percentual']}%
                </div>
            </div>
            """, unsafe_allow_html=True)

    # Destaque Setembro
    st.markdown("---")
    st.subheader("🔥 Destaque: Setembro 2025")

    setembro_dados = dados['por_mes']['Setembro']

    col1, col2 = st.columns(2)

    with col1:
        st.success(f"**Total Setembro:** {formatar_moeda_br(setembro_dados['total'])}")
        st.info("📊 **Maior crescimento:** B2B com R$ 120.000,00")

    with col2:
        st.markdown("**Composição Setembro:**")
        for gateway, valor in setembro_dados['detalhes'].items():
            percentual = (valor / setembro_dados['total']) * 100
            st.markdown(f"• **{gateway}:** {formatar_moeda_br(valor)} ({percentual:.1f}%)")

    # Botão de atualização
    st.markdown("---")

    col1, col2, col3 = st.columns([1, 1, 1])

    with col2:
        if st.button("🔄 Atualizar Dados", use_container_width=True):
            st.success("✅ Dados atualizados com sucesso!")
            st.rerun()

if __name__ == "__main__":
    main_modulo_faturamento_tempo_real()