Affinity
========

Affinity is a command line HTTP client similar to curl but made to be
simplistic and easy-to-use. Affinity is written in 100% pure python

Installation
------------

1. Download the source code and extract it
2. Run:

.. code:: bash

   $ pip install .

Quick Start Guide
-----------------

To make a simple GET request to the `Github
API <https://api.github.com/>`__ you just need to run:

.. code:: bash

   $ affinity https://api.github.com/

Now when you run that you will see:

.. code:: bash

   200 GET https://api.github.com/

To see the data sent from the request add the *-o* flag to output the
results to the console

.. code:: bash

   $ affinity https://api.github.com/ -o

If you want to learn more either run ``affinity -h`` or visit the :doc:`usage` section for more info

Changelog
---------

1.1.0
^^^^^

-  Removed output to file option. Just use your shell’s file redirect
   syntax
-  Allowed for using JSON files in the header, parameters and form data
-  Added ability to attach files to requests
-  Removed debug flag, made it part of standard output
-  Added full error handling

Contents
--------

.. toctree::
   usage
