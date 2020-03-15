
import ctypes

import gi

gi.require_version('Gtk', '3.0')
gi.require_version('GIRepository', '2.0')

from gi.repository import GIRepository
from gi.repository import Gtk


# Load the libraries we need via GIRepository
def _get_shared_library(n):
	repo = GIRepository.Repository.get_default()
	return repo.get_shared_library(n).split(',')[0]

libgtk = ctypes.CDLL(_get_shared_library('Gtk'))
libgdk = ctypes.CDLL(_get_shared_library('Gdk'))

# Get C function
def c_func(dll, name, args, res=None):
	fn = getattr(dll, name)
	fn.restype = res
	fn.argtypes = args
	return fn

def atom_p(name):
	return libgdk.gdk_atom_intern_static_string(name, False)

print("---- clipboard ----")

clipboard = libgtk.gtk_clipboard_get(atom_p(b'CLIPBOARD'))
assert clipboard != 0

# Test passing clipboard pointer works
gtk_clipboard_set_text = c_func(libgtk, 'gtk_clipboard_set_text', (ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint))

gtk_clipboard_wait_for_text = c_func(libgtk, 'gtk_clipboard_wait_for_text',(), res=ctypes.c_char_p)

gtk_clipboard_set_text(clipboard, b'Test 123', len(b'Test 123'))
print("Set text")

text = gtk_clipboard_wait_for_text(clipboard)
print("TEXT>", text, type(text))
assert text == b'Test 123'

# print("----- target entry list ----")

# targetentrylist = libgtk.gtk_target_list_new(None, 0)
# libgtk.gtk_target_list_add(
# 	targetentrylist,
# 	atom_p(b'text/plain'),
# 	0,
# 	9,
# )

# gtk_target_list_find = c_func(libgtk, 'gtk_target_list_find',
# 						(ctypes.c_void_p, ctypes.c_void_p), res=ctypes.c_bool)

# ok = gtk_target_list_find(targetentrylist, atom_p(b'text/plain'), None)
# print("FOUND TARGET:", ok)
# assert ok

# print("---- functions and set_with_data ----")

# GetFuncType = ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)
# def get_func(clipboard, selection, info, data):
# 	print("GET %r" % ((clipboard, selection, info, data),))
# 	libgtk.gtk_selection_data_set_text(selection, b'Test 456', len(b'Test 456'))

# ClearFuncType = ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p)
# def clear_func(clipboard, data):
# 	print("CLEAR %r" % ((clipboard, data),))

# c_get_func = GetFuncType(get_func)
# c_clear_func = ClearFuncType(clear_func)

# gtk_clipboard_set_with_data = c_func(libgtk, 'gtk_clipboard_set_with_data',
# 								(
# 									ctypes.c_void_p,
# 									ctypes.c_void_p,
# 									ctypes.c_uint,
# 									ctypes.c_void_p, #ctypes.POINTER(GetFuncType),
# 									ctypes.c_void_p, #ctypes.POINTER(ClearFuncType),
# 									ctypes.c_void_p
# 								),
# 								res=ctypes.c_bool)


# user_data = "userdata 123"
# ok = gtk_clipboard_set_with_data(
# 	clipboard,
# 	targetentrylist,
# 	1,
# 	c_get_func,
# 	c_clear_func,
# 	user_data
# )
# print(">>>", ok)
# assert ok


# gtk_clipboard_wait_for_contents = c_func(libgtk, 'gtk_clipboard_wait_for_contents',
# 									(ctypes.c_void_p, ctypes.c_void_p), res=ctypes.c_void_p)

# data = gtk_clipboard_wait_for_contents(clipboard, atom_p(b'text/plain'))
# print(">>>>", data)

# text = gtk_clipboard_wait_for_text(clipboard)
# print("TEXT>", text)
# assert text == b'Test 456'


# PS need global cache for data so it will not get garbage collected before "clear"