from pandasai import SmartDataframe
import os
import dotenv
import pandas as pd
from pandasai.llm import OpenAI
dotenv.load_dotenv()

def get_conclusion(df):
    non_toxic = df[df.label == "non-toxic"]
    llm = OpenAI(api_token=os.getenv("openai_api"))
    pandas_ai = SmartDataframe(non_toxic,config={"llm":llm})
    conclusion = pandas_ai.chat("remove the usless comments that doesn't add any value")
    return conclusion

if __name__ == "__main__":
    df = pd.read_csv("comments.csv")
    conclu = get_conclusion(df)
    conclu.to_csv("conclusion.csv")