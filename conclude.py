from pandasai import SmartDataframe
import pandasai.llm as llm
import os
import dotenv
import pandas as pd
dotenv.load_dotenv()

def get_conclusion(df):
    non_toxic = df[df.label == "non-toxic"]
    falcon = llm.GooglePalm(api_key=os.getenv("google_api_key"))
    pandas_ai = SmartDataframe(non_toxic,config={"llm":falcon})
    conclusion = pandas_ai.chat("summirse this and focus on the most import remarks")
    return conclusion

df = pd.read_csv("comments.csv")
conclu = get_conclusion(df)
print(conclu)