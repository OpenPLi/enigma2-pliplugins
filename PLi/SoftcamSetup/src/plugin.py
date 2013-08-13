from . import _
from Plugins.Plugin import PluginDescriptor
from Components.config import config, ConfigSubsection, ConfigYesNo

config.misc.softcam_setup = ConfigSubsection()
config.misc.softcam_setup.extension_menu = ConfigYesNo(default = True)

def main(session, **kwargs):
	import Sc
	session.open(Sc.ScSelection)

def menu(menuid, **kwargs):
	if menuid == "cam":
		return [(_("Softcam setup..."), main, "softcam_setup", 45)]
	return []

def Plugins(**kwargs):
	list = [(PluginDescriptor(name="Softcam setup", description="Lets you configure your softcams", where = PluginDescriptor.WHERE_MENU, fnc = menu))]
	if config.misc.softcam_setup.extension_menu.value:
		list.append(PluginDescriptor(name="Softcam setup", description="Lets you configure your softcams", where = PluginDescriptor.WHERE_EXTENSIONSMENU, fnc=main))
	return list
