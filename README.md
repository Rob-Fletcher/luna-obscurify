# luna-obscurify
Calculations to exactly cover the moon


## Installation
Clone the git repo, or download the file `luna_obscurify.py`. You also need to install the skyfield library which you can 
do with:
```bash
pip install skyfield
# or
pip install -r requirements.txt
```

## Usage
to use the program you just need to run the python script from the command line. Use the option `-d` to provide the 
diameter of the object used to obscure the moon in centimeters.

```bash
python luna_obscurify.py -d 5
```