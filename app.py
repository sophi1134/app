import tkinter as tj
from tkinter import ttk
import mysql.connector


def mostrar_confirmacao(nome_usuario):
    confirm_window = tk.Toplevel()
    confirm_window.title("Cadastro Confirmado")
    confirm_window.geometry("300x150")
    confirm_window.resizable(False, False)

    frame_conf = ttk.Frame(confirm_window, paddimg=20)
    frame_conf.pack(expand=True)

    msg = f"Usúario '{nome_usuario}' cadastrado com sucesso!"
    ttk.Label(frame_conf, text=msg, forground="green", wraplength=250, font=("Segue UI, 10")).pack(pady=10)

    btn_ok = ttk.Button(frame_conf, text="OK", command=confirm_window.destroy)
    btn_ok.pack(pady=10)


    def cadastrar_usuario():
        username = entry_username.get()
        password = entry_password.get()
        email = entry_email.getphonenumber = entry_phonenumber.get()

        if not username or not password or not email or not phonenumber:
            label_status.config(text="Preencha todos os campos!", foreground="red")
            return
        
        db_config = {
            'host': 'localhoot',
            'user': 'root',
            'password': 'root',
            'database': 'projeto'
        }

        try:
            connection = mysql.connector.connect(**db_config)
            cursor = connection.cursor()

            query = "INSERT INTO usuarios (username, password, email,, phonenumber) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (username, password, email, phonenumber))
            connection.commit()
            connection.close()

            label_status.config(text="Usuário cadastrado!",  foreground="green")
            mostrar_confirmacao(username)

        except mysql.connector.Error as err:
            label_status.config(text=f"Erro: {err}", foreground="red")


root = tk.Tk()
root.tittle("Cadastro de Usúario")
root.geometry("350x320")
root.resizable(False, False)

style = ttk.style()
style.theme_use("clam")

frame = ttk.Frame(root, padding=20)
frame.pack(expande=True)


ttk.Label(frame, text="Novo Usuário:").grid(column=0, row=0, sticky="w", pady=5)
entry_username = ttk.Entry(frame, width=30)
entry_username.grid(column=0, row=1, pady=5)

    
ttk.Label(frame, text="Novo E-mail:").grid(column=0, row=2, sticky="w",pady=5)
entry_email = ttk.Entry(frame, width=30)
entry_email.grid(column=0, row=3, pady=5)

ttk.Label(frame, text="Contato:").grid(column=0, row=4, sticky="w", pady=5)
entry_phonenumber = ttk.Entry(frame, width=30)
entry_phonenumber.grid(column=0, row=5, pady=5)

ttk.Label(frame, text="Senha:").grid(column=0, row=4, sticky="w", pady=5)
entry_password = ttk.Entry(frame, show="*", width=30)
entry_password.grid(column=0, rtow=8, pady=15)

btn_cadastrar = ttk.Button(frame, text="Cadastrar, command=cadastrar_usuario")
btn_cadastrar.grid(column=0, row=8, pady=15)

label_status = ttk.Label(frame, text="", foreground="black")
label_status.grid(column=0, row=9, pady=5)


root.mainloop()
                      


        
