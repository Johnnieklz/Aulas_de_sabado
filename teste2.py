import sqlite3

class Produto:
    def __init__(self, id, nome, preco, quantidade):
        self.id = id
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def exibir_informacoes(self):
        print(f"Nome: {self.nome}\nPreço: R$ {self.preco}\nQuantidade: {self.quantidade}")

class Banco_de_dados:
    def __init__(self, db_name="Banco_de_dados_produto.db"):
        self.conn = sqlite3.connect(db_name)
        self.criar_tabela()

    def criar_tabela(self):
        with self.conn:
            self.conn.execute("""
                CREATE TABLE IF NOT EXISTS itens (
                id INTEGER PRIMARY KEY,
                nome TEXT NOT NULL,
                preco REAL NOT NULL,
                quantidade INTEGER NOT NULL 
            )
            """)

    def inserir_item(self, item):
        with self.conn:
            self.conn.execute("""
                INSERT INTO itens (nome, preco, quantidade)
                VALUES (?, ?, ?)""", (item.nome, item.preco, item.quantidade))
        print("Item adicionado ao estoque com sucesso!")

    def editar_item(self, nome_item, nova_quantidade):
        with self.conn:
            cursor = self.conn.execute("UPDATE itens SET quantidade = ? WHERE nome = ?", (nova_quantidade, nome_item))
            if cursor.rowcount > 0:
                print(f"Quantidade do item {nome_item} atualizada com sucesso!")
            else:
                print(f"Item {nome_item} não encontrado!")

    def remover_item(self, nome_item):
        with self.conn:
            cursor = self.conn.execute("DELETE FROM itens WHERE nome = ?", (nome_item,))
            if cursor.rowcount > 0:
                print("Item removido do estoque com sucesso!") 
            else:
                print("Item não encontrado!")

    def exibir_itens(self):
        with self.conn:
            cursor = self.conn.execute("SELECT * FROM itens")
            itens = cursor.fetchall()
            if itens:
                for item in itens:
                    print(f"ID: {item[0]}\nNome: {item[1]}\nPreço: R$ {item[2]}\nQuantidade: {item[3]}\n")
            else:
                print("Nenhum item encontrado!")

    def interface(self):
        while True:
            print("\nEscolha uma opção:")
            print("1. Adicionar item.")
            print("2. Remover item.")
            print("3. Exibir itens.")
            print("4. Sair.")

            opcao = input("Digite o número da opção desejada: ")

            if opcao == "1":
                nome = input("Nome do item: ")
                preco = float(input("Preço do item: "))
                quantidade = int(input("Quantidade do item: "))
                item = Produto(None, nome, preco, quantidade)
                self.inserir_item(item)

            elif opcao == "2":
                nome_item = input("Digite o nome do item que será excluído: ")
                self.remover_item(nome_item)

            elif opcao == "3":
                self.exibir_itens()

            elif opcao == "4":
                print("Encerrando programa...")
                break

            else:  
                print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    estoque = Banco_de_dados()
    estoque.interface()
