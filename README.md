# Desafio Pontotel - Back-End
## Objetivo:
Este projeto consiste em uma API que retorna os valores da Bovespa e de empresas no mercado de ações, possuindo como fonte de dados a API disponibilizada pela https://www.alphavantage.co/. 

# Tecnologias
- [Python](https://www.python.org/downloads/)
- [Visual Studio Code](https://code.visualstudio.com/)
- [Pytest](https://docs.pytest.org/en/stable/)
- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
- [Regex](https://docs.python.org/pt-br/3.8/howto/regex.html)
- [Requests](https://requests.readthedocs.io/en/master/)

# Requisitos
- [Python >= 3.8](https://www.python.org/downloads/)

# Instalação
## Windows

```shell
git clone https://github.com/GustavoMendes1/back-end-alphavantage.git
cd back-end-alphavantage
pip install virtualenv
virtualenv ambvir
cd ambvir/Scripts
activate.bat
Na pasta back-end-alphavantage:pip install -r requirements.txt
Na pasta back-end-alphavantage:python app.py
```
# Testes
```shell
pytest TestsApi.py
```
# Observações
- Foi implementada uma requisição GET para pontuação da Bovespa na rota http://127.0.0.1:5000/
- Foi implementada uma requisição GET para pontuação de empresas em um determinado intervalo de tempo na rota de exemplo: http://127.0.0.1:5000/IBM/5min
