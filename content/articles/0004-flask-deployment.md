Title: Flask Deployment with Fabric
Status: published
Date: 2018-09-25 22:53
Author: Ashley Anderson

I've been playing around with [Flask](http://flask.pocoo.org) lately, and
deployment became a major bottleneck in my work-run cycle. I use [Digital
Ocean](http://digitalocean.com), which is cheap, simple, and has a great
[Community](https://www.digitalocean.com/community) section full of tutorials.
Still, when developing your own app this is far from a one-click setup out of
the box.

I've found [Fabric](http://www.fabfile.org) to be a simple way to automate
tedious tasks and take ownership over the deployment process. Below is a gist
of my rudimentary fabfile.py with tasks for creating, initializing, and
destorying droplets. This setup uses NginX + Gunicorn to serve the Flask app.

<script src="https://gist.github.com/aganders3/6b40485d74d4b37a19cd0ca34f512cc8.js"></script>
