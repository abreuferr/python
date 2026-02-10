ssh-agent bash -c 'ssh-add /usr/lib/libeToken.so; git clone git@github.com:abreuferr/python.git'


python -m venv venv
source venv/bin/activate

pip list
pip show pacote
pip install pacote
pip uninstall pacote
pip freeze > requirements.txt
pip install -r requirements.txt