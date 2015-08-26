# from wx.lib.pubsub import pub
#  
# class SomeReceiver(object):
#     def __init__(self):
#         pub.subscribe(self.__onObjectAdded, 'object.added')
#      
#     def __onObjectAdded(self,data, extra1, extra2=None):
#         print 'Object' , repr(data), 'is added'
#         print extra1
#         if extra2:
#             print extra2
#     
# #     def _Test(self):
# #         pub.subscribe(self.__onObjectAdded, 'object.test')
#  
# a = SomeReceiver()
# pub.sendMessage('object.added', data=42, extra1='hello')
# #pub.sendMessage('object.test')