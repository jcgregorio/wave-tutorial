import logging

from waveapi import robot
from waveapi import events
from waveapi import appengine_robot_runner

def OnSelfAdded(event, wavelet):
  wavelet.reply("Hello Everyone!")

if __name__=='__main__':
  logging.info("Creating robot")

  myrobot = robot.Robot("Greeter",
      image_url='http://google-wave-resources.googlecode.com/svn/trunk/samples/extensions/robots/python/conference-bot/img/avatar.png',
      profile_url='')
  myrobot.register_handler(events.WaveletSelfAdded, OnSelfAdded)
  appengine_robot_runner.run(myrobot, debug=True)

