Installation
====================================

Here we'll cover how to install TauLidarCommon. You need to make sure it's installed correctly before you can dive into using it!

Prerequisite: Install Python
----------------------------

Self-explanatory: you will need to have Python installed!

Download and install Python at https://www.python.org/downloads/.
**Make sure you install version 3.7 or higher**.

If you have questions about using Python, check out the `official Python.org  instructions <https://docs.python.org/3/using/index.html>`_.

$ python -m pip install TauLidarCommon
--------------------------------------

To install TauLidarCommon, you can use pip and run this command in your terminal of choice::

    $ python -m pip install TauLidarCommon

Alternate Method: Get the Source Code
-------------------------------------

TauLidarCommon is developed on `GitHub <https://github.com/OnionIoT/tau-lidar-common>`_

You can either clone the public repository::


    $ git clone git@github.com:OnionIoT/tau-lidar-common.git


Or, download a zip of the repo::

    $ curl -OL https://github.com/OnionIoT/tau-lidar-common/archive/master.zip

Once you have a copy of the source, you can embed it in your own Python package, or install it into your site-packages::

    $ cd tau-lidar-common
    $ python -m pip install .
