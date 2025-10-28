# 📋 TUTORIAL: Atualização Mensal do Dashboard - Do Notebook

**Repositório GitHub:** https://github.com/Kalarien/dash-financeiro.git
**Deploy Streamlit:** Atualiza automaticamente quando você faz push para o GitHub

---

## 🎯 VISÃO GERAL

Este tutorial ensina como atualizar os dados do dashboard financeiro **remotamente do seu notebook**, quando você estiver viajando. O processo é simples:

1. Clonar o repositório no notebook
2. Atualizar os dados nos arquivos Python
3. Fazer commit e push para o GitHub
4. Streamlit detecta automaticamente e atualiza o deploy

**⏱️ Tempo estimado:** 15-30 minutos

---

## 📦 ANTES DE COMEÇAR (Preparação do Notebook)

### 1. Instalar Git no Notebook (se não tiver)

**Windows:**
```bash
# Baixar e instalar Git de: https://git-scm.com/download/win
# Ou usar winget:
winget install --id Git.Git -e --source winget
```

**Mac:**
```bash
brew install git
```

**Linux:**
```bash
sudo apt-get install git
```

### 2. Configurar Git (PRIMEIRA VEZ APENAS)

```bash
git config --global user.name "Seu Nome"
git config --global user.email "seu-email@exemplo.com"
```

### 3. Ter Acesso ao GitHub

- Certifique-se de que tem acesso ao repositório: https://github.com/Kalarien/dash-financeiro
- Se usar autenticação por senha, use um **Personal Access Token** (não a senha normal)
  - Criar token: https://github.com/settings/tokens
  - Permissões necessárias: `repo` (acesso completo ao repositório)

---

## 🚀 PASSO A PASSO: ATUALIZAÇÃO MENSAL

### PASSO 1: Clonar o Repositório (PRIMEIRA VEZ APENAS)

No notebook, abra o terminal e execute:

```bash
# Navegue até onde quer salvar o projeto
cd C:\
# Ou no Mac/Linux:
cd ~

# Clone o repositório
git clone https://github.com/Kalarien/dash-financeiro.git

# Entre na pasta
cd dash-financeiro
```

**⚠️ IMPORTANTE:** Na primeira vez, o GitHub vai pedir suas credenciais:
- **Username:** seu username do GitHub
- **Password:** seu Personal Access Token (não a senha normal!)

---

### PASSO 2: Atualizar o Repositório Local

Se você já tem o repositório clonado, sempre atualize antes de fazer mudanças:

```bash
cd dash-financeiro
git pull origin main
```

---

### PASSO 3: Editar os Arquivos com Dados

Você precisa atualizar **3 arquivos Python** com os dados do novo mês:

#### 📄 Arquivo 1: `modulo_fechamento_mes.py`

**Linha 53:** Atualizar o mês e ano
```python
st.markdown("### Análise Completa - OUTUBRO 2025")  # Mudar para o mês atual
```

**Linha 56:** Atualizar data e período
```python
st.info("📅 **Última atualização:** 01/11/2025 | **Período:** Outubro 2025 (mês completo)")
```

**Linhas 67-96:** Atualizar métricas de faturamento
```python
with col1:
    st.markdown(criar_metrica_card(
        "Faturamento Total",
        "R$ XXX.XXX,XX",  # ← ATUALIZAR com faturamento de outubro
        "XX transações + B2B",  # ← ATUALIZAR número de transações
        "positive"
    ), unsafe_allow_html=True)

with col2:
    st.markdown(criar_metrica_card(
        "Faturamento B2B",
        "R$ XXX.XXX,XX",  # ← ATUALIZAR B2B de outubro
        "Vendas corporativas",
        "neutral"
    ), unsafe_allow_html=True)

# ... e assim por diante para col3 e col4
```

**Linhas 101-138:** Atualizar tabela de faturamento por adquirente
```python
df_faturamento = pd.DataFrame([
    {
        'Adquirente': 'B2B Corporativo',
        'Transações': '-',
        'Faturamento': 120000.00,  # ← ATUALIZAR valores
        '%': '46,7%',  # ← ATUALIZAR percentuais
        'Ticket Médio': '-',
        'Taxa': '-',
        'Status': '🟢 Empresarial'
    },
    # ... atualizar todos os adquirentes
])
```

