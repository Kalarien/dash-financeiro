# 🚀 COMO ATUALIZAR O DASHBOARD (GUIA RÁPIDO)

Este repositório contém o **Dashboard Financeiro** em produção no Streamlit Cloud.

---

## 📚 DOCUMENTAÇÃO DISPONÍVEL

### Para Atualização Mensal:

1. **TUTORIAL_ATUALIZACAO_MENSAL.md** 📖
   - Tutorial completo passo a passo
   - Como usar Git e GitHub
   - Troubleshooting detalhado
   - **LEIA ESTE PRIMEIRO** se for sua primeira vez

2. **CHECKLIST_ATUALIZACAO.md** ✅
   - Checklist imprimível
   - Lista todos os dados a coletar
   - Lista todos os locais a atualizar
   - **USE ESTE** durante a atualização

3. **auxiliar_atualizacao.py** 🤖
   - Script auxiliar interativo
   - Mostra onde estão os dados no código
   - Mostra valores atuais
   - **RODE ESTE** para não se perder

---

## ⚡ RESUMO SUPER RÁPIDO (Para quem já sabe)

```bash
# 1. Atualizar repositório
git pull origin main

# 2. Rodar auxiliar (opcional)
python auxiliar_atualizacao.py

# 3. Editar arquivos:
#    - modulo_fechamento_mes.py
#    - modulo_fluxo_caixa.py

# 4. Testar
streamlit run app.py

# 5. Deploy
git add modulo_fechamento_mes.py modulo_fluxo_caixa.py
git commit -m "Atualização dados financeiros - [MÊS] 2025"
git push origin main
```

---

## 🎯 PRIMEIRA VEZ?

1. Leia: **TUTORIAL_ATUALIZACAO_MENSAL.md**
2. Imprima: **CHECKLIST_ATUALIZACAO.md**
3. Rode: `python auxiliar_atualizacao.py`
4. Siga o passo a passo

---

## 🔗 LINKS IMPORTANTES

- **Repositório:** https://github.com/Kalarien/dash-financeiro.git
- **Streamlit Cloud:** https://share.streamlit.io/
- **Personal Access Token:** https://github.com/settings/tokens

---

## 📞 PRECISA DE AJUDA?

1. Leia o **TUTORIAL_ATUALIZACAO_MENSAL.md** (seção Troubleshooting)
2. Verifique os logs no Streamlit Cloud
3. Use o script `auxiliar_atualizacao.py` para ver o que está diferente

---

**Boa atualização! 🚀**
