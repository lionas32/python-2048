# python-2048


<p align="center">
  <img src="demo.gif" />
</p>
<p align="center"><em>A terminal-based version of <a href="https://play2048.co/">2048</a> made in python.</em></p>

## Prequisites and Setup

Currently it only works for terminals which have support for 256 colors and unicode characters. The one used during development
is `iterm2`.

Requires the `asciimatics` and `numpy` packages. The versions used during development are declared in `requirements.txt`.
Install them by running the command below in the project directory:

```
pip3 install -r requirements.txt
```

The python version used during development is 3.9.7


Start the game with `python3 main.py`. 


## Further Ideas


The plan is to later clean up the project structure and provide a `setup.py` file. This will allow for simple installation of the project as a module. With this, we can start the game from any directory in the terminal.
