Packaging
=========


Create a wheel
--------------
```
$ python3 setup.py bdist_wheel
```

Upload to PyPi
--------------
```
$ python setup.py register bdist_wheel upload 
```

Update package info
-------------------
```
$ python setup.py register
```

Run tests
---------
```
$ python setup.py test
```
