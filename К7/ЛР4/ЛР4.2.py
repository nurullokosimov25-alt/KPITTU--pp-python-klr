import shutil, zipfile, logging, os

logging.basicConfig(
    filename="backup.log",
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)

def backup(file_name):
    try:
        if not os.path.exists(file_name):
            raise FileNotFoundError("Файл не найден")

        shutil.copy(file_name, "copy_" + file_name)
        logging.info("Файл скопирован")

        with zipfile.ZipFile("backup.zip", "w") as z:
            z.write(file_name)
        logging.info("Архив создан")

    except Exception as e:
        logging.error(e)
