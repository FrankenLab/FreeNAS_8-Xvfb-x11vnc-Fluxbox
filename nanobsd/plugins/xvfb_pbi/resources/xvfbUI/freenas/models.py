from django.db import models


class Xvfb(models.Model):
    """
    Django model describing every tunable setting for Xvfb
    """

#    MYTH_SERVICES = ( ('1','MythSetup'), ('2','MythBackend'), ('3', 'MythFrontend'), ('4','MythWelcome'))

    enable = models.BooleanField(default=False)
    x11_DISPLAY = models.CharField(max_length=500, default=':1', blank=True)
    xvfb_enable = models.BooleanField(default=True)
#    mythservices_list = models.CharField(max_length=12,
#	choices=MYTH_SERVICES,
#	help_text=("<span style=\"color: yellow;\"><b>Select MythSetup the first time!</b></span>")
	)
