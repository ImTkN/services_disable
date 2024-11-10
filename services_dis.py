import subprocess

# Список служб, которые потенциально можно отключить (обновите по необходимости)
services_to_disable = [
    "Fax",  # Факсимильная служба
    "MapsBroker",  # Служба скачивания карт (не нужна без приложений Карт)
    "RetailDemo",  # Демо-режим розничной торговли
    "XblGameSave",  # Сохранения Xbox Live игр
    "XboxGipSvc",  # Xbox Accessory Management Service
    "WSearch",  # Индексация поиска
    "DiagTrack",  # Connected User Experiences and Telemetry
    "AssignedAccessManager",

]


def disable_service(service_name):
    """
    Функция для остановки и отключения службы Windows.
    """
    try:
        # Остановить службу
        subprocess.run(["sc", "stop", service_name], check=True)
        print(f"Служба {service_name} остановлена.")

        # Отключить службу
        subprocess.run(["sc", "config", service_name, "start=", "disabled"], check=True)
        print(f"Служба {service_name} отключена.")

    except subprocess.CalledProcessError as e:
        print(f"Не удалось изменить состояние службы {service_name}: {e}")


# Отключаем все службы из списка
for service in services_to_disable:
    disable_service(service)

# Запрос подтверждения выхода
while True:
    user_input = input("Вы хотите выйти из приложения? (Y/N): ").strip().upper()
    if user_input == 'Y':
        print("Выход из приложения.")
        break
    elif user_input == 'N':
        print("Остаемся в приложении. Если нужно повторно отключить службы, перезапустите программу.")
        break
    else:
        print("Неверный ввод. Пожалуйста, введите 'Y' для выхода или 'N' для продолжения.")
