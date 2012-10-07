import os
import platform
import pwd

from django.utils.translation import ugettext_lazy as _

from dojango import forms
from xvfbUI.freenas import models, utils


class XvfbForm(forms.ModelForm):

    class Meta:
        model = models.Xvfb
        widgets = {
            'x11_DISPLAY': forms.widgets.TextInput(),
        }
        exclude = (
            'enable',
            )

    def __init__(self, *args, **kwargs):
        self.jail = kwargs.pop('jail')
        super(XvfbForm, self).__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        obj = super(XvfbForm, self).save(*args, **kwargs)

        rcconf = os.path.join(utils.xvfb_etc_path, "rc.conf")
        with open(rcconf, "w") as f:
            if obj.enable:
                f.write('xvfb_enable="YES"\n')

            #xvfb_flags = ""
            #for value in advanced_settings.values():
            #    xvfb_flags += value + " "
            #f.write('xvfb_flags="%s"\n' % (xvfb_flags, ))

        os.system(os.path.join(utils.xvfb_pbi_path, "tweak-rcconf"))


        try:
            os.makedirs("/var/cache/Xvfb")
            os.chown("/var/cache/Xvfb", *pwd.getpwnam('xvfb')[2:4])
        except Exception:
            pass

        with open(utils.xvfb_config, "w") as f:
            f.write("[general]\n")
            f.write("web_root = /usr/pbi/xvfb-%s/etc/home/xvfb\n" % (
                platform.machine(),
                ))
            f.write("db_type = %s\n" % ("sqlite3", ))
            f.write("db_params = %s\n" % ("/var/cache/Xvfb", ))
            f.write("Xvfb_Enable= %d\n" % (obj.xvfb_enable, ))
            f.write("XvfbService= %s\n" % (obj.xvfbservices_list, ))
            f.write("X11_Display= %s\n" % (obj.x11_DISPLAY, ))
            f.write("runas = %s\n" % ("xvfb", ))
