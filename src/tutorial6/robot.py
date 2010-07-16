import logging

from waveapi import robot
from waveapi import events
from waveapi import element 
from waveapi import appengine_robot_runner

def OnSelfAdded(event, wavelet):
  blip = wavelet.root_blip
  blip.append(element.Input("add1", "2"))
  blip.append(element.Input("add2", "3"))
  blip.append(element.Button("plus", "+"))
  blip.append(element.Input("sum", ""))

def OnButtonClicked(event, wavelet):
  blip = wavelet.root_blip 
  sum = int(blip.first(element.Input, name="add1").get("value")) + int(
      blip.first(element.Input, name="add2").get("value"))
  blip.first(element.Input, name="sum").update_element({'value': str(sum)})


if __name__=='__main__':
  logging.info("Creating robot")

  myrobot = robot.Robot("Greeter",
      image_url='http://google-wave-resources.googlecode.com/svn/trunk/samples/extensions/robots/python/conference-bot/img/avatar.png',
      profile_url='')
  myrobot.register_handler(events.WaveletSelfAdded, OnSelfAdded)
  myrobot.register_handler(events.FormButtonClicked, OnButtonClicked)

  appengine_robot_runner.run(myrobot, debug=True)

