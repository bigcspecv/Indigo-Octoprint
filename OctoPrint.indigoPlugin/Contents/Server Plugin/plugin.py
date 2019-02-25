

# Library imports
from lib.octoPrintServiceResponse import OPSResponse
from lib import octoPrintServiceV4 as ops



class Plugin(indigo.PluginBase):
    def __init__(self,pluginId,pluginDisplayName,pluginVersion,pluginPrefs):
        indigo.PluginBase.__init__(self,pluginId,pluginDisplayName,pluginVersion,pluginPrefs)

    def __del__(self):
        indigo.PluginBase.__del__(self)

    def startup(self):
        self.logger.info(u"Startup called")
        ops.hostname = self.pluginPrefs["hostname"]
        ops.apiKey = self.pluginPrefs["apiKey"]
        for pref,value in self.pluginPrefs.iteritems():
            self.logger.info(u"{0}:{1}".format(pref,value))

    def shutdown(self):
        self.logger.info(u"Shutdown called")

    def closedPrefsConfigUi(self, valuesDict, userCanceled):
        self.logger.info(u"apiKey: {}".format(valuesDict["apiKey"]))
        self.logger.info(u"userCanceled: {}".format(userCanceled))