import logging

from waveapi import robot
from waveapi import events
from waveapi import appengine_robot_runner

def OnSelfAdded(event, wavelet):
  wavelet.reply("Hello Everyone!")

def OnBlipCreated(event, wavelet):
  wavelet.reply("Horray!")

if __name__=='__main__':
  logging.info("Creating robot")

  myrobot = robot.Robot("Greeter",
      image_url='http://google-wave-resources.googlecode.com/svn/trunk/samples/extensions/robots/python/conference-bot/img/avatar.png',
      profile_url='')
  myrobot.register_handler(events.WaveletSelfAdded, OnSelfAdded)
  myrobot.register_handler(events.WaveletBlipCreated, OnBlipCreated)
  appengine_robot_runner.run(myrobot, debug=True)

