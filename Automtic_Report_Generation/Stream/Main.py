import streamlit as Stream
import time
from Stream.GettingData import Process
from Stream.Store_Vector import Vector_Process
from Stream.Generate_Result import Get_Result
from Stream.ExportPdf import Export

def Main():
    Stream.title("Automatic Report Generator")
    Data = Process()
    if Data is not None:
        Query = Stream.text_input("Ask a Question: ")
        if Query:
            ResultedQuery = Vector_Process(Query, Data)
            Report = Get_Result(ResultedQuery)
            Export_Pdf = Export(Report)

if __name__ == "__main__":
    Main()