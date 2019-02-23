class Plugin(indigo.PluginBase):
    def __init__(self,pluginId,pluginDisplayName,pluginVersion,pluginPrefs):
        indigo.PluginBase.__init__(self,pluginId,pluginDisplayName,pluginVersion,pluginPrefs)

    def __del__(self):
        indigo.PluginBase.__del__(self)

    def startup(self):
        indigo.server.log(u"Startup called")

    def shutdown(delf):
        indigo.server.log(u"Shutdown called")
