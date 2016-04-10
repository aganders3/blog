Safari User Style Sheets
########################
:status: published
:date: 2016-04-09 21:03
:category:
:tags:
:author: Ashley Anderson
:summary:
:header_cover: /images/piestewa_1024.jpg

I use an ad blocker. OK, I use two ad blockers. There's a lot of debate about
the use of ad blockers that I'd rather not get involved in. Maybe this post is
getting involved.

In defense (retaliation?) against ad blockers, several sites are now blocking
blockers. All's fair! My problem is that browsing along, I often run into these
sites unintentionally. I don't want to go through lengths to circumvent these
protections, I just want to avoid hitting the sites in the first place. There
is a plethora of free (or paid) content out there.

I came across a `Hacker News comment`_ recently that suggested decorating
such links through a user style sheet. I think years ago I heard of user style
sheets but never gave them much thought. I use Safari, and a quick search led
me to the Apple developer page regarding injecting styles with a `Safari
Extension`_. It turned out to be remarkably easy to add some style to links to
a couple websites.

Just open the Safari Extension Builder (in the Develop menu -- you must have
developer mode enabled):

.. image:: /images/0001/safari_extension_builder.png
    :width: 100%
    :alt: the safari extension builder window

The ``+`` button in the lower left will allow you to create a new extension.
For this extension, the only thing we need is a style sheet. Put one in the
extension folder (`<extension_name>.safariexension`) next to the `Info.plist`
file. Use `substring matching selectors`_ to filter for URLs you want to
decorate. Here's how I have it set up:

.. code-block:: css

    a[href*="forbes.com"],
    a[href*="wired.com"] {
        color: #8B0000 !important;
    }

    a[href*="forbes.com"]::after,
    a[href*="wired.com"]::after {
        font-size: 50%;
        content: "😱";
    }

Select that file in the Extension Builder, and install your extension. Now my
links look like this:

.. image:: /images/0001/decorated_links.png
    :width: 100%
    :alt: links decorated with user style rules

Anyway, this is just one controversial use, but I'm keeping track of the
process for my own sake for future ideas. Unfortunately, without paying
$99/year for the Apple Developer Program, I can't sign my extensions. This
means I have to re-install them each time I quit/restart Safari. This is a
drag, but not a huge deal as I usually just keep it running.

.. _Hacker News comment: https://news.ycombinator.com/item?id=11455934
.. _Safari Extension: https://developer.apple.com/library/safari/documentation/Tools/Conceptual/SafariExtensionGuide/AddingStyles/AddingStyles.html#//apple_ref/doc/uid/TP40009977-CH7-SW1
.. _substring matching selectors: https://www.w3.org/TR/selectors/#attribute-substrings

