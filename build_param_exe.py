import urllib.request
import subprocess


def give_latest_version():
    remote_version_url = "https://raw.githubusercontent.com/Faunas/accountant_ticket_testing/master/version.txt"
    try:
        with urllib.request.urlopen(remote_version_url) as response:
            remote_version = response.read().decode("utf-8").strip()
            print(f"Посдедняя версия: {remote_version}")
        return remote_version
    except Exception as e:
        print(f"Ошибка при проверке последней версии: {e}")


def main():
    version = give_latest_version()
    command = f"pyinstaller --noconfirm --onefile --console --name TEST_BUCH_UCHET_v{version} C:/Users/Max/PycharmProjects/accounting_sheet/version_json_in.py"

    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при выполнении компиляции: {e}")


if __name__ == '__main__':
    main()
