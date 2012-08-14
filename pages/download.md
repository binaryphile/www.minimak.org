Minimak support varies by platform, but any platform that allows
key-mapping can be adapted.

Currently, the best support is for Windows, which has several options.
If you would like to contribute Linux or MacOS bindings, please use
[github](http://github.com/lilleyt/minimak).  We're not completely
familiar with custom keymaps on those platforms, but we've heard that the
[xmodmap](http://blacketernal.wordpress.com/set-up-key-mappings-with-xmodmap/)
facility is the place to start, at least on Linux.

There are a number of ways to use Minimak on Windows, including:

  - Easily switch between the half and full Minimak layouts with [Portable
Key Layout](#pkl) - **Recommended**

  - Create your own customized version of Minimak with the [Microsoft
Keyboard Layout Creator](#mklc)

  - Change Windows' boot-up key layout with [registry mapping](#rm)

We recommend learning Minimak with PKL and then later, if you're a
convert, setting your boot mappings with registry mappings.

Notes on Passwords
===================

One of the first things you'll learn when you try to adopt a new
keyboard layout is that you have an extremely hard time logging in
anywhere.  That's because your muscle memory no longer works for
passwords and since that is what you usually rely on, you now have to
spell everything out mentally.  Even then, it still usually ends up
wrong because you can't see any mistakes you're making.  This can be
very frustrating until you are proficient with the new layout.

This is a good reason to go with the recommended [PKL](#pkl) until you
are proficient at Minimak.  PKL allows you to turn the Minimak layout on
and off with a hotkey.  Just hit both *Alt* keys together and it will
suspend Minimak, putting you back in QWERTY.  Handle your login, then
hit both *Alts* again to toggle back to Minimak.  You'll want to do this
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

If you go with [registry mapping](#rm), it will change layouts at
boot-time, so you won't have to remember to type in QWERTY at the login
screen.  And you'll really mess with anyone who steals your password,
then tries to log into your machine thinking it's QWERTY.

Note on VMware Console
======================

VMware Console for Windows seems to rely on scan codes, which don't get
changed by remapping software.  This only happens in console and not,
for example, when RDCing to the same virtual machine.  We've only
encountered this with the console sofware for VMware, but it's possible
you may encounter it with other programs as well.
 
In this case, the remapping software will work everywhere except the
window for the program in question. You'll just have to remember to type
in QWERTY for that window.  Even the boot mapping method doesn't fix
this.

<a id="pkl">
Portable Key Layout
===================
</a>

You can find a copy of PKL customized for Minimak on
[github](https://github.com/downloads/lilleyt/minimak/pkl.zip).  This is
a copy of the PKL project with the Minimak layout added by us, not one
of their own distributions.

PKL is by FARKAS Máté and is distributed under GPL 3.

PKL is the recommended tool while you're learning Minimak.  PKL shows
you a keyboard image with the new layout, so you can consult it while
you learn.  It also supports switching layouts easily via menu, as well
as suspending PKL entirely by hitting both *Alt* keys.

PKL starts in full Minimak mode (both hands). There is a system tray
icon that can be right-clicked for a menu that includes the ability to
select the left-hand-only half-Minimak.

The keyboard graphic that is shown by PKL can be moved to one of two
predetermined positions by floating your mouse over it.  It can also be
removed from view by the hotkey combination *Windows+F1*.

There is no installation program for PKL, so you just unzip it and run
it.  If you decide you want to keep it, you can use a tool like
[ZipInstaller](http://www.nirsoft.net/utils/zipinst.html) to install it
in your *Program Files* directory for you, along with an uninstaller.
You may also decide to add a shortcut to the PKL executable to your
*Start* menu's *Startup* folder.

You can find more information on the [PKL
website](http://pkl.sourceforge.net/).

Note on BacksLock
-----------------

Taking a cue from [Colemak](http://colemak.com/), we recommend remapping
*CapsLock* to be another *Backspace* key.  It's one of the best keymappings
you can make, and many Linux flavors have their own setting to do it.

We call that mapping *BacksLock* for short, which is just our own name for
it.  Despite the name, there's no "locking" of the key like with *CapsLock*.

However, since that mapping isn't part of the standard Minimak, it is
not in the PKL layouts.  If you're ready to try *BacksLock* on Windows, we
suggest using the [registry mapping](#rm) that includes it.  On Linux,
you can instead check your configurations settings to see if there is a
mapping defined.

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
can't map *CapsLock* to *BacksLock* (among other keys).

While *BacksLock* isn't part of Minimak, we recommend using a tool that
can remap it whether you choose to use Minimak or not.  It's just a good
idea.

If you see a need for MKLC Minimak layouts that we've missed, we'd be
glad to hear your viewpoint and possibly include in the project any
layouts you'd be willing to create, presuming the rationale and
implementation meet our standards.

<a id="rm">
Registry Mapping
================
</a>

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

That's why we only recommend using registry mappings *after* you've
fully learned Minimak.

There are two modes of mappings, boot mappings and user mappings.  User
mappings only take effect after you've logged in.  However, they only
work for XP since user mapping functionality was removed with Vista.  We
recommend using boot mappings anyway since it allows you to type your
password the same when you're logging in as any other time.

Before you download any of the mappings, remember that they are provided
AS IS.  We are not responsible for any damage or inconvenience incurred
by using them.  If there is an issue with the download or how it is
loaded into your system, it may result in a non-working system or a
system you are locked out of.  Since these are boot mappings, you cannot
get around them by trying to log into another account.  What you load is
what you get, for all users.

If you do have a problem logging in after installing them, you can still
log in on Windows 7 with the on-screen keyboard.  Click on the *Ease of
Access* button in the lower left-hand corner of the login screen, then
click *Type without the keyboard (On Screen Keyboard)* and click *Ok*.
We don't have directions for XP, but if you figure them out, please let
us know so we can post them.

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
[github](https://github.com/downloads/lilleyt/minimak/registry_mappings.zip).
There are three versions in the zip:

  * Minimak-l - left-hand only
  * Minimak - both hands
  * Minimak + BacksLock - full Minimak with *CapsLock* mapped to *Backspace*

To install any of them, unzip the download and double-click the mapping
you want.  Windows will ask you if you want to load the file into the
registry.  Confirm it and then reboot the machine.  Remember to type in
the new layout when entering your password, and don't be surprised if
you don't get it right the first time.

<a id="km">
Key Mapper
----------
</a>

[Key Mapper](http://code.google.com/p/keymapper/) is one of [a number of
tools](http://www.makeuseof.com/tag/remap-keyboard-free-tools-windows/)
that take a more low-level approach to remapping, using Windows'
registry mappings for virtual keys. (In addition to the list provided in
the link, there's also
[kmapper](http://colemak.com/pub/windows/Kmapper-1.0.zip))

Of these, we like Key Mapper best because of its intuitive GUI.

To use Key Mapper, install it and run it.  Be sure you are running it
from an account with administrator privileges.

It will show you the basic instructions for using it, but here's the
short version.

First, switch to boot mapping mode, by selecting the *Mappings > Show >
Boot Mappings* menu item.  If you are on XP and want to create user
mappings instead, just skip this step.

Then, drag the key you want in a new location to that location.  When it
is dropped in place, the new key will show in a different color.  The
mapping will not take effect until you close Key Mapper and reboot your
machine, however.

If you are remapping a lot of keys, you will eventually end up mapping
over a key you also want to map somewhere else.  If so, double-click the
location you want to place the hidden key, then click *Capture* and type
the key you want to map.

Finally, exit Key Mapper and reboot your computer.  Be sure to read all
of the discussion in the notes above about passwords, etc.

Key Mapper can also export key configurations from *Mappings > Export As
Registry File*.  The registry files can be loaded by double-clicking on
them; you don't need to run Key Mapper to install them.

<a id="tt">
Typing Tutors
=============
</a>

Now that you've got your spiffy new layout in action, how do you learn
it?

You might start with our recommendations on the [learning](learning)
page.  However, before you jump over there, here are some programs and
sites that you may find useful for typing practice:

  * [GNU Typist](http://www.gnu.org/software/gtypist/) - Simple
  console-mode tutor
  * [TIPP10](http://www.tipp10.com/en/index/) - GUI
  typing tutor
  * [TypeRacer](http://www.typeracer.com/) - typing web site

Here's a [list of other
tutors](http://typingsoft.com/all_typing_tutors.htm) if none of those
are to your liking.

As always, make sure you are using good antivirus, such as [Panda Cloud
Antivirus](http://www.cloudantivirus.com), as we've come across at least
one free typing tutor that reportedly is infected.  For the best
security, we recommend scanning any downloaded file with the [VirusTotal]
(http://www.virustotal.com/) site, which scans with 40+ brand-name virus
scanners.  They also have an [uploader application]
(https://www.virustotal.com/documentation/desktop-applications/) that
can send a file from your desktop for scanning via the Explorer *Send To*
menu.  There's also a [Chrome extension]
(https://chrome.google.com/webstore/detail/efbjojhplkelaegfbieplglfidafgoka)
for scanning suspicious site links from within [Google Chrome]
(https://www.google.com/intl/en/chrome/browser/).


How sad is it that [Typing of the
Dead](http://www.amazon.com/The-Typing-Dead-Pc/dp/B00005RV5M), the
funnest way to learn typing, can't be had for less than $55?  There is,
however, a [free
demo](http://www.pcworld.com/downloads/file/fid,8276-order,1-page,1/description.html)
still available from PC World.  The demo features the first arcade level.

Note on VIM
===========

While many of the keys with which [VIM](http://www.vim.org/) users are familiar have changed
with Minimak, the good news is that a number of the related ones are in
the same relative positions.  For example, the J, K and L buttons have
been moved together to the top row (H, however, remains in the same
location).

While there is definitely relearning to be done when it comes to using
Minimak with VIM, there is a good argument to be made that Minimak is
*the* VIM-friendliest of the popular layouts today, due to the smallest
number of remappings and finger-impulse retention.

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
learning Minimak, [PKL](#pkl) supports this.

Or, if you have $1086 US to burn, consider the
[Optimus Popularis](http://store.artlebedev.com/electronics/optimus-popularis/)
keyboard.  It lets you show any letter (or image, for that
matter) on any key!

Or, if you're a real keyboard ninja, consider [Das Keyboard Model S
Ultimate] (http://www.daskeyboard.com/model-s-ultimate/), which has no
lettering at all!  At least then it won't be misleading.

It is not suggested, however, that you remove and replace the keys of
your keyboard in the new configuration.  Some keyboards don't support
the removal of keys and some have keys of differing shapes for different
parts of the keyboard.
