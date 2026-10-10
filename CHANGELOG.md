# Changelog

## v0.1.0

### Resumo

- A primeira release da loja: o total com desconto validado, e os portes de 3,50 € nas compras abaixo de 50 €.
- Para quem compra na loja de prova do FORGE.

### O que entra

- #11 — portes nas compras abaixo de 50 € (PR #12)
- #3 — o desconto tem de estar entre 0 e 100 % (PR #4)
- #1 — adotar o FORGE 1.0 (PR #2)
- #5 — o pack GitHub com a reavaliação corrigida (PR #6)
- Só técnica: o FORGE da Wave 2, em `STANDARD` e modo solo, e o deploy do projeto (PR #9)

### Ação necessária

Nenhuma.

### Validação em Qual

- O candidato: `v0.1.0-rc.1` (o commit acima), instalado em Qual a 2026-10-10 — `total([10, 20], 10)` = 30,15 €.
- A validar pela Functional Authority antes de aprovar este PR.

### Riscos

- Compras abaixo de 50 € passam a custar mais 3,50 € (com o desconto aplicado também aos portes).

### Rollback

Primeira release: não há versão anterior em Produção. Voltar atrás é retirar a loja de Produção; não há dados nem migrações.
