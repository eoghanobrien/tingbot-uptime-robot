# Uptime Tingbot

A simple Tingbot app, built to work with Uptime Robot, a website downtime monitoring tool. [Create a free account.](https://uptimerobot.com/signUp)

## Installation

Download the `uptime.tingapp` folder or clone this repository into a folder called `uptime.tingapp`.

```
$ git clone git@github.com:eoghanobrien/tingbot-uptime-robot.git
```

### Setup

[Create a free account at IFTTT](https://ifttt.com/join). [Then go to the Webhooks trigger page](https://ifttt.com//maker_webhooks) and click on the [settings page](https://ifttt.com/services/maker_webhooks/settings). Take note of your Webhook key.

Next, create a new applet. Click [My Applets](https://ifttt.com/my_applets) and then [New Applet](https://ifttt.com/create). Click `+this` and type `webhooks` and click the `Webhooks` button. Then click `Receive a web request`, enter your applet event name and click `Create Trigger`. Now click `+that`, type `webhooks` again and click the `Webhooks` button. This time, click `Make a web request`, enter `http://webhook.tingbot.com/{YOUR_CUSTOM_HOOK_NAME}` as the `URL`, set `Method` to `POST`, set `Content Type` to `text/plain` and set the `Body` to `{{Value1}}| {{Value2}}| {{Value3}}` and click `Create Action`. Then click `Finish`.

On to Uptime Robot.

[Create a free account at Uptime Robot](https://uptimerobot.com/signUp). Once you've signed up, go to `My Settings` and under `Alert Contacts`, click `Add Alert Contact`.

Next, select `Web-Hook` as the `Alert Contact Type`, give it a friendly name so you can easily remember it in future. Set the `URL to Notify` as the following IFTTT URL: 

```
https://maker.ifttt.com/trigger/{YOUR APPLET EVENT NAME}/with/key/{YOUR IFTTT WEBHOOK KEY}/?
```

Set the `POST Value` to:

```json
{
	"value1": "*monitorFriendlyName*",
	"value2": "*monitorURL*",
	"value3": "*alertType*"
}
```

Finally, check the box for `Send as JSON` and click `Save Changes`.

### Customize

The only customization that you **must** make is to add your webhoook name. You can also customize the sounds, images and text of your Uptime Tingbot app by creating a `settings.json` with the following settings:

```json
{
    "webhook": {
        "name": "{YOUR_CUSTOM_HOOK_NAME}"
    },
    "sounds": {
        "up": "sounds/up.wav",
        "down": "sounds/down.wav"
    },
    "images": {
        "normal": "images/status-default.png",
        "up": "images/status-up.png",
        "down": "images/status-down.png"
    },
    "text": {
        "normal": "All systems are functional",
        "up": "Up",
        "down": "Down"
    }
}
```

### Install

Open the app in the [Tingbot Tide app](http://docs.tingbot.com/tide/) and upload onto your Tingbot.