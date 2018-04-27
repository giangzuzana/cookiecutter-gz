import {{cookiecutter.utils_script}} as us
import time

start = time.strftime("%Y%m%d-%H%M%S")      			# timestamp

print("Hello from, {{cookiecutter.greeting_recipient}}!")

print us.run_time(start)
