from queue import Queue
import time

# Створити чергу заявок
request_queue = Queue() 

class Order():
    def __init__(self, id):
        self.id = id

global_queue_id_counter = 1

def generate_request():
    global global_queue_id_counter
# Створити нову заявку
    new_order = Order(global_queue_id_counter)
    global_queue_id_counter += 1
# Додати заявку до черги
    request_queue.put(new_order)

def process_request():
    # Якщо черга не пуста
    if not request_queue.empty():
        # Видалити заявку з черги
        order = request_queue.get()
        # Обробити заявку
        print(f'Order № {order.id} is processed')
        time.sleep(1)
    else:
        #Вивести повідомлення, що черга пуста
        print("Queue is empty")

def main():
    try:
        while True:
            generate_request()
            process_request()
    # завершення через комбінацію "Ctrl+C"
    except KeyboardInterrupt:
        print("Application processing is stopped")

if __name__ == "__main__":
    main()