# Twitter-Media-Downloder

![alt text](https://github.com/Freshm4at/Twitter-Media-Downloder/blob/main/readme%20assets/downloading_in_progress.png)
![alt text](https://github.com/Freshm4at/Twitter-Media-Downloder/blob/main/readme%20assets/media_downloaded.png)

TMD or Twitter Media Download is a python script to download user's media from his favorite tweets and retweets.
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
$ python TDM.py 
```

## Where media are stored?
TDM will create a folder named after the target user in TDM project folder. 
Videos and images are respectively store in a subfolder.
ex : "./Asmongold/images" and "./Asmongold/videos"

## TDM download media since which date ?
Twitter uses a limit in the data collect. This limitation is 200 tweets by request. But TDM pass throught this limitation and go get all favorite tweets and retweets.

## Usage
```
$ python TDM.py -k "YOUR_BEARER_KEY" TARGET_USER
usage:  [-k] user

positional arguments:
  user                  the target user from who you want media 
                        
additionnal arguments:
  -h, --help                                  show this help message and exit
  -k "BEARER_KEY", --key "BEARER_KEY"         Your bearer key, given from Twitter.Inc in the developper plateform. 

```
