# Bengfort.com

**The web application for the Bengfort website.**

[![Build Status](https://travis-ci.org/bbengfort/bengfort.com.png?branch=master)](https://travis-ci.org/bbengfort/bengfort.com)
[![Coverage Status](https://coveralls.io/repos/github/bbengfort/bengfort.com/badge.svg?branch=master)](https://coveralls.io/github/bbengfort/bengfort.com?branch=master)
[![Code Health](https://landscape.io/github/bbengfort/bengfort.com/master/landscape.svg?style=flat)](https://landscape.io/github/bbengfort/bengfort.com/master)
[![Stories in Ready](https://badge.waffle.io/bbengfort/bengfort.com.png?label=ready&title=Ready)](https://waffle.io/bbengfort/bengfort.com)

[![Skipper](bengfort/assets/img/skipper.jpg)](https://flic.kr/p/pqWmjP)

## About

This is the small web application that powers Bengfort.com. Primarily this application implements the [Wagtail CMS](https://wagtail.io/) so that the app is in Python instead of PHP (allowing me to modify at will).

### Attribution

The image used in this README, [Skipper](https://flic.kr/p/pqWmjP) by [Eric B. Walker](https://www.flickr.com/photos/premierehdr/) is licensed under [CC BY-NC 2.0](https://creativecommons.org/licenses/by-nc/2.0/)

## Changelog

The release versions that are deployed to the web servers are also tagged in GitHub. You can see the tags through the GitHub web application and download the tarball of the version you'd like.

The versioning uses a three part version system, "a.b.c" - "a" represents a major release that may not be backwards compatible. "b" is incremented on minor releases that may contain extra features, but are backwards compatible. "c" releases are bug fixes or other micro changes that developers should feel free to immediately update to.

### Version 0.2

* **tag**: [v0.2](https://github.com/bbengfort/bengfort.com/releases/tag/v0.2)
* **deployment**: Friday, November 11, 2016
* **commit**: [see tag](#)

Another intermediate step in the wagtail managed application. Now the home page is a bit more dynamic and editable. The navbar will show all menu items associated with it. We've also implemented a blog applications for writing blog posts, related links, tags, and search are all functional as well. It still doesn't look pretty, but it's moving along.

### Version 0.1

* **tag**: [v0.1](https://github.com/bbengfort/bengfort.com/releases/tag/v0.1)
* **deployment**: Thursday, November 10, 2016
* **commit**: [0efa4db](https://github.com/bbengfort/bengfort.com/commit/0efa4db8035f90f3eae52896fe56fd5c9caecd47)

This initial release of the application simply deploys the Bengfort web app to Heroku, and implements the Wagtail CMS. It is really nothing special and is a pre-release. Feel free to ignore it!
