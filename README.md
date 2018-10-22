# imdb2mongodb
Importing raw IMDB datasets into MongoDB

(These are probably the worst scripts I've ever written, btw)

To import IMDB datasets into MongoDB, make sure you have MongoDB installed, obviously.

Then download pymongo for connecting to your mongodb instance. Change the connection strings if necessary.

Download the datasets with download_datasets.sh script

Then run python3 buildCollections/buildCollections.py and inform the directory with datasets as an argument to the script.

Enjoy.
