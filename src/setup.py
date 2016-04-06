'''
Created on Apr 6, 2016

@author: agnesastoyanova
'''
from distutils.core import setup

setup(windows = [{
          "script":"DrillMaster.py",
          "icon_resources": [(1, "/image/DM.ico")],
          "dest_base":"DrillMaster"
          }]
      )
