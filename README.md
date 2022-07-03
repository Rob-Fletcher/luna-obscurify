# luna-obscurify
Calculations to exactly cover the moon


## Installation
Clone the git repo, or download the file `luna_obscurify.py`. You also need to install the skyfield library. If you want to
serve the application with flask you also need to install that. They can both be installed with the requirements file.
```bash
pip install -r requirements.txt
```

## Usage
to use the program you just need to run the python script from the command line. Use the option `-d` to provide the 
diameter of the object used to obscure the moon in centimeters.

```bash
python luna_obscurify.py -d 5
```

To serve the flask app you can start the local server.
```bash
flask run
```
Then open the URL that is printed to the terminal.