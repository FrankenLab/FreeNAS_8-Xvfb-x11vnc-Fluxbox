from subprocess import Popen, PIPE
import os
import platform

xvfb_pbi_path = "/usr/pbi/xvfb-" + platform.machine()
xvfb_etc_path = os.path.join(xvfb_pbi_path, "etc")
xvfb_mnt_path = os.path.join(xvfb_pbi_path, "mnt")
xvfb_fcgi_pidfile = "/var/run/xvfb.pid"
xvfb_fcgi_wwwdir = os.path.join(xvfb_pbi_path, "www")
xvfb_control = "/usr/local/etc/rc.d/mysql-server"
xvfb_config = os.path.join(xvfb_etc_path, "xvfb.conf")
xvfb_icon = os.path.join(xvfb_pbi_path, "default.png")
xvfb_backgnd = os.path.join(xvfb_pbi_path, "xvfbbkgnd.png")
xvfb_oauth_file = os.path.join(xvfb_pbi_path, ".oauth")


def get_rpc_url(request):
    return 'http%s://%s/plugins/json-rpc/v1/' % ('s' if request.is_secure() \
            else '', request.get_host(),)


def get_xvfb_oauth_creds():
    f = open(xvfb_oauth_file)
    lines = f.readlines()
    f.close()

    key = secret = None
    for l in lines:
        l = l.strip()

        if l.startswith("key"):
            pair = l.split("=")
            if len(pair) > 1:
                key = pair[1].strip()

        elif l.startswith("secret"):
            pair = l.split("=")
            if len(pair) > 1:
                secret = pair[1].strip()

    return key, secret


xvfb_advanced_vars = {
    "set_cwd": {
        "type": "checkbox",
        "on": "-a",
        },
    "debuglevel": {
        "type": "textbox",
        "opt": "-d",
        },
    "debug_modules": {
        "type": "textbox",
        "opt": "-D",
        },
    "disable_mdns": {
        "type": "checkbox",
        "on": "-m",
        },
    "non_root_user": {
        "type": "checkbox",
        "on": "-y",
        },
    "ffid": {
        "type": "textbox",
        "opt": "-b",
        },
}
