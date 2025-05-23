To find the actual game:
1. click the green code button on the top left
2. select 'download zip'
3. extract the zip
4. go to files/wastegen

install dependencies:
1. install python:
2. Download from the official python website here: https://www.python.org/downloads
3. Check if python is installed correctly by running `python3 --version` in a terminal
4. Follow the instructions for installing poetry from the official website: https://python-poetry.org/docs/#installing-with-pipx
   
If you want to run the game via helper scripts:
1. Mac/Linux: Double click the `run.sh` script or open it in the terminal via `./run.sh` with the current working directory set to the game's root directory.
2. Windows: Double click the `run.bat` script.
   
If you want to run the game via vscode:
1. open the ClanGen folder and run the following code snippet in the Visual Studio Code integrated terminal (Ctrl + ` to open the integrated terminal):
  ```
  poetry config virtualenvs.in-project true
  ```
2. Now run the following command to create a virtual environment:
  ```
  poetry install --no-root
  ```
3. It should have created a `.venv` folder in the root directory of the game.
  If you don't see it, remove existing poetry virtual environments by running `poetry env remove python` and try again.
4. After that, ensure that you have the Python extension installed in Visual Studio Code. You can install it from the Extensions tab on the left sidebar. [(or click here)
  ](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
5. Then, open the Command Palette (Ctrl+Shift+P) and search for `Python: Select Interpreter`. Select the virtual environment created by poetry (it should mention a `.venv` somewhere).
6. Finally, open the `main.py` file and click the play button in the top right corner to run the game.
