<div align="center">

# Torre de Hanói em Python

![Python](https://img.shields.io/badge/PYTHON-3.12%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pytest](https://img.shields.io/badge/TESTS-PYTEST-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)
![Status](https://img.shields.io/badge/STATUS-CONCLU%C3%8DDO-44CC11?style=for-the-badge)


Implementação da **Torre de Hanói** em Python com foco em fundamentos de programação: estruturas de dados tipo pilha (LIFO), recursão, interface de linha de comando (CLI) interativa, testes automatizados com `pytest`, análise de estilo com `flake8` e integração contínua via GitHub Actions.


</div>

---

## Objetivo

Projeto desenvolvido com foco em aprendizado e consolidação de fundamentos de programação em Python, utilizando o clássico problema matemático da Torre de Hanói para praticar lógica, recursão, estruturas de dados, organização de código em módulos, testes automatizados e integração contínua (CI).

Por ser um projeto de estudo, a proposta prioriza clareza, legibilidade e boas práticas em vez de complexidade desnecessária — registrando na prática a evolução do código ao longo das etapas.

---

## Estrutura do projeto

```text
.
├── .github/
│   └── workflows/
│       └── ci.yml          # Esteira de CI (flake8 + pytest)
├── docs/
│   └── demo.gif            # Demonstração visual da execução no terminal
├── src/
│   ├── __init__.py
│   ├── hanoi.py            # Motor lógico (pilhas, regras, validação e recursão)
│   ├── main.py             # CLI interativa (modos automático e manual)
│   └── README.md           # Documentação técnica dos módulos em src/
├── tests/
│   ├── __init__.py
│   └── test_hanoi.py       # Suíte de testes unitários com pytest
├── .gitignore
└── requirements.txt
```

---

## Como executar localmente

1. Clone o repositório e entre na pasta:

  ```bash
   git clone https://github.com/lauramorgadobastos/torre-de-hanoi-python
   cd torre-de-hanoi-python
   ```
3. Crie e ative o ambiente virtual:

 ```bash
  python -m venv .venv
  .\.venv\Scripts\Activate.ps1
   ```

3. Instale as dependências:

 ```bash
 pip install -r requirements.txt
   ```

4. Execute a aplicação em modo interativo:

```bash
python -m src.main
```

Você pode escolher entre:
* Modo 1 (Resolução automática): acompanha passo a passo a sequência ótima gerada por recursão ($2^n - 1$ movimentos).
* Modo 2 (Modo manual): joga movimentando os discos entre os pinos A, B e C, com opção de sair (S / sair) a qualquer momento.

### Testes e qualidade de código

```bash
flake8 src tests --max-line-length=100
pytest -v
```

Para detalhes sobre a arquitetura interna da aplicação, consulte [src/README.md](src/README.md)

---

## Sobre Mim

Desenvolvido por *Laura Morgado Bastos Gomes*
Estudante de *Sistemas de Informação - PUC Minas*.

### Conecte-se comigo

Você pode me encontrar nos canais abaixo:


[![Linkedin](https://img.shields.io/badge/LinkedIn-4C1D95?style=for-the-badge&logo=linkedin&logoColor=fff)](https://www.linkedin.com/in/laura-morgado-bastos?)
[![GitHub](https://img.shields.io/badge/GitHub-4C1D95?style=for-the-badge&logo=github&logoColor=fff)](https://github.com/lauramorgadobastos)
[![Email](https://img.shields.io/badge/Email-4C1D95?style=for-the-badge&logo=gmail&logoColor=fff)](mailto:laura.bastosmorgado27@gmail.com)

---

##  Licença

Este repositório não possui uma licença específica definida, pois tem caráter estritamente educacional e acadêmico.

---

<div align="center">
  <sub>Desenvolvido por <b>Laura Morgado</b>.</sub>
</div>
