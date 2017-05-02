# PyDia Simple Scale
# Copyright (c) 2003, Hans Breuer <hans@breuer.org>
#
# Experimental scaleing (selected) Objects via property api
#
# Known Issues:
#  - HANDLE_NON_MOVEABLE ?
#  - bezier control points
#  - unsizeable objects (or sizeable via multiple text size changing, e.g. UML Class)
#

#  This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

import dia, string 

class CSimusol :
	def __init__(self, d, data) :
		import os,subprocess, time
		filename = dia.active_display().diagram.filename
		sFilename ='%s' % (filename)
		subprocess.Popen(['xterm','-hold','-title','Simular','-e','simusol',sFilename])
		time.sleep(10)
def log_to_file(message, content=""):
    with open("/home/lorena/output.txt", "a") as file:
        file.write("message:: %s\n" % message)
        file.write("content:: %s\n" % content)
        file.write("\n\n")

def simu(data, flags) :
	dlg = CSimusol(dia.active_display().diagram, data)

dia.register_action ("SimusolScripts", "Simular",
		     "/DisplayMenu/Simusol/SimusolScript", 
		     simu)
