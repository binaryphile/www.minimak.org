---
title: Caveats
description:
---

Passwords
=========

One of the first things you'll learn when you try to adopt a new
keyboard layout is that you have an extremely hard time logging in
anywhere.  That's because your muscle memory no longer works for
passwords and since that is what you usually rely on, you now have to
spell everything out mentally.  Even then, it still usually ends up
wrong because you can't see any mistakes you're making.  This can be
very frustrating until you are proficient with the new layout.

This is a good reason to go with the recommended [PKL] until you are
proficient at Minimak.  PKL allows you to turn the Minimak layout on and
off with a hotkey.  Just hit both Alt keys together and it will
suspend Minimak, putting you back in QWERTY.  Handle your login, then
hit both Alts again to toggle back to Minimak.  You'll want to do this
whenever you deal with passwords.

Creating Passwords
------------------

You especially don't want to use Minimak to create new passwords until
you are 100% accurate.  That's because learning a new layout
(temporarily) makes you mistype letters in a consistent and reproducible
fashion.  If you do try to make passwords, you will typically end up
with a password that's good enough to get most systems to accept it, since
you can type it the same way twice, but isn't the password you thought
it was because you couldn't see your (consistently) mistyped letters.

Even when you're fairly confident of your new typing skills, it's a good
idea to type new passwords into a text editor first, then cut and paste
them into the site or application that needs it.

Logging In
----------

Another thing to note is that the different methods of changing layouts
don't always work for your system's bootup login prompt.

If you use a method that only remaps your keys after you login, you'll
need to remember to type your system login password in QWERTY in order
to log into your account.  This is true for PKL and layouts created with
MKLC, since they are only enabled after you log in.

If you use the same password for sites or programs, then after you log
in, you will then need to remember to type it in Minimak.  This can be a
bit disconcerting since you will frequently have to remember two ways of
typing the same thing.

If you go with [registry mapping], it will change layouts at boot-time,
so you won't have to remember to type in QWERTY at the login screen.
And you'll really mess with anyone who steals your password, then
tries to log into your machine thinking it's QWERTY.

Applications
============

VMware Console
--------------

VMware Console for Windows seems to rely on scan codes, which don't get
changed by remapping.  So your mappings won't have any effect in the
console.  This only happens in console and not, for example, when RDCing
to a virtual machine.  I've only encountered this with the console
software for VMware, but it's possible you may encounter it with other
programs as well.
 
In this case, the remapping software will work everywhere except the
window for the program in question. You'll just have to remember to type
in QWERTY for that window.  Even the boot mapping method doesn't fix
this.

VIM
---

While some of the keys with which [VIM] users are familiar have changed
with Minimak, the good news is that most are unchanged.  However, you
may want to remap the functionality of the J (down) and K (up) keys to N
and E respectively.  That means you'll probably want to map N (next) to
K as well.

Personally, I don't use key mappings because I'd rather learn the native
positions for my keyboard layout so I can have a single .vimrc which
doesn't have to change if I change layouts.  I use vim on some machines
which have to stay QWERTY, but I don't like having to create a
layout-specific .vimrc to maintain just for those machines.  For this
reason, I don't have the remapping commands for you, because I don't
know what they are.

While there is definitely relearning to be done when it comes to using
Minimak with VIM, there is a good argument to be made that Minimak is
the VIM-friendliest of the popular layouts today, due to the smallest
number of remappings.

Keyboard Lettering
==================

You may notice that the printed letters on your keyboard don't change
to match your new layout.

That is by design.

You see, having appropriately printed letters on your keyboard only
serves to encourage hunting-and-pecking, as well to encourage those
people who are not you to use your computer.  Eliminating both of these
temptations is considered a feature.

If you need to see the key layout for visual reference while you are
learning Minimak, [PKL] supports this.  You can also purchase [keyboard
lettering] stickers, which although they are made for Colemak, can
really be used for any layout since you choose where to affix them.

Or, if you have $1086 to burn, consider the [Optimus Popularis]
keyboard.  It lets you show any letter (or image, for that matter) on
any key!

[![Optimus Popularis Image]{: style="display:block;margin-left:auto;margin-right:auto" }][Optimus Popularis]

Or, if you're a real keyboard ninja, consider [Das Keyboard Model S
Ultimate], which has no lettering at all!  At least then it won't be
misleading.

[![Das Keyboard Image]{: style="display:block;margin-left:auto;margin-right:auto" }][Das Keyboard Model S Ultimate]

I'll also put in a plug for my favorite keyboard, the [TypeMatrix
ergonomic keyboard].  It's a great ergonomic keyboard, and inexpensive.
I like the 2020 model, which is available in the store for only $59.
You can get the 2030 as a blank model though. 

[![TypeMatrix Image]{: style="display:block;margin-left:auto;margin-right:auto" }][TypeMatrix ergonomic keyboard]

It is not suggested, however, that you remove and replace the keys of
your keyboard in the new configuration.  Some keyboards don't support
the removal of keys (i.e., they'll break) and some have keys of
differing shapes for different parts of the keyboard.

[registry mapping]: /download#rm
[PKL]: /download#pkl
[VIM]: http://www.vim.org/
[keyboard lettering]: http://www.4keyboard.com/colemakkeyboardsticker-p-234.html
[Optimus Popularis]: http://store.artlebedev.com/electronics/optimus-popularis/
[Optimus Popularis Image]: {{ urls.media }}/optimus-popularis-shop.jpg
[Das Keyboard Model S Ultimate]: http://www.daskeyboard.com/model-s-ultimate/
[Das Keyboard Image]: {{ urls.media }}/das_keyboard_s.jpg
[TypeMatrix ergonomic keyboard]: http://www.typematrix.com/shop/
[TypeMatrix Image]: {{ urls.media }}/2020-us.jpg
