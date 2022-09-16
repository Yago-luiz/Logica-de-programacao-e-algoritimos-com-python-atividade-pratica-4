listaProdutos = []
#  Início da função cadastrarProduto.
def cadastrarProduto(co):
    print('Cadastro de Produtos: ')
    print(f'O Codigo do Produto a ser Cadastrado é {co}')
    nome = input('Digite o Nome do Produto: ')
    fabricante = input('Digite o Nome do Fabricante: ')
    valor = float(input('Digite o Valor(R$) do Produto: '))
    dicionarioProduto = {'Código': co,
                         'Nome': nome,
                         'Fabricante': fabricante,
                         'Valor': valor}
    listaProdutos.append(dicionarioProduto.copy())
# Fim da função cadastrarProduto.

#  Início da função consularProduto.
def consutarProduto():
    while True:
        try:
            print('Consulta de Produtos: ')
            opConsultar = int(input('Escolha a Opção desejada:\n'
                                    '1 - Consultar Todos os Produtos\n'
                                    '2 - Consultar Produtos por Código\n'
                                    '3 - Consultar Produtos por Fabricante\n'
                                    '4 - Retornar\n'
                                    '>> '))
            if opConsultar == 1:
                print('Você Selecionou a Opção de Consultar Todos Produtos')
                for produto in listaProdutos: # Selecionar cada dicionário da lista.
                    for key, value in produto.items(): # Selecionar cada conjunto chave/valor do dicionário.
                        print(f'{key} : {value}')
            elif opConsultar == 2:
                print('Digite o Código do Produto: ')
                entrada = int(input('Digite o Código Desejado: '))
                for produto in listaProdutos: # Selecionar cada dicionário da lista.
                    if(produto['Código'] == entrada):
                        for key, value in produto.items():
                            print(f'{key} : {value}')
            elif opConsultar == 3:
                print('Digite o Fabricante: ')
                entrada = input('Digite o Fabricante Desejado: ')
                for produto in listaProdutos: # Selecionar cada dicionário da lista.
                    if (produto['Fabricante'] == entrada):
                        for key, value in produto.items():
                            print(f'{key} : {value}')
            elif opConsultar == 4:
                return
            else:
                print('Opção Inválida! Tente Novamente.')
                continue
        except ValueError:
            print('Erro. Digite um valor numérico por favor!')
# Fim da função consularProduto.

#  Início da função removerProduto.
def removerProduto():
    print('Exclusão de Produtos: ')
    entrada = int(input('Digite o Código Desejado: '))
    for produto in listaProdutos: # Selecionar cada dicionário da lista.
        if (produto['Código'] == entrada):
            listaProdutos.remove(produto)

# Fim da função removerProduto.

#  Início da main.
print('Bem-Vindo ao Controle de Estoque da Mercearia do Yago Silva Luiz - RU:4189430.')
regitroPoduto = 0
while True:
    try:
        opcao = int(input('Escolha a opção desejada:\n'
                          '1 - Cadastrar Produto\n'
                          '2 - Consultar Produto(s)\n'
                          '3 - Remover Produto\n'
                          '4 - Sair\n'
                          '>> '))
        if opcao == 1:
            regitroPoduto = regitroPoduto + 1
            cadastrarProduto(regitroPoduto)
        elif opcao == 2:
            consutarProduto()
        elif opcao == 3:
            removerProduto()
        elif opcao == 4:
            print('Programa Encerrado.')
            break
        else:
            print('Opção Inválida! Tente Novamente.')
            continue
    except ValueError:
        print('Erro. Digite um valor numérico por favor!')
#  Fim da main.
