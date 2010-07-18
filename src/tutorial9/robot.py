import logging

from waveapi import robot
from waveapi import events
from waveapi import element 
from waveapi import appengine_robot_runner

from google.appengine.api import urlfetch

def OnGadgetChanged(event, wavelet):
  gadget = wavelet.root_blip.first(element.Gadget).value()
  resp = urlfetch.fetch("http://oeis.org/classic/?p=1&n=1&fmt=3&q=" + gadget.get('numbers'))
  if resp.status_code == 200:
    content = resp.content
    lines = []
    for line in content.split("\n"):
      if line.startswith(" "):
        lines[-1] = lines[-1] + line
      else:
        lines.append(line)
    for line in lines:
      if line.startswith("%N "):
        token, id, description = tuple(line.split(" ", 2))
        wavelet.reply("Did you know that " + gadget.get('numbers') + " appears in the sequence: " + " ".join([s for s in description.split(" ") if s]))

def OnSelfAdded(event, wavelet):
  blip = wavelet.root_blip
  blip.append(element.Gadget("http://jcgbot.appspot.com/static/gadget-final.xml"))

if __name__=='__main__':
  logging.info("Creating robot")

  myrobot = robot.Robot("Greeter",
      image_url='http://google-wave-resources.googlecode.com/svn/trunk/samples/extensions/robots/python/conference-bot/img/avatar.png',
      profile_url='')
  myrobot.register_handler(events.WaveletSelfAdded, OnSelfAdded)
  myrobot.register_handler(events.GadgetStateChanged, OnGadgetChanged)

  appengine_robot_runner.run(myrobot, debug=True)

