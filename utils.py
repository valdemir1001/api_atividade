from models import Pessoas

def insere_pessoas():
    pessoa = Pessoas(nome='Alves',idade=47)
    print(pessoa)
    pessoa.save()

def consulta():
    pessoa = Pessoas.query.all()
    pessoa = Pessoas.query.filter_by(nome='Alves')
    for p in pessoa:
        print(p)

if __name__ == '__main__':
    #insere_pessoas()
    consulta()