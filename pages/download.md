MiniMak support varies by platform, but any platform that allows
key-mapping can be adapted.

Currently, the best support is for Windows, which has several options.
If you would like to contribute Linux or MacOS bindings, please use
[github](http://github.com/lilleyt/minimak).  I'm not completely
familiar with custom keymaps on those platforms, but I've heard that the
[xmodmap](http://blacketernal.wordpress.com/set-up-key-mappings-with-xmodmap/)
facility is the place to start, at least on Linux.

There are a number of ways to use MiniMak on Windows, including:

  - Easily switch between the half and full MiniMak layouts with [Portable
Key Layout](#pkl) - **Recommended**

  - Create your own customized version of MiniMak with the [Microsoft
Keyboard Layout Creator](#mklc)

  - Change Windows' boot-up key layout with [Key Mapper](#km)

We recommend learning MiniMak with PKL and then later, if you're a
convert, setting your boot mappings with Key Mapper.

Notes on Passwords
===================

One of the first things you'll learn when you try to adopt a new
keyboard layout is that you have an extremely hard time logging into
anything.  That's because your muscle memory no longer works for
passwords and since muscle memory is usually what you rely on, you now
have to spell everything out mentally.  Even then, it still usually ends
up wrong because you can't see any mistakes you're making.  This can be
very frustrating until you are proficient with the new layout.

This is a very good reason to go with the recommended [PKL](#pkl) until
you are really proficient at MiniMak.  PKL allows you to turn the
MiniMak layout on and off with a hotkey.  Just hit both Alt buttons
together and it will suspend MiniMak, putting you back in QWERTY.
Handle your login, then hit both Alts again to toggle back to MiniMak.
You'll want to do this whenever you deal with passwords.

Creating Passwords
------------------

You especially don't want to use MiniMak to create new passwords until
you are 100% accurate since learning a new layout makes you mistype
letters in a consistent and reproducible fashion.  If you do try to make
passwords, you will typically end up with a password that's good enough
to get most systems to accept, since you can type it the same way twice,
but isn't the password you thought it was because you couldn't see
your (consistently) mistyped letters.

Even when you're fairly confident of your new typing skills, it's a good
idea to type new passwords into a text editor first, then cut and paste
it into the site or application that needs it.

Logging In
----------

Another thing to note is that the different methods of changing layouts
don't always work for your system's bootup login prompt.

If you use a method that only remaps your keys after you login, you'll
need to remember to type your login password in the system's native
format (QWERTY, most likely) in order to log into your account.  This is
true for PKL and layouts created with MKLC, since they are only enabled
after you log in.

After you log in, you may use the same password to log into other
systems or sites.  You will then need to remember to type it in MiniMak,
which can be a bit disconcerting since you will frequently have
to remember two ways of typing the same thing.

If you go with the [Key Mapper](#km) software, it will change layouts at
boot-time, so you won't have to remember to type in QWERTY at the login
screen.

Note on VMware Console
======================

VMware Console for Windows seems to rely on scan codes, which don't get
changed by remapping software.  This only happens in console and not,
for example, when RDCing to the same virtual machine.  We've only
encountered this with the console sofware for VMware, but it's possible
you may encounter it elsewhere as well.
 
In this case, the remapping software will work everywhere except the
window for the program in question. You'll just have to remember to type
in QWERTY for that window.  Even the boot mapping method doesn't fix
this.

<a id="pkl">
Portable Key Layout
===================
</a>

You can find a copy of PKL customized for MiniMak on
[github](https://github.com/downloads/lilleyt/minimak/pkl.zip).  This is
a copy of the PKL project with the MiniMak layout added by us, not one
of their own distributions.

PKL is the recommended tool while you're learning MiniMak.  PKL shows
you a keyboard image with the new layout, so you can consult it while
you learn.  It also supports switching layouts easily via menu, as well
as suspending PKL entirely by hitting both Alt keys.

PKL starts in full MiniMak mode (both hands). There is a system tray
icon that can be right-clicked for a menu that includes the ability to
select the left-hand-only half-MiniMak.

The keyboard graphic that is shown by PKL can be moved to one of two
predetermined positions by floating your mouse over it.  It can also be
removed from view by the hotkey combination Windows+F1.

You can find more information on the
[PKL website](http://pkl.sourceforge.net/).

<a id="mklc">
Microsoft Keyboard Layout Creator
=================================
</a>

[Keyboard Layout
Creator](http://www.microsoft.com/globaldev/tools/msklc.mspx) is
Microsoft's officially-supported way of adding layouts to most versions
of Windows, including XP and 7.

That said, we don't recommend it.  We didn't see any advantage to MKLC
versus the other solutions, and it's slightly less functional since it
can't map Caps Lock (among other keys).

While Caps Lock isn't part of MiniMak, we recommend using a tool that
can remap it to Backspace whether you choose to use MiniMak or not.
It's just a good idea.

If you see a need for MKLC MiniMak layouts that we've missed, we'd be
glad to hear your viewpoint and possibly include in the project any
layouts you'd be willing to create, presuming the rationale and
implementation meet our standards.

<a id="km">
Key Mapper
==========
</a>

[Key Mapper](http://code.google.com/p/keymapper/) is one of a number of
tools that take a more low-level approach to remapping, using Windows'
registry mappings for virtual keys.

The advantage to using the Key Mapper approach is that it remaps the
keys from boot time, and you only need to do it once.  Once it's been
done, you don't need to run any additional software, unlike PKL.

That's why we only recommend using it *after* you've fully learned
MiniMak.
