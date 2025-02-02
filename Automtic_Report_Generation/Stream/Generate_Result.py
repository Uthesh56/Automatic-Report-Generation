from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from transformers import pipeline
from langchain.llms import HuggingFacePipeline

def Get_Result(ResultedQuery):
    Pipe = pipeline("text-generation", model="openai-community/gpt2-large", max_token=100)
    Template = """
    ### Report on Relevant Data
        Based on the query, here is the relevant information:
        {ResultedQuery}
        Thank you for using the Report Generator.
    """

    PromptTemp = PromptTemplate(template=Template, input_variables=["Pass_Content"])
    Pipe = pipeline("text-generation", model="openai-community/gpt2-large", max_new_tokens=100)
    LLM = HuggingFacePipeline(pipeline=Pipe)
    Mod = LLMChain(llm=LLM, prompt=PromptTemp)
    Report = Mod.run(Pass_Content=ResultedQuery)
    return Report
