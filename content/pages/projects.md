Title: Projects
Date: 2018-04-26 10:24
Status: published
Summary: A sampling of projects I created or contributed to
Header_Cover: /images/piestewa\_1024.jpg

Projects
========

Yield Curve Viewer
------------------
*A Flask-based web app for viewing The Yield Curve*

[Yield Curve Viewer](http://yield.aga3.xyz)

The Yield Curve refers to the "curve" of US Treasury Bond yields, and is a
financial [indicator](http://www.npr.org/indicator) with a track record for
predicting recessions. I built this site to scrape official yield data daily
from [treasury.gov](http://www.treasury.gov) and display the curve in a simple
manner.

Forecheck
---------

*An iOS app for creating resusable checklists*

<img class="align-left" width="30%" src="/images/projects/ForecheckIcon_masked.png" alt="Forecheck app icon"/>

Use Forecheck to create and re-use checklists for workflows, chores,
packing lists, and any other repeated processes you need to manage.
Checklists help ensure task completeness and eliminate oversights.
Forecheck is built to be minimal yet flexible, with a simple interface
designed to do one thing well.

Forecheck was developed on nights and weekends in winter 2017/2018. It
is my first complete iOS App.

<a href="https://itunes.apple.com/us/app/Forecheck-checklist-maker/id1351180485">
    <img class="align-center" src="/images/projects/Download_on_the_App_Store_Badge_US-UK_RGB_blk_092917.svg" alt="Download Forecheck on the App Store" style="cursor: pointer;" />
</a>

**Privacy Policy** Forecheck does not collect or store any user data.
Apple does collect and report to me some anonymized usage statistics.
This may change in future versions of Forecheck. If it does, this
privacy policy will be updated accordingly, and it will be noted in the
update notes.

GPI
---

*A Graphical Programming Interface for image processing and scientific
programming* [www.gpilab.com](http://www.gpilab.com)

GPI was developed by Nick Zwart to support MRI research for the Magnetic
Resonance Technology Design Group at the Barrow Neurological Institute
in Phoenix, AZ. I joined this group as a post-doc in 2014, eventually
becoming a Research Assistant Professor. I moved on from this position
in 2017, but I still use and maintain GPI in a smaller capacity.

Ray Tracing
-----------

Recently I've been learning about Rust and getting back to 3D graphics programming.
Those interests combined in my
[`wasm-ray`](https://github.com/aganders3/wasm-ray) project. This is an
implementation based on Peter Shirley's great book [_Ray Tracing in One
Weekend_](https://raytracing.github.io).

Initially I was building it for wasm - you can see the live demo of that
[here](https://aga3.xyz/wasm-ray/), but ultimately it was too slow to be fun
and I switched to local rendering. This also let me learn about "fearless
parallelism" in Rust, which was nice. I'm planning to keep this project going
for a while in some form.
