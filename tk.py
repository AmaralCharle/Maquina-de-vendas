import customtkinter as ctk
from tkinter import messagebox

class MaquinaVendas:
    def __init__(self, root):
        self.produtos = {
            'Refrigerante': 3.00,
            'Água': 1.50,
            'Salgadinho': 2.50,
            'Chocolate': 2.00
        }
        self.saldo = 0.0

        self.root = root
        self.root.title("Máquina de Vendas")
        self.root.geometry("600x400")  # Define o tamanho da janela

        # Configuração do estilo global
        ctk.set_appearance_mode("light")  # ou "dark"
        ctk.set_default_color_theme("blue")  # ou "green", "dark-blue", etc.

        # Título
        self.label_titulo = ctk.CTkLabel(root, text="Máquina de Vendas", font=("Arial", 24, 'bold'))
        self.label_titulo.pack(pady=20)

        # Saldo
        self.label_saldo = ctk.CTkLabel(root, text=f"Saldo: R$0.00", font=("Arial", 18))
        self.label_saldo.pack(pady=10)

        # Frame para produtos
        self.frame_produtos = ctk.CTkFrame(root)
        self.frame_produtos.pack(pady=10)

        self.buttons_produtos = []
        for produto, preco in self.produtos.items():
            button = ctk.CTkButton(self.frame_produtos, text=f"{produto} - R${preco:.2f}", command=lambda p=produto: self.escolher_produto(p))
            button.pack(fill='x', pady=5, padx=10)
            self.buttons_produtos.append(button)

        # Frame para inserir dinheiro
        self.frame_inserir_dinheiro = ctk.CTkFrame(root)
        self.frame_inserir_dinheiro.pack(pady=10)

        self.label_inserir = ctk.CTkLabel(self.frame_inserir_dinheiro, text="Inserir dinheiro:", font=("Arial", 14))
        self.label_inserir.pack(side='left', padx=10)

        self.entry_dinheiro = ctk.CTkEntry(self.frame_inserir_dinheiro, font=("Arial", 14))
        self.entry_dinheiro.pack(side='left', padx=10)

        self.button_inserir = ctk.CTkButton(self.frame_inserir_dinheiro, text="Inserir", command=self.inserir_dinheiro)
        self.button_inserir.pack(side='left', padx=10)

    def atualizar_saldo(self):
        self.label_saldo.configure(text=f"Saldo: R${self.saldo:.2f}")

    def inserir_dinheiro(self):
        try:
            valor = float(self.entry_dinheiro.get())
            if valor <= 0:
                raise ValueError("O valor deve ser positivo.")
            self.saldo += valor
            self.atualizar_saldo()
            self.entry_dinheiro.delete(0, ctk.END)
        except ValueError as e:
            messagebox.showerror("Entrada inválida", str(e))

    def escolher_produto(self, produto):
        preco = self.produtos[produto]
        if self.saldo >= preco:
            self.saldo -= preco
            self.atualizar_saldo()
            messagebox.showinfo("Compra realizada", f"Você comprou: {produto}\nTroco: R${self.saldo:.2f}")
            self.saldo = 0.0
        else:
            messagebox.showwarning("Saldo insuficiente", "Saldo insuficiente. Por favor, insira mais dinheiro.")

def main():
    root = ctk.CTk()
    app = MaquinaVendas(root)
    root.mainloop()

if __name__ == "__main__":
    main()
