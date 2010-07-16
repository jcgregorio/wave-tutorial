import logging

from waveapi import robot
from waveapi import events
from waveapi import appengine_robot_runner

def OnDocumentChanged(event, wavelet):
  event.blip.all(":(").replace(":)", [('style/fontWeight', 'bold')])

if __name__=='__main__':
  logging.info("Creating robot")

  myrobot = robot.Robot("Greeter",
      image_url='http://google-wave-resources.googlecode.com/svn/trunk/samples/extensions/robots/python/conference-bot/img/avatar.png',
      profile_url='')
  myrobot.register_handler(events.DocumentChanged, OnDocumentChanged)
  appengine_robot_runner.run(myrobot, debug=True)

