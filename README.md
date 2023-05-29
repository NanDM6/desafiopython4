# desafiopython4
Utilizando Python em conjunto com SQLAlchemy e PymongoDB para inserir e manipular dados.
Um código é utilizando SQLAlchemy, outro para persistir os dados no BD com pymongo e o terceiro para manipular os dados inseridos.
Principais conceitos utilizados nos códigos:
SQLAlchemy é uma biblioteca em Python que facilita a interação com bancos de dados relacionais.
A interação com o banco de dados é realizada por meio de uma abstração chamada "Engine", que representa a conexão com o banco de dados.
As tabelas do banco de dados são representadas como classes em SQLAlchemy, usando a classe base "declarative_base()".
As colunas das tabelas são definidas como atributos nas classes usando os tipos de dados fornecidos pelo SQLAlchemy, como Integer, String, etc.
As relações entre tabelas são estabelecidas por meio de relacionamentos, utilizando a função "relationship".
Consultas SQL são criadas por meio de objetos "select", "insert", "update" e "delete", combinados com cláusulas como "where" e "order_by".
As consultas são executadas por meio do método "execute" do objeto "Engine" ou por meio de uma sessão, obtida por meio do objeto "Session".
PyMongo:

PyMongo é uma biblioteca em Python para interagir com o MongoDB, um banco de dados NoSQL orientado a documentos.
A conexão com o banco de dados é estabelecida por meio do objeto "MongoClient", fornecendo a string de conexão adequada.
As coleções do banco de dados são representadas como atributos em um objeto "Database".
Consultas ao banco de dados são realizadas por meio de métodos como "find", "insert_one", "update_one", "delete_one", combinados com filtros e projeções.
Índices podem ser criados em coleções para otimizar consultas e garantir unicidade de valores, usando o método "create_index".