**Linhas 167-196:** Atualizar métricas de caixa
**Linhas 201-246:** Atualizar tabela de caixa por adquirente
**Linhas 267-315:** Atualizar comparativo Faturamento vs Caixa
**Linhas 321-353:** Atualizar resumo executivo

---

#### 📄 Arquivo 2: `modulo_fluxo_caixa.py`

**Linha 19:** Atualizar mês no título
```python
st.markdown("### Posição Consolidada - NOVEMBRO 2025")  # Mês atual
```

**Linha 20:** Atualizar data
```python
st.info("📅 **Última atualização:** 01/11/2025")
```

**Linhas 23-64:** Atualizar dados dos gateways
```python
dados_gateways = [
    {
        'Gateway': 'Asaas',
        'Em Conta': 199242.36,  # ← ATUALIZAR saldo em conta
        'A Receber': 180404.30,  # ← ATUALIZAR valores a receber
        'Total': 199242.36 + 180404.30,
        'Status': '🟢 Ativo',
        'Cor': '#10b981'
    },
    # ... atualizar todos os gateways
]
```

**Linhas 192-200:** Atualizar observações (se necessário)

---

#### 📄 Arquivo 3: `modulo_faturamento_tempo_real.py`

Verifique se este arquivo também tem dados hardcoded que precisam ser atualizados.

---

### PASSO 4: Testar Localmente (RECOMENDADO)

Antes de fazer push, teste se está funcionando:

```bash
# Instalar dependências (primeira vez apenas)
pip install -r requirements.txt

# Rodar o dashboard localmente
streamlit run app.py
```

Acesse http://localhost:8501 e verifique:
- Login funciona
- Dados de outubro aparecem corretamente
- Fluxo de Caixa está atualizado
- Nenhum erro aparece

---

### PASSO 5: Fazer Commit das Mudanças

```bash
# Ver o que foi modificado
git status

# Adicionar os arquivos modificados
git add modulo_fechamento_mes.py modulo_fluxo_caixa.py modulo_faturamento_tempo_real.py

# Fazer commit com mensagem descritiva
git commit -m "Atualização dados financeiros - Outubro 2025"
```

---

### PASSO 6: Enviar para o GitHub (Push)

```bash
git push origin main
```

**⚠️ Se pedir credenciais:**
- **Username:** seu username do GitHub
- **Password:** seu Personal Access Token

---

### PASSO 7: Verificar Deploy Automático no Streamlit

1. Acesse: https://share.streamlit.io/
2. Faça login com sua conta Streamlit
3. Veja a lista de apps
4. Clique no seu dashboard
5. Na aba "Logs", você verá:
   ```
   Detecting changes...
   Restarting app...
   App is live!
   ```

**⏱️ Tempo de deploy:** 1-3 minutos após o push

---

## 🔍 ONDE ENCONTRAR OS DADOS PARA ATUALIZAR

### Faturamento do Mês
- Verificar extratos de: Asaas, Pagar.me, Stripe, Crypto
- Somar todas as transações do mês
- Separar B2B de B2C

### Fluxo de Caixa
- Entrar em cada gateway e verificar:
  - **Em Conta:** saldo disponível agora
  - **A Receber:** valores confirmados mas ainda não recebidos

### Taxas e Custos
- Verificar extratos bancários
- Somar todas as taxas cobradas pelos gateways
- Incluir taxas de antecipação (se houver)

---

## 📊 CHECKLIST DE ATUALIZAÇÃO MENSAL

Imprima ou salve este checklist:

```
□ 1. Coletar dados de todos os gateways de pagamento
□ 2. Calcular faturamento total do mês
□ 3. Verificar saldos em conta de cada gateway
□ 4. Verificar valores a receber confirmados
□ 5. Atualizar modulo_fechamento_mes.py:
    □ Linha 53: Mês/ano
    □ Linha 56: Data de atualização
    □ Linhas 67-96: Métricas de faturamento
    □ Linhas 101-138: Tabela de faturamento
    □ Linhas 167-196: Métricas de caixa
    □ Linhas 201-246: Tabela de caixa
    □ Linhas 267-315: Comparativo
    □ Linhas 321-353: Resumo executivo
□ 6. Atualizar modulo_fluxo_caixa.py:
    □ Linha 19: Mês/ano
    □ Linha 20: Data de atualização
    □ Linhas 23-64: Dados dos gateways
□ 7. Testar localmente (streamlit run app.py)
□ 8. Fazer commit e push para GitHub
□ 9. Verificar deploy no Streamlit Cloud
□ 10. Acessar dashboard em produção e conferir
```

