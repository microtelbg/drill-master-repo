'''
Created on Apr 6, 2016

@author: agnesastoyanova
'''
from distutils.core import setup
import py2exe

setup(windows = [{
          "script":"DrillMaster.py",
          "icon_resources": [(1, "DM.ico")],
          "dest_base":"DrillMaster"
          }]
      )
