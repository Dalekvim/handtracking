Hand Tracking
=============

This project takes footage from a webcam using OpenCV and uses MediaPipe to detect and draw networks on hands.

I made this following a YouTube video course, `Advanced Computer Vision with Python <https://youtu.be/01sAkU_NvOY>`__ as part of my Seeing with Sound project.

.. image:: https://google.github.io/mediapipe/images/mobile/hand_landmarks.png

Installation
------------

If you have git installed on your machine, you can clone this repo

``git clone https://github.com/Dalekvim/handtracking.git``

or you can download a zip file by clicking on the dropdown box that says "code" and then "Download ZIP".

When the download is complete, open up a terminal, and change directory into the project.

Dependencies
~~~~~~~~~~~~

**Note:** This section assumes you are in the root directory of the project.

Download ``pipenv``, if you haven't already. You can get it using python's package manager:

``python -m pip install pipenv``

If this doesn't work on windows, you may want to try

``py -m pip install pipenv``

Then use

``pipenv install --ignore-pipfile``

to download the dependencies.

If you want dev dependencies, use

``pipenv install --dev``

Usage
-----

First change directory to where the main file is

``cd handtracking``

Check that you are in the right directory using

``dir`` (windows)

or

``ls`` (mac or linux)

You should see a file called ``handtracking.py``. This is the main script.

To run this file use

``python handtracking.py``

or

``py handtracking.py`` (windows)
