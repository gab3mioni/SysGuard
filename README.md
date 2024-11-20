# **SysGuard**

SysGuard é uma aplicação full stack que permite o monitoramento de métricas de um sistema, como uso de CPU, memória e disco. O backend fornece uma API em Python utilizando Flask, enquanto o frontend foi desenvolvido em React para exibir as informações em tempo real.

---

## **🛠️ Construído com**

### **Backend**
- [Python 3.12](https://www.python.org/) - Linguagem principal do backend
- [Flask](https://flask.palletsprojects.com/) - Framework para construção da API
- [Flask-CORS](https://flask-cors.readthedocs.io/) - Para lidar com CORS na API
- [Psutil](https://psutil.readthedocs.io/) - Monitoramento de recursos do sistema
- [Docker SDK para Python](https://docker-py.readthedocs.io/) - Interação com containers Docker
- [SQLAlchemy](https://www.sqlalchemy.org/) - Mapeamento objeto-relacional (ORM)

### **Frontend**
- [React 18.3](https://react.dev/) - Framework JavaScript para construção da interface
- [Axios](https://axios-http.com/) - Consumir a API
- [Node.js](https://nodejs.org/) - Ambiente de execução para o React

### **Ambiente**
- [Docker](https://www.docker.com/) - Gerenciamento de containers
- [Docker Compose](https://docs.docker.com/compose/) - Orquestração de serviços em containers

---

## **🚀 Começando**

Essas instruções permitirão que você obtenha uma cópia do projeto em operação na sua máquina local para fins de desenvolvimento e teste.

### **📋 Pré-requisitos**

Certifique-se de ter os seguintes itens instalados:

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

---

## **🔧 Instalação**

1. Clone o repositório:
   ```bash
      git clone https://github.com/seu-usuario/sysguard.git
   ```

2. Navegue até o diretório:
    ```bash
      cd sysguard
    ```
   
3. Para executar o projeto, use o comando:
    ```bash
      docker-compose up --build
    ```
   
    Este comando:
    - Constrói as imagens Docker necessárias.
    - Sobe os containers para o backend e frontend.
   

4. Após a execução, o backend estará disponível em:
    ```bash
      http://localhost:5000/api
    ```
   E o frontend poderá ser acessado em:
    ```bash
      http://localhost:3001
    ```
   
## 📌 Versão

Nós usamos [Git](https://git-scm.com/) para controle de versão. Para as versões disponíveis, observe as [tags neste repositório](https://github.com/gab3mioni/SysGuard/tags).

## ✒️ Autores

* **Gabriel Mioni Bastos** - *Desenvolvedor Fullstack* - [gab3mioni](https://github.com/gab3mioni)