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
		return [(_("Softcam setup..."), main, "softcam_setup", -1)]
	return []

def Plugins(**kwargs):
	name = _("Softcam setup")
	description = _("Lets you configure your softcams")
	list = [(PluginDescriptor(name=name, description=description, where = PluginDescriptor.WHERE_MENU, fnc = menu))]
	if config.misc.softcam_setup.extension_menu.value:
		list.append(PluginDescriptor(name=name, description=description, where = PluginDescriptor.WHERE_EXTENSIONSMENU, fnc=main))
	return list
