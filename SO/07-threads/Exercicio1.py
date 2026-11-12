import threading
import time


def processamento(thread_id):
    time.sleep(0.5)
    print(f"Thread #{thread_id}")


def main():
    threads = []

    for i in range(5):
        thread = threading.Thread(target=processamento, args=(i,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


if __name__ == "__main__":
    main()
