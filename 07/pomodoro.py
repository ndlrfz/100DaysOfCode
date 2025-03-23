import time
import webbrowser

# how many pomo
# minutes
# break time
# complete

pomo_count = int(input("How many pomodoro and break:: "))
pomo_minutes = int(input("How much much time for each pomodoro - in minutes:: "))
pomo_break = int(input("Enter your break time in minutes:: "))

count = 0

while (count < pomo_count):
    print("Pomodoro started...")
    time.sleep(pomo_minutes * 60)
    print("Time to rest")
    webbrowser.open("https://www.youtube.com/watch?v=CNF5S8Kewzo")
    count += 1
