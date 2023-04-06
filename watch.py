import tkinter as tk
import time


class Stopwatch:
    def __init__(self, master):
        self.master = master
        master.title("Секундомер")
        self.seconds = 0
        self.is_running = False

        # Создаем метку, которая будет показывать время на секундомере
        self.label = tk.Label(master, text="00:00", font=("Arial", 30))
        self.label.pack(pady=20)

        # Создаем кнопки "Старт" и "Стоп"
        self.start_button = tk.Button(master, text="Старт", font=("Arial", 14), command=self.start)
        self.start_button.pack(padx=5, pady=5, side=tk.LEFT)

        self.stop_button = tk.Button(master, text="Стоп", font=("Arial", 14), command=self.stop)
        self.stop_button.pack(padx=5, pady=5, side=tk.LEFT)

        # Создаем кнопку "Сброс"
        self.reset_button = tk.Button(master, text="Сброс", font=("Arial", 14), command=self.reset)
        self.reset_button.pack(padx=5, pady=5, side=tk.LEFT)

    def start(self):
        self.is_running = True
        self.start_time = time.monotonic() - self.seconds

        # Запускаем цикл обновления времени на метке
        self.update()

    def update(self):
        if self.is_running:
            self.seconds = time.monotonic() - self.start_time
            minutes = int(self.seconds // 60)
            seconds = int(self.seconds % 60)
            time_str = f"{minutes:02}:{seconds:02}"
            self.label.config(text=time_str)
            self.master.after(1000, self.update)

    def stop(self):
        self.is_running = False

    def reset(self):
        self.is_running = False
        self.seconds = 0
        self.label.config(text="00:00")


root = tk.Tk()
my_stopwatch = Stopwatch(root)
root.mainloop()
