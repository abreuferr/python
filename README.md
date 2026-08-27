ssh-agent bash -c 'ssh-add /usr/lib/libeToken.so; git clone git@github.com:abreuferr/python.git'


python -m venv venv
source venv/bin/activate

pip list
pip show pacote
pip install pacote
pip uninstall pacote
pip freeze > requirements.txt
pip install -r requirements.txt

## Validação dos exemplos

Com as dependências de estudo instaladas, execute:

```sh
python validate.py
```

O comando valida a sintaxe de todos os scripts e executa os testes automatizados
que não exigem interface gráfica ou entrada interativa.
