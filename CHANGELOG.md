# Changelog

## v0.1.1

### Resumo

- Hotfix do incidente #14: um carrinho vazio deixa de pagar 3,50 € de portes.
- Para quem usa a loja de prova do FORGE.

### O que entra

- #14 — incidente: um carrinho vazio pagava portes (PR #15, hotfix com a prova de regressão)

### Ação necessária

Nenhuma.

### Validação em Qual

- O candidato: `v0.1.1-rc.1` (o commit acima), instalado em Qual a 2026-10-12 — o mesmo artefacto que vai para Produção.
- A validar pela Functional Authority antes de aprovar este PR: `total([])` = 0 €; `total([10, 20], 10)` continua 30,15 €.

### Riscos

- Nenhum além da correção: só o carrinho vazio muda de total.

### Rollback

Reinstalar `v0.1.0` em Produção — o deploy da tag anterior, com o artefacto que já lá esteve. Não há dados nem migrações; o carrinho vazio volta a ter o defeito do #14.
