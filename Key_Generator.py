import tkinter as tk
from tkinter import messagebox
import secrets

passwords = {}

def generate_password():
    try:
        length = int(entry_length.get())
        name = entry_name.get().strip()
        password = (secrets.token_urlsafe(length)).strip()

        if length == 0 or name == "":
            messagebox.showwarning("Erro", "⚠️ Nome é obrigatório e a senha não pode ter 0 caracteres.")
        elif name in passwords:
            messagebox.showwarning("Erro", "⚠️ Já existe uma senha com esse nome.")
        else:
            passwords[name] = password
            messagebox.showinfo("Sucesso", f"Senha salva!\n\nName: {name}\nPassword: {password}")
            entry_name.delete(0, tk.END)
            entry_length.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Erro", "Digite um número válido para o tamanho da senha.")

def delete_password():
    name = entry_name.get().strip()
    if name in passwords:
        del passwords[name]
        messagebox.showinfo("Sucesso", f"Senha de '{name}' excluída com sucesso!")
        entry_name.delete(0, tk.END)
    else:
        messagebox.showwarning("Erro", "⚠️ Esse nome não existe.")

def list_passwords():
    if not passwords:
        messagebox.showinfo("📒 Senhas Salvas", "⚠️ Nenhuma senha cadastrada.")
        return
    
    # cria nova janela
    top = tk.Toplevel(root)
    top.title("📒 Senhas Salvas")
    top.geometry("400x300")
    
    text_area = tk.Text(top, wrap="word")
    text_area.pack(expand=True, fill="both")

    # insere senhas
    for name, pwd in passwords.items():
        text_area.insert(tk.END, f"Name: {name} | Password: {pwd}\n")

    # deixa somente leitura (mas ainda dá pra copiar com Ctrl+C)
    text_area.config(state="disabled")

def quit_app():
    root.destroy()

# --- Janela Principal ---
root = tk.Tk()
root.title("Password Manager")
root.geometry("400x300")

tk.Label(root, text="Nome:").pack()
entry_name = tk.Entry(root, width=40)
entry_name.pack()

tk.Label(root, text="Número de caracteres:").pack()
entry_length = tk.Entry(root, width=10)
entry_length.pack()

tk.Button(root, text="Gerar Senha", command=generate_password).pack(pady=5)
tk.Button(root, text="Excluir Senha", command=delete_password).pack(pady=5)
tk.Button(root, text="Listar Senhas", command=list_passwords).pack(pady=5)
tk.Button(root, text="Sair", command=quit_app).pack(pady=5)

root.mainloop()