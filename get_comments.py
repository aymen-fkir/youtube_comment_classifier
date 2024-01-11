import dotenv
import googleapiclient.discovery
import os
import emoji
import pandas as pd
def Get_comments(limit_number,videoid):
    dotenv.load_dotenv()

    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = os.getenv("youtube_api_key")

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey = DEVELOPER_KEY)

    request = youtube.commentThreads().list(part="snippet",videoId=videoid,maxResults=limit_number)
    response = request.execute()
    comments = response["items"]
    cmts = []
    for comment in comments:
        cmt = comment["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
        cmt = emoji.demojize(cmt)
        cmts.append(cmt)
    return cmts
if __name__ == "__main__":
    videoid = "AKxPIWTQYys"
    cmts = Get_comments(10,videoid)
    df = pd.DataFrame(cmts,columns=["comments"])
    df.to_csv("comments.csv",index=False)