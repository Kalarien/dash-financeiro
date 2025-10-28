#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AUXILIAR DE ATUALIZAÇÃO MENSAL
Script para ajudar a identificar onde atualizar os dados mensais
"""

import os

def mostrar_locais_atualizacao():
    """Mostra todos os locais que precisam ser atualizados"""

    print("=" * 80)
    print("📋 GUIA DE ATUALIZAÇÃO MENSAL DO DASHBOARD")
    print("=" * 80)
    print()

    print("📁 Arquivos que você precisa editar:")
    print()

    # Verificar se os arquivos existem
    arquivos = [
        "modulo_fechamento_mes.py",
        "modulo_fluxo_caixa.py",
        "modulo_faturamento_tempo_real.py"
    ]

    for arquivo in arquivos:
        if os.path.exists(arquivo):
            print(f"  ✅ {arquivo}")
        else:
            print(f"  ❌ {arquivo} - ARQUIVO NÃO ENCONTRADO!")

    print()
    print("=" * 80)
    print("📄 ARQUIVO 1: modulo_fechamento_mes.py")
    print("=" * 80)
    print()

    print("🔍 LOCAIS PARA ATUALIZAR:")
    print()

    print("1️⃣ LINHA 53: Mês e Ano no Título")
    print("   Atual: st.markdown(\"### Análise Completa - Setembro 2025\")")
    print("   Mudar para: st.markdown(\"### Análise Completa - OUTUBRO 2025\")")
    print()

    print("2️⃣ LINHA 56: Data de Atualização")
    print("   Atual: st.info(\"📅 **Última atualização:** 04/10/2025 | **Período:** Setembro 2025 (mês completo)\")")
    print("   Mudar para: st.info(\"📅 **Última atualização:** [DATA_HOJE] | **Período:** Outubro 2025 (mês completo)\")")
    print()

    print("3️⃣ LINHAS 67-96: Métricas de Faturamento (4 cards)")
    print("   - Faturamento Total")
    print("   - Faturamento B2B")
    print("   - Faturamento B2C")
    print("   - Taxa Média B2C")
    print()

    print("4️⃣ LINHAS 101-138: Tabela de Faturamento por Adquirente")
    print("   df_faturamento = pd.DataFrame([")
    print("       {'Adquirente': 'B2B Corporativo', 'Faturamento': XXX, ...},")
    print("       {'Adquirente': 'Pagar.me', 'Faturamento': XXX, ...},")
    print("       {'Adquirente': 'Stripe', 'Faturamento': XXX, ...},")
    print("       {'Adquirente': 'Crypto', 'Faturamento': XXX, ...}")
    print("   ])")
    print()

    print("5️⃣ LINHAS 167-196: Métricas de Caixa (4 cards)")
    print("   - Total Bruto Recebido")
    print("   - Total de Taxas Pagas")
    print("   - Valor Líquido")
    print("   - Antecipações")
    print()

    print("6️⃣ LINHAS 201-246: Tabela de Caixa por Adquirente")
    print("   df_caixa = pd.DataFrame([")
    print("       {'Adquirente': 'Asaas', 'Valor Bruto': XXX, ...},")
    print("       {'Adquirente': 'Pagar.me', 'Valor Bruto': XXX, ...},")
    print("       ...")
    print("   ])")
    print()

    print("7️⃣ LINHAS 267-315: Comparativo Faturamento vs Caixa")
    print("   df_comparativo = pd.DataFrame([...])")
    print()

    print("8️⃣ LINHAS 321-353: Resumo Executivo (4 cards grandes)")
    print()

    print("=" * 80)
    print("📄 ARQUIVO 2: modulo_fluxo_caixa.py")
    print("=" * 80)
    print()

    print("1️⃣ LINHA 19: Mês no Título")
    print("   Atual: st.markdown(\"### Posição Consolidada - Outubro 2025\")")
    print("   Mudar para: st.markdown(\"### Posição Consolidada - NOVEMBRO 2025\")")
    print()

    print("2️⃣ LINHA 20: Data de Atualização")
    print("   Atual: st.info(\"📅 **Última atualização:** 04/10/2025\")")
    print("   Mudar para: st.info(\"📅 **Última atualização:** [DATA_HOJE]\")")
    print()

    print("3️⃣ LINHAS 23-64: Dados dos Gateways")
    print("   dados_gateways = [")
    print("       {")
    print("           'Gateway': 'Asaas',")
    print("           'Em Conta': 199242.36,  ← ATUALIZAR")
    print("           'A Receber': 180404.30,  ← ATUALIZAR")
    print("           ...")
    print("       },")
    print("       ... (5 gateways no total)")
    print("   ]")
    print()

    print("=" * 80)
    print("📄 ARQUIVO 3: modulo_faturamento_tempo_real.py")
    print("=" * 80)
    print()
    print("   ⚠️ Verifique este arquivo para ver se há dados hardcoded")
    print()

    print("=" * 80)
    print("🎯 PRÓXIMOS PASSOS")
    print("=" * 80)
    print()
    print("1. Abra cada arquivo em um editor de texto")
    print("2. Use Ctrl+G para ir para a linha específica")
    print("3. Atualize os valores com os dados do novo mês")
    print("4. Salve os arquivos")
    print("5. Teste localmente: streamlit run app.py")
    print("6. Commit e push para o GitHub")
    print()

    print("=" * 80)
    print("💡 DICA: Use o CHECKLIST_ATUALIZACAO.md para não esquecer nada!")
    print("=" * 80)
    print()

def verificar_dados_atuais():
    """Mostra os dados atuais dos arquivos"""

    print("=" * 80)
    print("📊 DADOS ATUAIS NO SISTEMA")
    print("=" * 80)
    print()

    # Ler modulo_fechamento_mes.py
    try:
        with open("modulo_fechamento_mes.py", "r", encoding="utf-8") as f:
            conteudo = f.read()

            # Buscar mês atual
            if "Setembro 2025" in conteudo:
                print("📅 Mês atual no fechamento: SETEMBRO 2025")
            elif "Outubro 2025" in conteudo:
                print("📅 Mês atual no fechamento: OUTUBRO 2025")
            else:
                print("📅 Mês atual no fechamento: NÃO IDENTIFICADO")

            # Buscar faturamento total
            import re
            match = re.search(r'"Faturamento Total",\s*"R\$ ([\d.,]+)"', conteudo)
            if match:
                print(f"💰 Faturamento Total: R$ {match.group(1)}")

            print()
    except FileNotFoundError:
        print("❌ modulo_fechamento_mes.py não encontrado!")
        print()

    # Ler modulo_fluxo_caixa.py
    try:
        with open("modulo_fluxo_caixa.py", "r", encoding="utf-8") as f:
            conteudo = f.read()

            # Buscar mês atual
            if "Outubro 2025" in conteudo:
                print("📅 Mês atual no fluxo: OUTUBRO 2025")
            elif "Novembro 2025" in conteudo:
                print("📅 Mês atual no fluxo: NOVEMBRO 2025")
            else:
                print("📅 Mês atual no fluxo: NÃO IDENTIFICADO")

            # Buscar saldo Asaas
            import re
            match = re.search(r"'Gateway': 'Asaas',.*?'Em Conta': ([\d.]+),", conteudo, re.DOTALL)
            if match:
                print(f"💳 Asaas em conta: R$ {float(match.group(1)):,.2f}")

            print()
    except FileNotFoundError:
        print("❌ modulo_fluxo_caixa.py não encontrado!")
        print()

    print("=" * 80)
    print()

def main():
    """Função principal"""

    print()
    print("🤖 AUXILIAR DE ATUALIZAÇÃO MENSAL")
    print()

    while True:
        print("Escolha uma opção:")
        print()
        print("1. Ver guia de atualização (onde atualizar)")
        print("2. Ver dados atuais do sistema")
        print("3. Sair")
        print()

        escolha = input("Digite o número da opção: ").strip()

        if escolha == "1":
            print()
            mostrar_locais_atualizacao()
            input("\nPressione ENTER para continuar...")
            print()
        elif escolha == "2":
            print()
            verificar_dados_atuais()
            input("\nPressione ENTER para continuar...")
            print()
        elif escolha == "3":
            print()
            print("👋 Até logo!")
            print()
            break
        else:
            print()
            print("❌ Opção inválida!")
            print()

if __name__ == "__main__":
    main()
