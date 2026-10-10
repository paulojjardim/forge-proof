#!/usr/bin/env bash
# «Instalar» em Qual: a loja de prova não tem servidores — desempacota o
# artefacto, corre-o, e diz no resumo do run o que instalou.
set -euo pipefail
: "${FORGE_ARTIFACT_DIR:?o artefacto vem do FORGE}"
destino="$(mktemp -d)"
tar -xzf "$FORGE_ARTIFACT_DIR/loja.tar.gz" -C "$destino"
python -c "import sys; sys.path.insert(0, '$destino/loja'); import loja; print('Qual: total([10, 20], 10) =', loja.total([10, 20], 10))"
{
  echo "### Qual: ${GITHUB_REF_NAME} (${GITHUB_SHA})"
  echo '```'
  cat "$FORGE_ARTIFACT_DIR/SHA256SUMS" 2>/dev/null || sha256sum "$FORGE_ARTIFACT_DIR/loja.tar.gz"
  echo '```'
} >> "${GITHUB_STEP_SUMMARY:-/dev/stdout}"
