import logging

from waveapi import robot
from waveapi import events
from waveapi import element 
from waveapi import appengine_robot_runner

def OnGadgetChanged(event, wavelet):
  gadget = wavelet.root_blip.first(element.Gadget).value()
  add1 = gadget.get('add1')
  add2 = gadget.get('add2')
  sum = gadget.get('sum')
  wavelet.reply("Look at that! %s + %s = %s" % (add1, add2, sum))

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

