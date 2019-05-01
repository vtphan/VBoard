#
# Author: Vinhthuy Phan, 2018
#

import sublime, sublime_plugin
import urllib.parse
import urllib.request
import os
import json
import socket
import webbrowser
import random
import re

vboards_TIMEOUT = 4
vboards_DIR = os.path.dirname(os.path.realpath(__file__))
vboards_INFO = os.path.join(vboards_DIR, "student_info")
vboards_BROADCAST_FOLDER = os.path.join(vboards_DIR, 'Broadcasts')
if not os.path.exists(vboards_BROADCAST_FOLDER):
	os.mkdir(vboards_BROADCAST_FOLDER)

# ----------------------------------------------------------------------
def vboards_Request(path, data, method='POST'):
	global vboards_INFO
	try:
		with open(vboards_INFO, 'r') as f:
			info = json.loads(f.read())
	except:
		info = dict()
	if 'Server' not in info or info['Server'].strip()=='':
		sublime.message_dialog("Please set server address.")
		return None

	url = urllib.parse.urljoin(info['Server'], path)
	load = urllib.parse.urlencode(data).encode('utf-8')
	req = urllib.request.Request(url, load, method=method)
	try:
		with urllib.request.urlopen(req, None, vboards_TIMEOUT) as response:
			return response.read().decode(encoding="utf-8")
	except urllib.error.HTTPError as err:
		sublime.message_dialog("{0}".format(err))
	except urllib.error.URLError as err:
		sublime.message_dialog("{0}\nCannot connect to server.".format(err))
	print('Something is wrong')
	return None

# ------------------------------------------------------------------
class vboardsShare(sublime_plugin.TextCommand):
	def run(self, edit):
		fname = self.view.file_name()
		if fname is None:
			sublime.message_dialog('Error: file is empty.')
			return
		beg, end = self.view.sel()[0].begin(), self.view.sel()[0].end()
		content = self.view.substr(sublime.Region(beg,end))
		ext = 'txt'
		items = fname.rsplit('.',1)
		if len(items)==2:
			ext = items[1]
		data = {'content': content, 'ext': ext}
		response = vboards_Request('student_shares', data)
		if response is not None:
			sublime.message_dialog(response)

# ------------------------------------------------------------------
class vboardsReceive(sublime_plugin.ApplicationCommand):
	def run(self):
		response = vboards_Request('student_receives', {})
		if response is not None:
			sub = json.loads(response)
			if sub['Content'] == '':
				sublime.message_dialog('There is no message.')
			else:
				local_file = os.path.join(vboards_BROADCAST_FOLDER, 'virtual_board.')
				local_file += sub['Ext']
				with open(local_file, 'w', encoding='utf-8') as fp:
					fp.write(sub['Content'])
				if sublime.active_window().id() == 0:
					sublime.run_command('new_window')
				sublime.active_window().open_file(local_file)

# ------------------------------------------------------------------
class vboardsSetServerAddress(sublime_plugin.ApplicationCommand):
	def run(self):
		global vboards_INFO
		try:
			with open(vboards_INFO, 'r') as f:
				info = json.loads(f.read())
		except:
			info = dict()
		if 'Server' not in info:
			info['Server'] = ''
		if sublime.active_window().id() == 0:
			sublime.run_command('new_window')
		sublime.active_window().show_input_panel("Set server address.  Press Enter:",
			info['Server'],
			self.set,
			None,
			None)

	def set(self, addr):
		addr = addr.strip()
		if len(addr) > 0:
			try:
				with open(vboards_INFO, 'r') as f:
					info = json.loads(f.read())
			except:
				info = dict()
			if not addr.startswith('http://'):
				addr = 'http://' + addr
			info['Server'] = addr
			with open(vboards_INFO, 'w') as f:
				f.write(json.dumps(info, indent=4))
			sublime.message_dialog('Server address is set to ' + addr)
		else:
			sublime.message_dialog("Server address cannot be empty.")

# ------------------------------------------------------------------

