# Twitter-Media-Downloder
TMD or Twitter Media Download is a python script to download user's media from his favorite tweets and retweet.
Downloaded medias include images and videos from fav and retweet tweets.

TDM also downloads media from quoted fav/rt tweets.

## Setup
1) Clone the repository

```
$ git clone https://github.com/Freshm4at/Twitter-Media-Downloder/
```

2) Install the dependencies

```
$ cd Twitter-Media-Downloder
$ pip install -r requirements.txt
```

3) Run Twitter-Media-Downloder

```
$ python TMD.py 
```

## Usage
```
$ python -k "YOUR_BEARER_KEY" TARGET_USER
usage:  [-k] user

positional arguments:
  user                  the target user from who you want media 
                        
additionnal arguments:
  -h, --help                                  show this help message and exit
  -k "BEARER_KEY", --key "BEARER_KEY"         Your bearer key, given from Twitter.Inc in the developper plateform. 

```
