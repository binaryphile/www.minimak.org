---
title: Minimak tweeted by Jeff Atwood
date: '2012-10-22'
description:
categories: sightings
---

I've followed Jeff's [Coding Horror] blog for quite some time, and from
it I know that [he takes his keyboarding seriously].  I thought he might
find Minimak interesting, but I've held off trying to bring it to his
attention until the site was in some kind of presentable shape.

Today's that day.  Within 10 minutes of sending him an email, he tweeted
the site out, and it's amazing to see the amount of traffic it's
generated.

![Site Statistics]

About 2,000 visits in the space of 2 hours...wow!  Of those, about 50 of
you downloaded the Windows package.  If any of you Mac/Linux users out
there want to contribute packages, that would be great since I don't
really know how to do it on those platforms.  Xmodmap or xkb on Linux
seem to be the way to go there, but I don't know what Mac has for
remapping.

Of course, I managed to bork things up a bit right in the midst of the
onslaught...I remembered that I was hosting on S3, which charges for
traffic, and so I immediately:

a) put in a valid credit card, since they'd been letting me coast
forever and a day

b) tried to set cache-control headers on all of the site content

It's the second one that got me in trouble because I had to use a
program which shall remain nameless, one I'd never tried before.  It
changed the cache headers, but all my content-type headers also got
changed in the process, breaking the whole site.

I quickly reuploaded the site, so I don't think many people were
affected.

Last, I should mention that I forgot to post how to contact me...the
easiest way is either through the comments here or via the [issues tab]
at github.

Happy Minimaking!

[Coding Horror]: http://www.codinghorror.com/blog/
[Site Statistics]: {{ urls.media }}/statistics.png
[issues tab]: https://github.com/binaryphile/minimak/issues
[he takes his keyboarding seriously]: http://www.codinghorror.com/blog/2010/10/the-keyboard-cult.html
