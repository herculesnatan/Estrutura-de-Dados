def verificaSimetria(raiz):
    def eh_Simetrica(esq, dir):
        if not esq and not dir:
            return True
        elif not esq or not dir:
            return False
        return (esq.dado == dir.dado) and eh_Simetrica(esq.esq, dir.dir) \
            and eh_Simetrica(esq.dir, dir.esq)

    if not raiz:
        return True
    return eh_Simetrica(raiz.esq, raiz.dir)