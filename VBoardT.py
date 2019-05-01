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

vboardt_TIMEOUT = 4
vboardt_DIR = os.path.dirname(os.path.realpath(__file__))
vboardt_INFO = os.path.join(vboardt_DIR, "teacher_info")
vboardt_SUBMISSIONS_FOLDER = os.path.join(vboardt_DIR, 'Submissions')
if not os.path.exists(vboardt_SUBMISSIONS_FOLDER):
	os.mkdir(vboardt_SUBMISSIONS_FOLDER)

# ----------------------------------------------------------------------
def vboardt_Request(path, data, method='POST'):
	global vboardt_INFO
	try:
		with open(vboardt_INFO, 'r') as f:
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
		with urllib.request.urlopen(req, None, vboardt_TIMEOUT) as response:
			return response.read().decode(encoding="utf-8")
	except urllib.error.HTTPError as err:
		sublime.message_dialog("{0}".format(err))
	except urllib.error.URLError as err:
		sublime.message_dialog("{0}\nCannot connect to server.".format(err))
	print('Something is wrong')
	return None

# ------------------------------------------------------------------
class vboardtClearBroadcast(sublime_plugin.TextCommand):
	def run(self, edit):
		data = {'content': '', 'ext': '', 'clear': 'yes'}
		response = vboardt_Request('teacher_shares', data)
		if response is not None:
			sublime.message_dialog(response)

# ------------------------------------------------------------------
class vboardtShare(sublime_plugin.TextCommand):
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
		data = {'content': content, 'ext': ext, 'clear': 'no'}
		response = vboardt_Request('teacher_shares', data)
		if response is not None:
			sublime.message_dialog(response)

# ------------------------------------------------------------------
class vboardtReceive(sublime_plugin.ApplicationCommand):
	def run(self):
		response = vboardt_Request('teacher_receives', {})
		if response is not None:
			sub = json.loads(response)
			if sub['Len'] == 0:
				message = "There's no submission."
			elif sub['Content'] == '':
				message = 'Content is empty.'
			else:
				message = 'Sub id: {}. {} remaining.'.format(sub['Id'],sub['Len']-1)
				local_file = os.path.join(vboardt_SUBMISSIONS_FOLDER, str(sub['Id']))
				local_file += '.' + sub['Ext']
				with open(local_file, 'w', encoding='utf-8') as fp:
					fp.write(sub['Content'])
				if sublime.active_window().id() == 0:
					sublime.run_command('new_window')
				sublime.active_window().open_file(local_file)
			sublime.status_message(message)

# ------------------------------------------------------------------
class vboardtSetServerAddress(sublime_plugin.ApplicationCommand):
	def run(self):
		global vboardt_INFO
		try:
			with open(vboardt_INFO, 'r') as f:
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
				with open(vboardt_INFO, 'r') as f:
					info = json.loads(f.read())
			except:
				info = dict()
			if not addr.startswith('http://'):
				addr = 'http://' + addr
			info['Server'] = addr
			with open(vboardt_INFO, 'w') as f:
				f.write(json.dumps(info, indent=4))
			sublime.message_dialog('Server address is set to ' + addr)
		else:
			sublime.message_dialog("Server address cannot be empty.")

# ------------------------------------------------------------------

