import psutil

def get_system_info():
    # Свободное место на диске (в байтах)
    disk_free = psutil.disk_usage('/').free
    # Размер своп-диска (в байтах)
    swap_size = psutil.swap_memory().total
    # Занятая оперативная память (в байтах)
    ram_used = psutil.virtual_memory().used
    # Список запущенных процессов
    running_processes = psutil.process_iter()

    print(f"Свободное место на диске: {disk_free} байт")
    print(f"Размер своп-диска: {swap_size} байт")
    print(f"Занятая оперативная память: {ram_used} байт")
    print("Запущенные процессы:")
    for process in running_processes:
        print(f"- {process.name()}")

if __name__ == "__main__":
    get_system_info()
