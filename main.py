import tingbot
import time
import requests
from tingbot import *
from src.website import Website
from src.views import *

current = {}
current['state'] = 0
current['payload_time'] = 0

# The name of the webhook
webhook_name = tingbot.app.settings['webhook']['name'].encode('ascii')
webhook_url = "http://webhook.tingbot.com/" + webhook_name

# Reset the webhook with an empty request
requests.post(webhook_url, data="||")

# Set up the sounds and generic environment
sound_up = Sound(tingbot.app.settings['sounds']['up'])
sound_down = Sound(tingbot.app.settings['sounds']['down'])

image_up = tingbot.app.settings['images']['up']
image_down = tingbot.app.settings['images']['down']
image_normal = tingbot.app.settings['images']['normal']

text_up = tingbot.app.settings['text']['up']
text_down = tingbot.app.settings['text']['down']
text_normal = tingbot.app.settings['text']['normal']

# Set up the default view object and render the screen
view_default = ViewDefault(screen)
view_default.render(image_normal, text_normal)

# Buttons just cancel sound
@left_button.press
@midleft_button.press
@midright_button.press
@right_button.press
def on_button_press():
    sound_down.stop()
    sound_up.stop()
    
# Set up the webhook
@webhook(webhook_name)
def on_webhook(data):
    website = Website(data)
    view_up = ViewUp(screen, website)
    view_down = ViewDown(screen, website)
    
    current['state']  = website.get_state()
    current['payload_time'] = time.time()
    
    if website.is_up():
        view_up.render(image_up, text_up)
        sound_up.play(False)
        sound_down.stop()
    elif website.is_down():
        view_down.render(image_down, text_down)
        sound_up.stop()
        sound_down.play(True)
    else:
        view_default.render(image_normal, text_normal)
        sound_up.stop()
        sound_down.stop()

@every(seconds = 1.0/30)
def loop():
    if not current['state'] == 1 and time.time() - current['payload_time'] > 10:
        view_default.render(image_normal, text_normal)

# Run the app
tingbot.run()
