from sqlalchemy import create_engine, column, Integer, String, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///atividades.db', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()


class Pessoas(Base):
    __tablename__ = 'pessoas'
    id = column(Integer, primary_key=True)
    nome = column(String(40), index=True)
    idade = column(Integer)

    def __repr__(self):
        return '<Pessoa {}>'.format(self.nome)

    def save(self):
        db_session.add(self)
        db_session.commit()


class Atividades(Base):
    __tablename__ = 'atividades'
    id = column(Integer, primary_key=True)
    nome = column(String(80))
    pessoa_id = column(Integer, ForeignKey('pessoas.id'))
    pessoa = relationship('Pessoas')


def init_db():
    Base.metadata.create_all(bind=engine)


if __name__ == '__main__':
    init_db()
