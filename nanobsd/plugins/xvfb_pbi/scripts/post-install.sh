#!/bin/sh

XVFB_HOME=/usr/pbi/xvfb-`uname -m`
XVFB_USER=xvfb

env -i ${XVFB_HOME}/bin/python ${XVFB_HOME}/xvfbUI/manage.py syncdb --migrate --noinput

# IF `uname -m` .eq. amd64
mv ${XVFB_HOME}/lib_x64/libGL.so ${XVFB_HOME}/lib/
mv ${XVFB_HOME}/lib_x64/libGL.so.1 ${XVFB_HOME}/lib/
rm -rf ${XVFB_HOME}/lib_x64
rm ${XVFB_HOME}/lib*.so*

ldconfig -m ${XVFB_HOME}/lib
ldconfig -m ${XVFB_HOME}/lib/mysql
ldconfig -m ${XVFB_HOME}/lib/mysql/plugin
ldconfig -m ${XVFB_HOME}/lib/qt4/plugins

mv ${XVFB_HOME}/sbin_xvfb ${XVFB_HOME}/sbin/xvfb
chmod 755 ${XVFB_HOME}/sbin/xvfb

##########################
# INSTALL FONTS FOR X11
##########################

mkdir -p /usr/local/lib/X11/fonts
#ln -sf /usr/local/lib/X11/fonts ${XVFB_HOME}/lib/X11/fonts
(cd /usr/local/lib/X11/fonts ; cp -a ${XVFB_HOME}/fonts/* .)

mkdir -p /usr/local/etc/fonts
cp -a ${XVFB_HOME}/fonts.conf /usr/local/etc/fonts/fonts.conf
${XVFB_HOME}/bin/fc-cache -f

rm -rf ${XVFB_HOME}/fonts

pw groupadd ${XVFB_USER}
pw useradd ${XVFB_USER} -g ${XVFB_USER} -G wheel -s /bin/sh -w none -d ${XVFB_HOME}/etc/home/xvfb
mv /root/.xvfb /root/.xvfb_OLD
ln -sf ${XVFB_HOME}/etc/home/xvfb /root/.xvfb
mkdir -p ${XVFB_HOME}/etc/home/xvfb/.fluxbox

# Need to create home directory
#pw useradd ${XVFB_USER} -g ${XVFB_USER} -G wheel -s /bin/sh -d ${XVFB_HOME}/etc/home/xvfb -w none
#chown -R ${XVFB_USER}:${XVFB_USER} ${XVFB_HOME}/etc/home/xvfb

##########################
# CLEANUP
##########################

#echo $JAIL_IP"	"`hostname` >> /etc/hosts
#echo 'mysql-server_flags=""' >> ${XVFB_HOME}/etc/rc.conf
#echo 'mysql-server_flags=""' >> /etc/rc.conf
