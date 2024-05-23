import requests
import json
from twilio.rest import Client
from enter_location_info import EnterLocation, LOCATION_INFO_PATH
from enter_twilio_details import EnterTwilioCredentials, TWILIO_CRED_PATH
from tkinter import messagebox


def send_whatsapp_message():
    twilio_credentials = get_twilio_credentials()
    account_sid = twilio_credentials["account_sid"]
    auth_token = twilio_credentials["auth_token"]
    from_number = twilio_credentials["from"]
    to_number = twilio_credentials["to"]

    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_=from_number,
        body='Get your umbrella, it will rain today.',
        to=to_number
    )

    messagebox.showinfo(title="Message sent", message=f"Message {message.status}")


def get_twilio_credentials():
    # retrieve twilio credentials
    try:
        with open(TWILIO_CRED_PATH, 'r') as file:
            twilio_credentials = json.load(file)
        return twilio_credentials

    except FileNotFoundError:
        EnterTwilioCredentials()
        return get_twilio_credentials()


def get_params():
    # define parameters for request
    params = {
        "appid": "a4dffac7fd8f73aba5007011120cae43",
        "cnt": 4,
    }

    try:
        with open(LOCATION_INFO_PATH, 'r') as file:
            data = json.load(file)

        params["lat"] = data["lat"]
        params["lon"] = data["lon"]

        return params

    except FileNotFoundError:
        EnterLocation()
        return get_params()


def main():
    params = get_params()

    # get data from open weather map
    response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=params)
    response.raise_for_status()
    data = response.json()

    rain = False
    for forecast in data["list"]:
        print(forecast["dt_txt"])
        for weather in forecast["weather"]:
            print(weather["id"])
            if weather["id"] < 700:
                rain = True
                break
        if rain:
            send_whatsapp_message()
            break

    if not rain:
        messagebox.showinfo(title="Yay!", message="Looks like no rain today!")


if __name__ == "__main__":
    main()
