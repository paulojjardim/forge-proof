"""A loja de prova do FORGE 1.0."""

#: Os portes, e o subtotal a partir do qual são grátis (#11).
PORTES = 3.50
PORTES_GRATIS_A_PARTIR_DE = 50


def total(precos, desconto=0):
    """O total dos preços, com os portes e um desconto percentual entre 0 e 100.

    Os portes cobram-se quando o subtotal dos artigos, antes do desconto, é
    inferior a 50 € e há artigos; o desconto aplica-se ao total com portes.
    """
    if not 0 <= desconto <= 100:
        raise ValueError(f"desconto de {desconto} %: tem de estar entre 0 e 100")
    subtotal = sum(precos)
    # Sem artigos, sem portes: um carrinho vazio custa 0 €.
    portes = PORTES if precos and subtotal < PORTES_GRATIS_A_PARTIR_DE else 0
    return round((subtotal + portes) * (1 - desconto / 100), 2)
