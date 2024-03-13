from CriaClientes import GeraClientes
from CriaLojas import GeraLojas
from CriaCompras import GeraCompras
from datetime import date
import CriaBancodeDados

data_hoje = str(date.today())
totcli=0
while True:
    print('-' * 30)
    print('*     MENU  PRINCIPAL        *')
    print('-' * 30)
    print('* 1 - Cria Clientes          *')
    print('* 2 - Cria Lojas             *')
    print('* 3 - Cria Compras           *')
    print('* 4 - Cria Todas             *')
    print('* 5 - Cria Base de dados     *')
    print('* 6 - Sair do sistema        *')
    print('-' * 30)
    opcao = input("Escolha uma opção: ")
    print('-' * 30)
    if opcao == '1':
        registrosCliente = int(input('Quantos registros de clientes deseja? '))
        GeraClientes(registrosCliente, data_hoje)
    elif opcao == '2':
        GeraLojas()
    elif opcao == '3':
        registrosCompra = int(input('Quantos registros de Compras deseja? '))
        GeraCompras(registrosCompra)
    elif opcao == '4':
        registrosCliente = int(input('Quantos registros de clientes deseja? '))
        GeraClientes(registrosCliente, data_hoje)
        GeraLojas()
        registrosCompra = int(input('Quantos registros de Compras deseja? '))
        GeraCompras(registrosCompra)
    elif opcao == '5':
        CriaBancodeDados.Deleta_schema()
        CriaBancodeDados.cria_schema()
        CriaBancodeDados.cria_table()
        CriaBancodeDados.Dados_cepnatal()
    elif opcao == '6':
        break