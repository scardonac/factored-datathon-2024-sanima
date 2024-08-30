from services.database_service import get_data
import pandas as pd
import streamlit as st

@st.cache_data
def process_data(data):
    """
    {
        "news": [
            {
                "event_code": "parametro a considerar",
                "summary": "string",
                "url": "string",
                "latitude": 0.0,
                "longitude": 0.0,
                "country": "string iso",
                "title": "string",
                "polarity_percent": 0,
                "fake_percent": 0,
                "facts": ["list strings"],
                "tags": ["list strings"],
                "keywords": [" list string"]
            }
        ],
        "general_summary": "string",
        "message": "string",
        "query_parameters": {
            "country": "string iso",
            "date_init": "date",
            "date_end": "date",
            "topics": ["string list"]
        }
    }
    """
    data = get_data()
    data["news"] = pd.DataFrame(data["news"])
    return data