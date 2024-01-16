from pandasai import SmartDataframe
import os
import dotenv
import pandas as pd
from pandasai.llm import OpenAI
dotenv.load_dotenv()

def get_conclusion(df):
    non_toxic = df[df.label == "non-toxic"]
    llm = OpenAI(api_token=os.getenv("openai_api"))
    pandas_ai = SmartDataframe(non_toxic.drop(columns=["comment"]),config={"llm":llm})
    #these will generate an image 
    conclusion = pandas_ai.chat("generate a chart based on this data . the chart must explain the score of toxicity of the comment. The x axe should be the index column and the y axe should be the score")
    return conclusion

if __name__ == "__main__":
    df = pd.read_csv("comments.csv")
    get_conclusion(df)