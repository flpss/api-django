# API Django - Biblioteca (teste)

## Installation

Você precisa ter o [Docker](https://www.docker.com/) e o Docker Compose instalados e rodando no computador. O projeto foi testado com o docker 19.03.8-ce e o docker-compose 1.25.5, no sistema operacional Arch Linux.

Após clonar o projeto, basta utilizar:

```bash
docker-compose up -d --build
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py collectstatic
```

Para parar a aplicação, use:
```bash
docker-compose down
```

Caso deseje resetar o banco, com a aplicação rodando, use:
```
docker-compose exec web python manage.py flush
```
## Uso
Existe o painel de administração que pode ser acessado em [http://localhost:8000/admin](http://localhost:8000/admin). Para criar uma conta, você pode executar:
```bash
docker-compose exec web python manage.py createsuperuser
```
A API conta com a documentação do próprio django-rest-framework, utilizado no projeto. Basta acessar [http://localhost:8000](http://localhost:8000). Além disso, nos objetos livro e empréstimo, é possível solicitar um único passando o id na url (ex: /livros/2 ou /emprestimos/23).