from ftplib import FTP, error_perm

def create_directory(ftp, directory):
    """
    Prüft und erstellt ein Verzeichnis auf dem FTP-Server.
    """
    try:
        ftp.mkd(directory)
        # print(f"Created directory: {directory}")
    except error_perm as e:
        # Prüft, ob der Fehler bedeutet, dass das Verzeichnis bereits existiert
        if "550" in str(e):
            # print(f"Directory {directory} already exists.")
            pass
        else:
            raise e  # Wenn ein anderer Fehler auftritt, werfe die Exception weiter
    except Exception as e:
        print(f"Error creating directory {directory}: {str(e)}")

def ensure_directories_exist(ftp_host, ftp_user, ftp_password, directories):
    """
    Verbindet sich mit dem FTP-Server und prüft/erstellt die übergebenen Verzeichnisse.
    """
    try:
        with FTP(ftp_host) as ftp:
            ftp.login(user=ftp_user, passwd=ftp_password)
            for directory in directories:
                create_directory(ftp, directory)
    except Exception as e:
        print(f"Error connecting to FTP server or creating directories: {str(e)}")
