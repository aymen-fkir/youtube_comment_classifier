import os
import dotenv
import requests
import pandas as pd


dotenv.load_dotenv()

def classify_comment(payload):
    API_URL = "https://api-inference.huggingface.co/models/martin-ha/toxic-comment-model"
    headers = {"Authorization": os.getenv("hugging_face_key")}
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()


def organise_comments(comments):
    labels = []
    score = []
    for comment in comments:
        class_cmt = classify_comment({"inputs":comment})
        if class_cmt[0][0]["score"] > class_cmt[0][1]["score"]:
            labels.append(class_cmt[0][0]["label"])
            score.append(class_cmt[0][0]["score"])
        else:
            labels.append(class_cmt[0][1]["label"])
            score.append(class_cmt[0][1]["score"])
    df = pd.DataFrame({"comment":comments,"label":labels,"score":score})
    return df


if __name__ == "__main__":
    comments = pd.read_csv("comments.csv")
    comments = comments["comments"].tolist()
    df = organise_comments(comments)
    df.to_csv("comments.csv",index=False)
# start using openai