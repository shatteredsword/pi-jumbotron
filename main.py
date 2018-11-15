#!/usr/bin/env python3
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MyWindow(Gtk.Window):
	def __init__(self):
		Gtk.Window.__init__(self, title="Hello World")
		self.label = Gtk.Label("00:00")
		self.label.set_markup("<span font='120.5'>waddup</span>")
		self.add(self.label)

win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.fullscreen()
win.show_all()
Gtk.main()