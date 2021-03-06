---
title: Download
description:
---

[Download For Windows]{: .art-button}
{: .float-right }

Windows
-------

Supports all versions of Windows from XP on.  All of the materials are
provided AS IS.  __Please read the [caveats].__  I'm not responsible for any
damage to your system or inconvenience caused by using these layouts.

Included in the download
are:

- __[Portable Key Layout]__ - _Recommended for learning Minimak_
- __[Registry Mappings]__ - for system-level installation

Again, __please read the page on [caveats]__ if this is the first time you
are using an alternative layout.

[Download For Mac]{: .art-button}
{: .float-right }

Mac
---

Mac bindings are included in the zip.  Do the following:

- Copy `Minimak.bundle` from the `osx` directory in the repository to `/Library/Keyboard Layouts`.
  You will need to enter your password.
- Open _System Preferences > Keyboard > Input Sources_
- Turn on the layouts you wish to use

For information on Backslock on the Mac, see the [Colemak Mac page].

[Download For Linux]{: .art-button}
{: .float-right }

Linux
-----

At the moment, mappings are only available for graphics mode logins via
[xmodmap].

These are brand new mappings and untested since I don't have a machine
with X to test on.  The mappings are simple enough that I'm confident
most will work with the possible exception of the P and semicolon
mappings, since I'm not sure whether the semicolon keysym is spelled
out.

To try the keymappings for the length of your login session, run the
command:

    xmodmap filename

where filename is the name of the mapping you've chosen.

To install one for your login, first copy the file to `~/.Xmodmap`, then
add the following to `~/.xinitrc`:

    if [ -f $HOME/.Xmodmap ]; then
        /usr/bin/xmodmap $HOME/.Xmodmap
    fi

There are no Backslock mappings since many Linux systems have Backslock
as a possible configuraion choice in their keyboard settings.

[Download For Windows]{: .art-button}
{: .float-right }

