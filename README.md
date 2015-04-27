
YaST CI Tasks
=============

[![Build Status](http://ci.opensuse.org/buildStatus/icon?job=yast-rake-ci-master)](http://ci.opensuse.org/view/Yast/job/yast-rake-ci-master/)
[![Code Climate](https://codeclimate.com/github/yast/yast-yast-rake-ci/badges/gpa.svg)](https://codeclimate.com/github/yast/yast-rake-ci)


Description
============

This package provides extensions for the [YaST Rake tasks](https://github.com/yast/yast-rake).

These tasks are needed only during development and in Jenkins build, this package
in not needed at run-time or in OBS for building the YaST packages.

The package installs all needed packages via RPM dependencies.

Provided Tasks
--------------

### check:ci ###

This Rake task is designed for running tests and check in Jenkins CI. These
checks can run locally as well. This task is used by this module itself to run
the tests during package build.

The task runs these tests and checks:

- Runs test using the [`test:unit`](https://github.com/yast/yast-rake#testunit)
  task, it sets `COVERAGE=1` environment variable to run the tests with the
  code coverage enabled.
- If [`.rubocop.yml`](https://github.com/bbatsov/rubocop/blob/master/config/default.yml)
  file is present it runs [`rubocop`](https://github.com/bbatsov/rubocop)
  to check the code style
- If the file is missing it runs simple [`check:syntax`](https://github.com/openSUSE/packaging_tasks#checksyntax)
  task to at least check the syntax of the files.
- It runs the [`check:spelling`](https://github.com/yast/yast-rake#checkspelling)
  task to check spelling in documentation files
- Runs the [`check:pot`](https://github.com/yast/yast-rake#checkpot) task
  to scan for possible errors in translations
- Runs the [`yard`](https://github.com/lsegal/yard) task if `.yardopts` file is present


Development
===========

This module is developed as part of YaST. See the
[development documentation](http://yastgithubio.readthedocs.org/en/latest/development/).


Getting the Sources
===================

To get the source code, clone the GitHub repository:

    $ git clone https://github.com/yast/yast-rake-ci.git

If you want to contribute into the project you can
[fork](https://help.github.com/articles/fork-a-repo/) the repository and clone your fork.


Contact
=======

If you have any question, feel free to ask at the [development mailing
list](http://lists.opensuse.org/yast-devel/) or at the
[#yast](https://webchat.freenode.net/?channels=%23yast) IRC channel on freenode.
