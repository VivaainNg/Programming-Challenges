## Project Euler

If you're interested to explore more about Project Euler challenges, head over to: https://projecteuler.net/


As per the FAQ in that site, each problem is designated to be solved under "1-minute rule". Usually, I'll solve a
problem the brute-force/direct way, before figuring out how to optimize it (time-complexity wise).


I've solved each problem for each file, based on problem's ID. I.e: Python solution for Problem #12 is problem_12.py.


## Run Python's solution


Directory structure:
```sh
python
├── solution
│   ├── __init__.py
│   └── problem_1.py
└── tests.py
```


Depending on what you're trying to run/test, you can do the following:


* If you're trying to get the output of a particular problem, say Problem 3, you can just run as so, assuming you're at the root of this project-euler subdirectory:
```sh
$ python python/solution/problem_3.py
```

* If you're trying to run the test suite encompassing ALL Project Euler's problems,
* (i) From project-euler/ root, you run as follows:
```sh
$ python -m unittest -v
```

* (i) From root of this repo, you run as follows:
```sh
$ python -m unittest discover ./project-euler/python -v
```
