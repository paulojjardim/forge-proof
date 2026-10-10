# loja

Instruções do agente.

<!-- FORGE:BEGIN -->
## FORGE — contrato de engenharia

Este repositório usa o **FORGE**. Configuração: `.forge/project.yaml`.
Estado: `forge status`.

1. Perceber o resultado pedido antes de editar; sem âmbito negativo
   declarado, perguntar.
2. Não inventar requisitos: uma decisão de produto ou de autoridade é de
   quem a tem — parar e perguntar.
3. A alteração coerente mais pequena, dentro do âmbito.
4. Preservar alterações do utilizador que não pertencem à tarefa.
5. Afirmar o que é determinístico só com evidência de ferramenta: um
   relato não é uma prova.
6. `UNDETERMINED` nunca é `PASS`: reportar a incerteza e o que não foi
   verificado.
7. Nunca alterar ou desligar um teste, nem silenciar um lint, um scanner
   ou uma check, para ficar verde.
8. Segredos e dados pessoais reais nunca no repositório, nos testes nem
   nos logs.
9. Nunca escrever em `.forge/` nem correr `forge accept`: a evidência é do
   FORGE, a aceitação é da Functional Authority.
10. Nunca aprovar uma excepção de segurança: propor à pessoa a linha de
    `VULNERABILIDADES-ACEITES.md`, com prazo — nunca a escrever.
11. Não commitar, publicar nem integrar sem autorização explícita.
12. Antes de dizer que está feito: `forge verify` até `PASS`, e
    `forge status` para o que falta e de quem.
13. Parar quando a decisão é de uma pessoa.

Os fluxos estão nas skills `/forge-define`, `/forge-implement`,
`/forge-verify`, `/forge-security` e `/forge-resume`.

Esta secção é gerida pelo FORGE. O resto do ficheiro é do projecto, e não
é tocado.
<!-- FORGE:END -->
