import googleapiclient.discovery
import os
import dotenv
import requests
import pandas as pd


def classify_comment(payload):
    API_URL = "https://api-inference.huggingface.co/models/martin-ha/toxic-comment-model"
    headers = {"Authorization": os.getenv("hugging_face_key")}
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()


def Get_comments():
    dotenv.load_dotenv()

    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = os.getenv("youtube_api_key")

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey = DEVELOPER_KEY)

    request = youtube.commentThreads().list(part="snippet",videoId="Hnjr7o-HNx8",maxResults=10)
    response = request.execute()
    return response["items"]

def organise_comments(comments):
    cmts = []
    labels = []
    score = []
    for comment in comments:
        cmt = comment["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
        cmts.append(cmt)
        class_cmt = classify_comment({"inputs":cmt,})
        if class_cmt[0][0]["score"] > class_cmt[0][1]["score"]:
            labels.append(class_cmt[0][0]["label"])
            score.append(class_cmt[0][0]["score"])
        else:
            labels.append(class_cmt[0][1]["label"])
            score.append(class_cmt[0][1]["score"])
    df = pd.DataFrame({"comment":cmts,"label":labels,"score":score})
    return df


if __name__ == "__main__":
    comments = Get_comments()
    df = organise_comments(comments)
    df.to_csv("comments.csv",index=False)
# start using openai