Portable Key Layout {#pkl}
===================

PKL is the recommended tool while you're learning Minimak.  PKL shows
you a keyboard image with the new layout, so you can consult it while
you learn.  It also supports suspending Minimak by hitting both Alt
keys.

The keyboard graphic that is shown by PKL can be moved to one of two
predetermined positions by floating your mouse over it.  It can also be
removed from view by the hotkey combination Windows+F1.

There is no installation program for PKL, so you just unzip it and run
it.  If you decide you want to keep it, you can use a tool like
[ZipInstaller] to install it in your _Program Files_ directory for you,
along with an uninstaller.

You may also want to add a shortcut to the PKL executable to your
Start menu's _Startup_ folder.

You can find more information on the [PKL website].

PKL is by FARKAS Máté and is distributed under GPL 3.

[Download For Windows]{: .art-button}
{: .float-right }

Registry Mapping {#rm}
================

The advantage to using the registry mapping approach is that it remaps
the keys at boot time, and you only need to do it once.  Once it's
been done, you don't need to run any additional software from then on,
unlike PKL.

However, there are two drawbacks to this approach.  The first is that it
doesn't work if you want anyone else to be able to use your machine.
The mappings apply to all users and take effect at boot time.  This is
usually unworkable on machines that are shared between users, and
prevents you from doing things like handing the keyboard to someone else
so they can put in a password, for example.  If you are using XP, read
about user mappings below for a way to allow other users to logon
without losing their regular QWERTY layout.

The second drawback is that you can't undo the mappings, even
temporarily, without rebooting your machine.  The only way to
temporarily undo the registry mappings would be to use another mapping
tool like PKL with an inverse-Minimak mapping, but currently PKL has no
such mapping.

That's why I only recommend using registry mappings _after_ you've
fully learned Minimak.

There are two modes of mappings, boot mappings and user mappings.  User
mappings only take effect after you've logged in.  However, they only
work for XP since user mapping functionality was removed with Vista.  I
recommend using boot mappings anyway since it allows you to type your
password the same when you're logging in as any other time.

Before you download any of the mappings, remember that they are provided
AS IS.  I am not responsible for any damage or inconvenience incurred
by using them.  If there is an issue with the download or how it is
loaded into your system, it may result in a non-working system or a
system you are locked out of.  Since these are boot mappings, you cannot
get around them by trying to log into another account.  What you load is
what you get, for all users.

If you do have a problem logging in after installing them, you can still
log in on Windows 7 with the on-screen keyboard.  Click on the _Ease of
Access_ button in the lower left-hand corner of the login screen, then
click _Type without the keyboard (On Screen Keyboard)_ and click _Ok_.
I don't have directions for XP, but if you figure them out, please let
us know so I can post them.

If you want to avoid this possibility altogether, you may want to do the
mappings yourself with [Key Mapper](#km), rather than rely on our
registry files.  You may also want to use user mappings rather than boot
mappings so you can get in via another account if the mappings don't
work correctly.  If you go that route, you may want to first try out
your mapping on a temporary account created for that purpose.  Note that
user mappings only work for XP, not Vista, 7 or 8.

That said, the registry files should work on any Windows that's at least
XP or above.

You can download boot mappings that work for any Windows system from
[github].  There are several versions in the zip, consult the README
there.

To install one of them, unzip the download and double-click the mapping
you want.  Windows will ask you if you want to load the file into the
registry.  Confirm it and then reboot the machine.  Remember to type in
the new layout when entering your password, and don't be surprised if
you don't get it right the first time.

BacksLock
---------

Taking a cue from [Colemak], I recommend remapping CapsLock to be
another Backspace key.  It's one of the best keymappings you can make,
and many Linux flavors have their own setting to do it.

I call this mapping BacksLock for short, which is just my own name for
it.  Despite the name, there's no "locking" of the key like with
CapsLock.

However, since that mapping isn't part of the standard Minimak, it is
not in the PKL layouts.  If you're ready to try BacksLock on Windows, I
suggest using the [registry mapping] that includes it.  On Linux, you
can instead check your configurations settings to see if there is a
mapping defined.

Key Mapper {#km}
----------

[Key Mapper] is one of [a number of tools] that take a more low-level
approach to remapping, using Windows' registry mappings for virtual
keys. (In addition to the list provided in the link, there's also
[kmapper])

Of these, I like Key Mapper best because of its intuitive GUI.

To use Key Mapper, install it and run it.  Be sure you are running it
from an account with administrator privileges.

It will show you the basic instructions for using it, but here's the
short version.

First, switch to boot mapping mode, by selecting the _Mappings > Show >
Boot Mappings_ menu item.  If you are on XP and want to create user
mappings instead, just skip this step.

Then, drag the key you want in a new location to that location.  When it
is dropped in place, the new key will show in a different color.  The
mapping will not take effect until you close Key Mapper and reboot your
machine, however.

If you are remapping a lot of keys, you will eventually end up mapping
over a key you also want to map somewhere else.  If so, double-click the
location you want to place the hidden key, then click _Capture_ and type
the key you want to map.

Finally, exit Key Mapper and reboot your computer.  Be sure to read all
of the [caveats] about passwords, etc.

Key Mapper can also export key configurations from _Mappings > Export As
Registry File_.  The registry files can be loaded by double-clicking on
them; you don't need to run Key Mapper to install them.

Note on Microsoft Keyboard Layout Creator {#mklc}
=========================================

[Keyboard Layout Creator] is Microsoft's officially-supported way of
adding layouts to most versions of Windows, including XP and 7.

That said, I don't recommend it.  I didn't see any advantage to MKLC
versus the other solutions, and it's slightly less functional since it
can't map CapsLock to BacksLock (among other keys).

While BacksLock isn't formally part of Minimak, I recommend using a tool
that can remap it whether you choose to use Minimak or not.  Unless
you've already mapped some other key to CapsLock, it's just a good
idea to put Backspace there.

{{>download-event}}

[Download For Windows]: {{ site.download_location }}
[Download For Mac]: {{ site.download_location }}
[Download For Linux]: {{ site.download_location }}
[ZipInstaller]: http://www.nirsoft.net/utils/zipinst.html
[PKL website]:http://pkl.sourceforge.net/
[github]: {{ site.download_location }}
[Portable Key Layout]: #pkl
[Registry Mappings]: #rm
[registry mapping]: #rm
[Colemak]: http://colemak.com/
[caveats]: /caveats
[Key Mapper]: http://code.google.com/p/keymapper/
[a number of tools]: http://www.makeuseof.com/tag/remap-keyboard-free-tools-windows/
[kmapper]: http://colemak.com/pub/windows/Kmapper-1.0.zip
[Keyboard Layout Creator]: http://www.microsoft.com/globaldev/tools/msklc.mspx
[Colemak Mac page]: http://colemak.com/wiki/index.php?title=Mac
[xmodmap]: https://wiki.archlinux.org/index.php/Xmodmap
