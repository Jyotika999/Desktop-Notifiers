import time
from plyer import notification


if __name__ == "__main__":
	while True:
		notification.notify(
			title = "Time to Get Hydrated !!",
			message = " You have been working so long, now its the time to make yourself healthier, Now get up from your Laptop and Drink a Glass of Water.",
			app_icon = "",
			timeout = 2

         )
		time.sleep(6)


