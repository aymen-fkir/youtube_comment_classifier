import googleapiclient.discovery
import os
import dotenv
import getpass
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate

def classify_the_comment(comment):
    if "GOOGLE_API_KEY" not in os.environ:
        os.environ["GOOGLE_API_KEY"] = getpass.getpass("Provide your Google API Key")
    llm = ChatGoogleGenerativeAI(model="gemini-pro")
    prompt = PromptTemplate.from_template("classify this comment {cmt} base on these clases [remark,postive commet,negative comment]")
    result = llm.batch(prompt.format(cmt=comment))
    return result
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
        try:
            cmt = comment["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
            class_cmt = classify_the_comment(cmt)
            print(f"{cmt} : {class_cmt}")
        except:
            print(str(cmt)+" harmfull")    
# start using openai