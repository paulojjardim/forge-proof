#!/usr/bin/env bash
# O artefacto da loja: o código, num arquivo. Constrói-se uma vez, em Qual
# (deploy-qual.yml); a Produção instala este mesmo ficheiro.
set -euo pipefail
: "${FORGE_ARTIFACT_DIR:?o FORGE diz onde pôr o artefacto}"
git archive --format=tar.gz --prefix=loja/ -o "$FORGE_ARTIFACT_DIR/loja.tar.gz" HEAD loja.py
