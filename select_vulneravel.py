from typing import Optional

from sqlmodel import Field, Session, SQLModel, create_engine, select, text


class Hero(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: Optional[int] = None


engine = create_engine("sqlite:///database.db")

with Session(engine) as session:
    # Sua consulta SQL
    statement = text("SELECT * FROM hero;") # SQL Injection => poderia ser "DROP TABLE Hero"
    
    # Executando a consulta
    results = session.exec(statement)
    
    # Fetch dos resultados
    heroes = results.fetchall()
    
    # Imprimindo os resultados
    for hero in heroes:
        print(hero)