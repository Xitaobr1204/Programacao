import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import os

class EmailMarketing:
    def __init__(self, smtp_server, smtp_port, smtp_username, smtp_password):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.smtp_username = smtp_username
        self.smtp_password = smtp_password
        self.contatos = []

    def adicionar_contato(self, nome, email):
        self.contatos.append({"nome": nome, "email": email})

    def enviar_email(self, assunto, corpo, anexo_imagem=None):
        for contato in self.contatos:
            msg = MIMEMultipart()
            msg['From'] = self.smtp_username
            msg['To'] = contato["email"]
            msg['Subject'] = assunto

            corpo_email = f"Olá {contato['nome']},\n\n{corpo}"
            msg.attach(MIMEText(corpo_email, 'plain'))

            if anexo_imagem:
                with open(anexo_imagem, 'rb') as img_file:
                    msg.attach(MIMEImage(img_file.read(), name=os.path.basename(anexo_imagem)))

            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.smtp_username, self.smtp_password)
                server.sendmail(self.smtp_username, contato["email"], msg.as_string())

    def obter_relatorio(self):
        pass

def main():
    smtp_server = 'smtp.example.com'
    smtp_port = 587
    smtp_username = 'seu_email@example.com'
    smtp_password = 'sua_senha'

    programa_email = EmailMarketing(smtp_server, smtp_port, smtp_username, smtp_password)

    programa_email.adicionar_contato("João", "joao@example.com")
    programa_email.adicionar_contato("Maria", "maria@example.com")

    assunto = "Oferta Especial!"
    corpo = "Confira nossa oferta exclusiva para você."
    anexo_imagem = "caminho/para/sua/imagen.jpg"
    programa_email.enviar_email(assunto, corpo, anexo_imagem)

    relatorio = programa_email.obter_relatorio()
    print(relatorio)

if __name__ == "__main__":
    main()