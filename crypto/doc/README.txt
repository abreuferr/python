# Material de estudo: criptografia em Python

Os arquivos em `../src` são scripts independentes para explorar primitivas e
protocolos criptográficos. Eles **não são componentes prontos para produção**.
Em especial, alguns programas mostram intencionalmente abordagens históricas ou
inseguras para tornar visível o motivo de protocolos modernos existirem.

## Como executar

Use Python 3.9 ou superior, crie um ambiente virtual e instale as dependências
do diretório `crypto`:

```sh
python -m venv .venv
source .venv/bin/activate
python -m pip install -r crypto/requirements.txt
python crypto/src/aes-256-gmc-in-python.py
```

Cada script gera suas próprias chaves e valores de demonstração. As chaves
privadas impressas na tela são efêmeras e servem somente para acompanhar os
cálculos; nunca registre ou exponha segredos dessa forma em software real.

## Leituras guiadas

- `rnd.py` mostra por que `random` e sementes baseadas em tempo não devem gerar
  segredos; para isso, use `secrets` ou `os.urandom`.
- `aes-ctr-in-python.py` demonstra confidencialidade, mas CTR não autentica os
  dados. Compare-o com os exemplos AES-GCM, que detectam adulteração.
- `rsa-key-sign-verify-in-python.py` implementa a operação matemática crua de
  RSA para estudo. Ela não é uma assinatura segura: sistemas reais usam um
  esquema codificado, como RSA-PSS.
- Os scripts com `tinyec` são para visualizar aritmética de curvas elípticas.
  A própria biblioteca não é apropriada para produção e não deve ser usada para
  validar pontos recebidos de uma rede.

## Fontes de informação

- Códigos Python: https://cryptobook.nakov.com
