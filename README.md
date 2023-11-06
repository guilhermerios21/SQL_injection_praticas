
# flask-sql-injection
  

Aplicação Flask + BD para demonstração de uma vulnerabilidade SQL Injection identificada pelo SAST do .gitlab-ci.yml.

## mydb.db

|id|user |password|
|--|--|--|
|1 |teste@teste.com |1234|
|2 |teste2@teste.com |1234|
|3 |teste@teste.com |12345678|
|4 |teste2@teste.com |87654321|
  
## Código

    63 sql_Query_Not_Injection = text("select * from user where id=:user_id")
    64 result = conn.execute(sql_Query_Not_Injection, user_id = id)
    65
    66 sql_Query_Injection_False_Negative = text("select * from user where id={}".format(id))
    67 result = conn.execute(sql_Query_Injection_False_Negative)
    68
    69 # deprecated in SQLAlchemy >=2.0
    70 sql_Query_Injection = "select * from user where id={}".format(id)
    71 result = conn.execute(sql_Query_Injection)

 - As linhas 63 e 64 **não contém** uma vulnerabilidade SQL Injection;
 - As linhas 66 e 67 **contém** uma vulnerabilidade SQL Injection, **não identificável** no SAST do .gitlab-ci;
 - As linhas 70 e 71 **contém** uma vulnerabilidade SQL Injection, **identificável** no SAST do .gitlab-ci.

## Deploy com docker compose, com MySQL
```
$ docker compose up -d
```

## Deploy local, com SQLite
```
$ python app/app.py run
```
## Explorando a vulnerabilidade
```
$ GET http://localhost:5000/login?id=1%20or%201=1
```

Baseado no projeto [EstudosAvancadosSI](https://github.com/BrunoEleodoro/EstudosAvancadosSI)