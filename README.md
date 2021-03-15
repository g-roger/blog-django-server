# django-blog-server

Exemplo de aplicação Django para ser aplicada em pessoas que estão aprendendo a criação de sites dinâmicos, integrando back-end com front-end.

### Como iniciar o projeto

* Iniciar ambiente
```shell script
$ python -m venv .venv
$ source .venv/bin/activate 
$ pip install -r requirements.txt
```

* executar servidor
```shell script
% python manage.py runserver
```

* executar migrações

```shell script
$ python manage.py migrate
```

------
* Banco de dados

django-blog-server utiliza o banco de dados SQLITE. Não necessitando de configurações extras para execução do banco.
