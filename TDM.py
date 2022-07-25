import requests
from colorama import init,Fore,Style
import shutil
import os
import argparse
from alive_progress import alive_bar

def GetJson(payload,url,autorization) :
    headers = {"Authorization": f"Bearer {autorization}"}
    payload = payload
    r = requests.get(url, headers=headers, params=payload)
    if r.status_code == 200:
        tweets = r.json()
    else:
        print(
            "An error occurred with the request,"
            + f"the status code was {r.status_code}"
        )
        tweets = []
    return tweets
def save_file(url,ddir):
    if url:
        name = url.split('/')[-1].split("?")[0]
        op_dir = os.path.join(ddir, name)
        with requests.get(url, stream=True) as r:
            with open(op_dir, 'wb') as f:
                shutil.copyfileobj(r.raw, f)

def fillList(videos,images,media):
    mediaType = media[0]["type"]
    if mediaType == "video":
        videos.append(media[0]['video_info']['variants'][0]['url'])
    elif mediaType == "photo":
        if len(media)>1:
            for elem in media:
                images.append(elem["media_url"])
        else: 
            images.append(media[0]["media_url"])
    return [videos,images]     


def getUrl(lenght,user,autorization):
    videos = []
    images = []
    fav = "https://api.twitter.com/1.1/favorites/list.json"
    rt = "https://api.twitter.com/1.1/statuses/user_timeline.json"
    LauchPayloadVideoFAV = {
        "screen_name": user,
        "count": 200,
    }
    LauchPayloadRT = {
        "screen_name": user,
        "count": 200,
        "include_rts": "true",
    }
    lastid = 0
    
    for i in range(1,lenght):
        if (i!=1):
            LauchPayloadVideoFAV["max_id"] = lastid
        tweets = GetJson(LauchPayloadVideoFAV,fav,autorization)
        for tweet in tweets:
            if "media" in tweet["entities"]:
                media = tweet['extended_entities']['media']
                temp = fillList(videos,images,media)
                videos = temp[0]
                images = temp[1]
            if "quoted_status" in tweet and "media" in tweet["quoted_status"]["entities"]:
                media = tweet["quoted_status"]["extended_entities"]["media"]
                temp = fillList(videos,images,media)
                videos = temp[0]
                images = temp[1]          
            lastid = tweet["id"]
        i=i+1

    for i in range(1,lenght):
        if (i!=1):
            LauchPayloadRT["max_id"] = lastid
        tweets = GetJson(LauchPayloadRT,rt,autorization)
        for tweet in tweets:
            if "retweeted_status" in tweet:
                if "media" in tweet["retweeted_status"]["entities"]:
                    media = tweet["retweeted_status"]["extended_entities"]["media"]  
                    temp = fillList(videos,images,media)
                    videos = temp[0]
                    images = temp[1]     
                if "quoted_status" in tweet:
                    if "media" in tweet["retweeted_status"]["quoted_status"]["entities"]:
                        media = tweet["retweeted_status"]["quoted_status"]["extended_entities"]["media"] 
                        temp = fillList(videos,images,media)
                        videos = temp[0]
                        images = temp[1] 
            lastid = tweet["id"]
        i=i+1
    return [images,videos]

parser = argparse.ArgumentParser()
parser.add_argument('user', type=str, help = 'The target user (screen name, ex : @xxx)')
parser.add_argument('-k', '--key',type=str,dest = 'key',help = 'Your Bearer key from Twitter')
args = parser.parse_args()

data = getUrl(10,args.user,args.key)
imagesNumber = len(data[0])
videosNumber = len(data[1])

currentFolder = os.getcwd()
Path=currentFolder+"\\"+args.user
if(os.path.exists(Path) == False or os.path.exists(Path) == False ):
    os.mkdir(Path)
    os.mkdir(Path+"\\images")
    os.mkdir(Path+"\\videos")

print('['+Fore.YELLOW +'...' + Style.BRIGHT+Style.RESET_ALL+']' + 'Downloading images, wait ...\n')
for x in [imagesNumber]:
    with alive_bar(x) as bar:
        for elem in data[0]:
            save_file(elem,Path+"\\images")
            bar()
print(" ")
print('['+Fore.GREEN+'+'+Style.RESET_ALL+'] '+Fore.GREEN, imagesNumber,'videos'+Style.RESET_ALL+ ' successfully saved in ...\\'+args.user+'\\images" !\n')
print('['+Fore.YELLOW +'...' +Style.BRIGHT+Style.RESET_ALL+']' + 'Downloading videos, wait ...\n')
for x in [videosNumber]:
    with alive_bar(x) as bar:
        for elem in data[1]:
            save_file(elem,Path+"\\videos")
            bar()
print(" ")
print('['+Fore.GREEN+'+'+Style.RESET_ALL+'] '+Fore.GREEN,videosNumber, 'videos'+Style.RESET_ALL+ ' successfully saved in ...\\'+args.user+'\\videos" !\n')
