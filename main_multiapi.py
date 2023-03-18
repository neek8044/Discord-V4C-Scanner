import random
import string
import requests
import colorama
import datetime

import discord
from dhooks import Webhook


## CONFIGURATION
API_VERS = [6, 7, 8, 9]
DISPLAY_PROCESSES = False
WEBHOOK_NAME = "V4C Scanner"
STARTED_DESCRIPTION = "Started scanning process."
FOUND_DESCRIPTION = "Nitro Located!"
MESSAGE = "Link: "
loadchar = ">"
loadspace = "-"


colorama.init()
YELLOW = colorama.Fore.YELLOW
GREEN = colorama.Fore.GREEN
RESET = colorama.Fore.RESET

WEBHOOK = "https://discord.com/api/webhooks/xxxxx/xxxxx" # Paste channel webhook here


def sendWebhook(link):
    Found = discord.Color.from_rgb(255, 51, 255)
    webhook = WEBHOOK
    hook = Webhook(webhook)

    embed = discord.Embed(
        description = FOUND_DESCRIPTION,
        color=Found,
        timestamp = datetime.datetime.utcnow()
    )
    embed.set_author(name=WEBHOOK_NAME)
    embed.add_field(name=MESSAGE, value=str(link))
    hook.send(embed=embed)


def onReady(amount):
    onReady = discord.Color.from_rgb(37, 114, 68)

    webhook = WEBHOOK

    hook = Webhook(webhook)

    embed = discord.Embed(
        description = STARTED_DESCRIPTION,
        color = onReady,
        timestamp = datetime.datetime.utcnow(),
    )
    embed.set_author(name="V4C Scanner")
    embed.add_field(name="Amount: ", value=str(amount))
    hook.send(embed=embed)


print("DISCLAIMER: The core of this code was taken from V4C's replit which is now deleted. I have only tweaked it a bit so it is more usable.")

def get_num():
    while True:
        try:
            return int(input("Number of codes to generate: "))
        except:
            print("Invalid. Enter integers only.")
num = get_num()


onReady(num) # Send a webhook upon start | you can comment this out


# Generating text file
print("Generating...", end=" ")
file = open("./GeneratedNitroCodes.txt", "w", encoding="utf-8")
for i in range(num):
    y = "".join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(16))
    file.write("https://discord.gift/" + y + "\n")
file.close()
print("Done")


# Checking for valid codes

with open("./GeneratedNitroCodes.txt") as file:
    print("Checking...")
    i = 0
    for line in file:
        i += 1

		# Get nitro link
        nitro = line.strip("\n")
        for version in range(len(API_VERS)):
            url = f"https://discordapp.com/api/v{API_VERS[version]}/entitelemnts/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"
            r = requests.get(url)

		    # Check if nitro is valid
            if r.status_code == 200:
                print(str(i) + GREEN + " Found: " + nitro + RESET) if DISPLAY_PROCESSES else ...
                with open("./v4c_nitro_codes.txt", "w") as f:
                    f.write(nitro + "\n")
                    f.close()
                sendWebhook(nitro)
            else:
                print(str(i) + YELLOW + " Invalid: " + nitro + RESET) if DISPLAY_PROCESSES else print(f"{i}/{num} [{round(i / num * 100)}%] {loadchar*(version+1)}{loadspace*(len(API_VERS)-version-1)}", end="\r")
                continue

print("\nLooped through", num, "codes. If any were found they should be stored on a local file (v4c_nitro_codes.txt) or sent to your webhook.")
