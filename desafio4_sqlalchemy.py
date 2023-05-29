import sqlalchemy
from sqlalchemy.orm import declarative_base, relationship, Session
from sqlalchemy import (
    Column,
    func,
    select,
    Integer,
    Float,
    String,
    ForeignKey,
    create_engine,
    inspect,
)

Base = declarative_base()


class Cliente(Base):
    __tablename__ = "cliente"
    # atributos
    id = Column(Integer, primary_key=True)
    name = Column(String)
    cpf = Column(String(9))
    endereco = Column(String)

    conta = relationship(
        "Conta", back_populates="cliente", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"Cliente(id={self.id}, name={self.name}, cpf={self.cpf}, endereco={self.endereco})"


class Conta(Base):
    __tablename__ = "conta"
    id = Column(Integer, primary_key=True)
    tipo_conta = Column(String(20), nullable=False)
    agencia = Column(String(10), nullable=False)
    num_conta = Column(Integer, nullable=False)
    saldo = Column(Float, nullable=False)
    cliente_id = Column(Integer, ForeignKey("cliente.id"), nullable=False)

    cliente = relationship("Cliente", back_populates="conta")

    def __repr__(self):
        return f"Conta (id={self.id}, tipo_conta={self.tipo_conta}, agencia={self.agencia}, num_conta={self.num_conta}, saldo={self.saldo})"


print(Cliente.__tablename__)
print(Conta.__tablename__)

# conexao com o banco de dados
engine = create_engine("sqlite://")

# criando as classes como tabelas no BD
Base.metadata.create_all(engine)

# depreciacao
# print(engine.table_names())

# investiga o esquema de BD
inspetor_engine = inspect(engine)
print(inspetor_engine.has_table("cliente"))
print(inspetor_engine.get_table_names())
print(inspetor_engine.default_schema_name)


with Session(engine) as session:
    juliana = Cliente(
        name="juliana",
        cpf="1234567890",
        endereco="rua macarone",
        conta=[
            Conta(
                tipo_conta="corrente", agencia="1001", num_conta=5529302, saldo=1000.23
            )
        ],
    )

    sandy = Cliente(
        name="sandy",
        cpf="2345678901",
        endereco="travessa cambui",
        conta=[
            Conta(tipo_conta="poupanca", agencia="1001", num_conta=7729302, saldo=100)
        ],
    )

    patrick = Cliente(
        name="patrick",
        cpf="3456789012",
        endereco="rua luis silva",
        conta=[
            Conta(tipo_conta="corrente", agencia="1001", num_conta=6629302, saldo=-200)
        ],
    )

    # enviando para o BD
    session.add_all([juliana, sandy, patrick])

    session.commit()

stmt = select(Cliente).where(Cliente.name.in_(["juliana", "sandy", "patrick"]))
print("\nRecuperando usuarios a partir de condiçao de filtragem")
for cliente in session.scalars(stmt):
    print(cliente)

stmt_Conta = select(Conta).where(Conta.cliente_id.in_([1]))
print("\nRecuperando as contas a partir de condiçao de filtragem")
for conta in session.scalars(stmt_Conta):
    print(conta)

stmt_order = select(Cliente).order_by(Cliente.name.asc())
print("\nRecuperando info de maneira ordenada")
for result in session.scalars(stmt_order):
    print(result)


stmt_join = select(Cliente.cpf, Conta.tipo_conta).join_from(Conta, Cliente)
# print("\nRecuperando info de maneira conjunta")
# for result in session.scalars(stmt_join):
#    print(result)
# essa call não funciona pq o scalar só pega o primeiro elemento, diferente do fetchall

connection = engine.connect()
results = connection.execute(stmt_join).fetchall()
print("\nExecutando statement a partir da connection")
for result in results:
    print(result)

stmt_count = select(func.count("*")).select_from(Cliente)
print("\nContando o numero de instancias em Cliente")
for result in session.scalars(stmt_count):
    print(result)

session.close()
