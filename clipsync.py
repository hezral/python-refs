#!/usr/bin/env python

import gtk

class Owner:
    def __init__(self):
        pass

class ClipSync:
    def __init__(self):
        self.clipboard = gtk.Clipboard(gtk.gdk.display_get_default(), "CLIPBOARD")
        self.clipboard.connect("owner-change", self.owner_change)

        self.primary = gtk.Clipboard(gtk.gdk.display_get_default(), "PRIMARY")
        self.primary.connect("owner-change", self.owner_change)
        self.self_owner = 0 # FIXME: how to look this up at start?

    def get_peer(self, clipboard):
        if clipboard == self.primary:
            return self.clipboard
        else:
            return self.primary

    def get_data(self, clipboard, store, info, owner):
        type = owner.targets[info]
        peer = self.get_peer(clipboard)
        content = peer.wait_for_contents(type)
        if content:
            data = content.data
        else:
            data = ""
        store.set(type, 8, data)

    def got_targets(self, clipboard, targets, info):
        targets = list(targets)
        targets.remove("TARGETS")

        owner = Owner()
        owner.targets = targets

        entries = [(targets[i],0,i) for i in range(len(targets))]
        peer = self.get_peer(clipboard)
        peer.set_data("owner", owner)
        peer.set_with_data(entries, self.get_data, None, owner)

    def owner_change(self, clipboard, event):
        print("%r owner change %r %r" % (clipboard, event.reason.value_nick, event.owner))

        ours = clipboard.get_data("owner")
        if ours and self.self_owner == 0:
            self.self_owner = event.owner

	if event.owner == self.self_owner:
	    return

	peer = self.get_peer(clipboard)
	if event.owner == 0 and peer.get_data("owner"):
	    peer.clear()
	    peer.set_data("owner", None)
        elif event.reason.value_nick == 'new-owner' and self.self_owner != event.owner:
            clipboard.request_targets(self.got_targets)


ClipSync()
gtk.main()
