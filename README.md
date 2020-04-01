# Google Code Jam - Sandbox
This is a very simple repo, just to track my own solutions to the Code Jam historic problems.

I'm new to Code Jam, and I find the problems fun, so I'm going through the historic sets. 
I do not read the analysis section until after I have a working solution. The code in this repo reflects my initial thought. Usually I learn something clever by reading the "Analysis" section afterward (a humbling experience for sure)

## Running Tests
To match Google's environment, I'm using Docker.

### Python
At the time I'm getting started, Google's Python3 environment is 3.5. Notably, this is prior to f"strings".
From the directory where solution.py and input.txt sit:
```
cat ./input.txt |  docker run --rm -i -v "$PWD":/usr/src/myapp -w /usr/src/myapp python:3.5 python solution.py
```