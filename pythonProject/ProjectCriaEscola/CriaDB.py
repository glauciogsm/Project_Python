from datetime import date
from CriaInstrutor import GeraInstrutor
from CriaCursos import GeraCursos
from CriaTurmas import GeraTurmas
from CriaAlunos import GeraAlunos
from CriaMatriculas import GeraMatriculas
from CriaBancodeDados import Deleta_schema, cria_schema, cria_table

data_hoje = str(date.today())
totAluno=0
while True:
    print('-' * 30)
    print('*     MENU  PRINCIPAL        *')
    print('-' * 30)
    print('* 1 - Cria Instrutores       *')
    print('* 2 - Cria Cursos            *')
    print('* 3 - Cria Turmas            *')
    print('* 4 - Cria Alunos/Matriculas *')
    print('* 5 - Cria Todas             *')
    print('* 6 - Cria Base de dados     *')
    print('* 7 - Sair do sistema        *')
    print('-' * 30)
    opcao = input("Escolha uma opção: ")
    print('-' * 30)
    if opcao == '1':
        GeraInstrutor()
    elif opcao == '2':
        GeraCursos()
    elif opcao == '3':
        GeraTurmas(data_hoje)
    elif opcao == '4':
        registrosAlunos = int(input('Quantos registros de alunos deseja? '))
        GeraAlunos(registrosAlunos)
        GeraMatriculas(registrosAlunos)
    elif opcao == '5':
        Deleta_schema()
        cria_schema()
        cria_table()
        GeraInstrutor()
        GeraCursos()
        GeraTurmas(data_hoje)
        registrosAlunos = int(input('Quantos registros de alunos deseja? '))
        GeraAlunos(registrosAlunos)
        GeraMatriculas(registrosAlunos)
    elif opcao == '6':
        Deleta_schema()
        cria_schema()
        cria_table()
    elif opcao == '7':
        break