<h1>Setup</h1>
<p>É necessário levantar um container docker para rodar esse projeto. Para isso, tendo o docker instalado, execute o comando abaixo:</p>

```docker run --name dynamodblocal -p 8000:8000 -v dynamodbdata:/home/dynamodblocal/data amazon/dynamodb-local```

<p>Após isso, instale as dependências executando o seguinte comando na raiz do projeto</p>

```pip install -r requirements.txt```

<p>Em seguida, é possível rodar o projeto com o seguinte comando:</p>

```python src/app.py```