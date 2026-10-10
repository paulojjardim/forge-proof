"""A loja de prova do FORGE 1.0."""


def total(precos, desconto=0):
    """O total dos preços, com um desconto percentual."""
    return round(sum(precos) * (1 - desconto / 100), 2)
