import googleapiclient.discovery
import os
import dotenv
import requests


def classify_the_comment(payload):
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


if __name__ == "__main__":
    comments = Get_comments()
    for comment in comments:
        cmt = comment["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
        class_cmt = classify_the_comment({"inputs":cmt,})
        print(f"{cmt} : {class_cmt}")
# start using openai