#!/bin/sh
# PBI building script
# This will run after your port build is complete
##############################################################################

mythtv_pbi_path=/usr/pbi/mythtv-$(uname -m)/

find ${mythtv_pbi_path}/lib -iname "*.a" -delete
#rm -rf ${mythtv_pbi_path}/include
rm -rf ${mythtv_pbi_path}/share/doc
rm -rf ${mythtv_pbi_path}/share/emacs
rm -rf ${mythtv_pbi_path}/share/examples
rm -rf ${mythtv_pbi_path}/share/gettext
rm -rf ${mythtv_pbi_path}/share/gtk-doc/html/gi
rm -rf ${mythtv_pbi_path}/man
