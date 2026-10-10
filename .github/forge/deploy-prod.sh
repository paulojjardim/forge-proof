#!/usr/bin/env bash
# «Instalar» em Produção: o mesmo artefacto que esteve em Qual — conferido
# pelo deploy-prod.yml antes de chegar aqui.
set -euo pipefail
: "${FORGE_ARTIFACT_DIR:?o artefacto vem do FORGE}"
destino="$(mktemp -d)"
tar -xzf "$FORGE_ARTIFACT_DIR/loja.tar.gz" -C "$destino"
python -c "import sys; sys.path.insert(0, '$destino/loja'); import loja; print('Prod: total([10, 20], 10) =', loja.total([10, 20], 10))"
{
  echo "### Produção: ${GITHUB_REF_NAME} (${GITHUB_SHA})"
  echo '```'
  cat "$FORGE_ARTIFACT_DIR/SHA256SUMS"
  echo '```'
} >> "${GITHUB_STEP_SUMMARY:-/dev/stdout}"
