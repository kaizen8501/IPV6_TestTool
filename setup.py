from distutils.core import setup
import py2exe, sys, os
from glob import glob
import jpath

sys.argv.append('py2exe')
#sys.path.append("C:\Program Files (x86)\Microsoft Visual Studio 10.0\VC\redist\x86\Microsoft.VC100.CRT")
#"packages":['wx.lib.pubsub']}},


# setup(
# 	windows = [{'script':'S2E_TestTool.py'}],
# 	options = {'py2exe':{
# 			   'bundle_files':1,
# 			   'packages': ['wx.lib.pubsub','pubsub','wx','serial','threading','tcpServer'],
# 			   'includes':["wx.lib.pubsub.*","wx.lib.pubsub.core.*", "wx.lib.pubsub.core.arg1.*" ],
# 				"excludes":["MSVCP90.dll"],
# 				"optimize":0
# 			   }},
# 	zipfile = None,
# )


setup(
	windows = [{'script':'S2E_TestTool.py'}],
	options = {'py2exe':{
			   'bundle_files':1,
			   'packages': ['wx.lib.pubsub']
			   }},
	zipfile = None,
)
