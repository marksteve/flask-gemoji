============
flask-gemoji
============

.. image:: http://img.shields.io/pypi/v/flask-gemoji.png

Add gemojis to your Flask apps. See the LICENSE for copyright information.

------------
Installation
------------
::

    pip install flask-gemoji

-----
Usage
-----
::

    from flask import Flask
    from flask_gemoji import Gemoji
    
    app = Flask(__name__)
    Gemoji.init_app(app)


::

    <html>
    <body>
        {{ content | gemoji }}
    </body>
    </html>

