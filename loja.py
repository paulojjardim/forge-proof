"""A loja de prova do FORGE 1.0."""


def total(precos, desconto=0):
    """O total dos preços, com um desconto percentual entre 0 e 100."""
    if not 0 <= desconto <= 100:
        raise ValueError(f"desconto de {desconto} %: tem de estar entre 0 e 100")
    return round(sum(precos) * (1 - desconto / 100), 2)
