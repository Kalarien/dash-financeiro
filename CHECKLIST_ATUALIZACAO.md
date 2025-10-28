# ✅ CHECKLIST: Atualização Mensal do Dashboard

**Mês a atualizar:** _______________
**Data:** _____ / _____ / _____

---

## 📊 COLETA DE DADOS

### Faturamento
- [ ] Acessar Asaas e coletar faturamento do mês
- [ ] Acessar Pagar.me e coletar faturamento do mês
- [ ] Acessar Stripe e coletar faturamento do mês
- [ ] Acessar Crypto e coletar faturamento do mês
- [ ] Verificar vendas B2B do mês
- [ ] Calcular total de transações
- [ ] Calcular faturamento total

**Faturamento Total:** R$ _________________

### Fluxo de Caixa
- [ ] Asaas - Saldo em conta: R$ _________________
- [ ] Asaas - A receber: R$ _________________
- [ ] Pagar.me - Saldo em conta: R$ _________________
- [ ] Pagar.me - A receber: R$ _________________
- [ ] Stripe - Saldo em conta: R$ _________________
- [ ] Stripe - A receber: R$ _________________
- [ ] Crypto - Saldo em conta: R$ _________________
- [ ] Crypto - A receber: R$ _________________
- [ ] B2B - Saldo em conta: R$ _________________
- [ ] B2B - A receber: R$ _________________

**Total em Conta:** R$ _________________
**Total a Receber:** R$ _________________

### Taxas e Custos
- [ ] Somar taxas de cobrança
- [ ] Somar taxas de antecipação
- [ ] Somar outras taxas

**Total de Taxas:** R$ _________________

---

## 💻 ATUALIZAÇÃO DO CÓDIGO

### Setup Inicial (no notebook)
- [ ] Git está instalado
- [ ] Repositório clonado: `git clone https://github.com/Kalarien/dash-financeiro.git`
- [ ] Personal Access Token do GitHub salvo

### Atualizar Repositório
```bash
cd dash-financeiro
git pull origin main
```
- [ ] Repositório atualizado sem conflitos

### Editar Arquivos

#### modulo_fechamento_mes.py
- [ ] Linha 53: Atualizar mês/ano no título
- [ ] Linha 56: Atualizar data de atualização
- [ ] Linhas 67-96: Atualizar métricas de faturamento (4 cards)
- [ ] Linhas 101-138: Atualizar tabela de faturamento por adquirente
- [ ] Linhas 167-196: Atualizar métricas de caixa (4 cards)
- [ ] Linhas 201-246: Atualizar tabela de caixa por adquirente
- [ ] Linhas 267-315: Atualizar comparativo Faturamento vs Caixa
- [ ] Linhas 321-353: Atualizar resumo executivo (4 cards)

#### modulo_fluxo_caixa.py
- [ ] Linha 19: Atualizar mês/ano
- [ ] Linha 20: Atualizar data de atualização
- [ ] Linhas 23-64: Atualizar dados dos 5 gateways

#### modulo_faturamento_tempo_real.py (se necessário)
- [ ] Verificar se há dados a atualizar

---

## 🧪 TESTES

### Teste Local
```bash
streamlit run app.py
```
- [ ] Dashboard abre sem erros
- [ ] Login funciona
- [ ] Aba "Faturamento do Mês" mostra dados do novo mês
- [ ] Aba "Fluxo de Caixa" mostra saldos atualizados
- [ ] Todos os valores estão corretos
- [ ] Nenhum erro no console

---

## 🚀 DEPLOY

### Commit e Push
```bash
git add modulo_fechamento_mes.py modulo_fluxo_caixa.py
git commit -m "Atualização dados financeiros - [MÊS] 2025"
git push origin main
```
- [ ] Commit realizado com sucesso
- [ ] Push realizado com sucesso

### Verificação no Streamlit Cloud
- [ ] Acessar https://share.streamlit.io/
- [ ] Ver logs do deploy
- [ ] Deploy concluído com sucesso (1-3 min)

### Verificação Final
- [ ] Acessar dashboard em produção
- [ ] Fazer login
- [ ] Verificar aba "Faturamento do Mês"
- [ ] Verificar aba "Fluxo de Caixa"
- [ ] Todos os dados estão corretos
- [ ] Sistema funcionando 100%

---

## 📝 NOTAS

**Problemas encontrados:**
_________________________________________________________________
_________________________________________________________________
_________________________________________________________________

**Tempo gasto:** _______ minutos

**Próxima atualização:** _____ / _____ / _____

---

**✅ ATUALIZAÇÃO CONCLUÍDA COM SUCESSO!**

---

## 🆘 CONTATOS DE EMERGÊNCIA

**Se algo der errado:**
1. Verificar logs no Streamlit Cloud
2. Fazer rollback: `git revert HEAD`
3. Entrar em contato com suporte

**Links Úteis:**
- Repositório: https://github.com/Kalarien/dash-financeiro.git
- Streamlit Cloud: https://share.streamlit.io/
- Tutorial completo: TUTORIAL_ATUALIZACAO_MENSAL.md
