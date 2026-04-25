import psutil

battery = psutil.sensors_battery()
percent = battery.percent
print(f"Battery at: {percent}%")
