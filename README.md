flask-gemoji
============

Add gemojis to your Flask apps. See the LICENSE for copyright information.


Installation
============

``` shell
pip install flask-gemoji
```

Usage
=====

``` python
from flask import Flask
from flask_gemoji import Gemoji

app = Flask(__name__)
Gemoji.init_app(app)
```

``` html
<html>
<body>
    {{ content | gemoji }}
</body>
</html>
```
