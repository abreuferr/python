# Repositório: python

Coleção de estudos em Python, não uma aplicação única — cada subpasta
(`crypto/`, `info/`, `science/<nome>/`, `usp_ime/`) é um módulo
independente, sem ponto de entrada compartilhado. Ver README.md para
setup de ambiente e validação dos exemplos.

## Convenção de organização

Cada módulo tem seu próprio `README.md` na raiz do módulo — nunca dentro
de `doc/` ou `src/`. Documentação específica por tópico (ex.: notas em
`crypto/doc/`) continua normalmente em `doc/`.

## Gotcha

`scripts/validate.py` varre o repositório inteiro a partir de
`ROOT = Path(__file__).resolve().parent.parent` (sobe dois níveis pra sair
de `scripts/` e chegar na raiz). Se o script for movido de novo, esse
`ROOT` precisa ser ajustado, senão ele só varre a própria pasta.