---

## 🆘 TROUBLESHOOTING

### Problema: Git pede senha mas não aceita

**Solução:** Você precisa usar um Personal Access Token, não sua senha normal.

1. Vá em: https://github.com/settings/tokens
2. Clique em "Generate new token" > "Generate new token (classic)"
3. Dê um nome: "Notebook Update Dashboard"
4. Marque: `repo` (acesso completo ao repositório)
5. Clique em "Generate token"
6. **COPIE O TOKEN** (você não verá de novo!)
7. Use este token como senha no Git

---

### Problema: Streamlit não atualiza automaticamente

**Solução 1:** Verificar se o push foi bem-sucedido
```bash
git log -1  # Ver último commit
git status  # Ver se está tudo limpo
```

**Solução 2:** Forçar redeploy manual no Streamlit
1. Acesse https://share.streamlit.io/
2. Clique nos 3 pontinhos do seu app
3. Clique em "Reboot app"

---

### Problema: Erro "ModuleNotFoundError" no deploy

**Solução:** Verificar se o arquivo `requirements.txt` está atualizado

```bash
# Ver o conteúdo
cat requirements.txt

# Deve ter pelo menos:
streamlit>=1.28.0
pandas>=2.0.0
plotly>=5.15.0
openpyxl>=3.1.0
xlrd>=2.0.0
python-dateutil>=2.8.0
requests>=2.31.0
```

---

### Problema: Dashboard mostra erro ao carregar dados

**Solução:** Verificar se as planilhas Excel estão no repositório

```bash
# Listar arquivos Excel
ls *.xlsx

# Adicionar se necessário
git add "Matriz financeira.xlsx"
git commit -m "Adicionar planilha de dados"
git push origin main
```

---

## 📞 COMANDOS ÚTEIS

### Ver histórico de commits
```bash
git log --oneline
```

### Desfazer mudanças locais (CUIDADO!)
```bash
git checkout -- modulo_fechamento_mes.py
```

### Ver diferenças antes de commitar
```bash
git diff modulo_fechamento_mes.py
```

### Verificar URL do repositório
```bash
git remote -v
```

---

## 🔐 SEGURANÇA

### Personal Access Token
- **NUNCA** compartilhe seu token
- **NUNCA** faça commit de um arquivo com o token
- Guarde em local seguro (gerenciador de senhas)
- Se vazar, revogue imediatamente: https://github.com/settings/tokens

### Senha do Dashboard
Atual: `CulturaBuilder852@`

**⚠️ RECOMENDAÇÃO:** Migrar para variável de ambiente no futuro
- Ver: https://docs.streamlit.io/streamlit-community-cloud/deploy-your-app/secrets-management

---

## 📚 RECURSOS ADICIONAIS

- **Documentação Git:** https://git-scm.com/doc
- **GitHub Docs:** https://docs.github.com/
- **Streamlit Cloud:** https://docs.streamlit.io/streamlit-community-cloud
- **Streamlit Secrets:** https://docs.streamlit.io/streamlit-community-cloud/deploy-your-app/secrets-management

---

## ✅ RESUMO RÁPIDO (Para quem já sabe)

```bash
# 1. Atualizar repositório local
cd dash-financeiro
git pull origin main

# 2. Editar arquivos
# - modulo_fechamento_mes.py (dados de outubro)
# - modulo_fluxo_caixa.py (saldos atualizados)

# 3. Testar localmente (opcional mas recomendado)
streamlit run app.py

# 4. Commit e push
git add modulo_fechamento_mes.py modulo_fluxo_caixa.py
git commit -m "Atualização dados financeiros - Outubro 2025"
git push origin main

# 5. Aguardar deploy automático (1-3 min)
# 6. Verificar em produção
```

---

**📅 Última atualização deste tutorial:** 28/10/2025
**✍️ Criado por:** Claude Code
**🔗 Repositório:** https://github.com/Kalarien/dash-financeiro.git

---

**💡 DICA FINAL:**

Faça um teste ANTES de viajar! Clone o repositório no notebook, faça uma pequena mudança (ex: mudar uma cor), commit, push e veja se o deploy funciona. Assim você garante que tudo está configurado corretamente.

Boa viagem! 🚀
