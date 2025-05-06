import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    VOYAGEAI_API_KEY    = os.getenv("VOYAGEAI_API_KEY")
    KDBAI_ENDPOINT      = os.getenv("KDBAI_ENDPOINT")
    KDBAI_API_KEY       = os.getenv("KDBAI_API_KEY")
    MODEL_NAME          = os.getenv("VOYAGEAI_MODEL_NAME")
    GEMINI_API_KEY      = os.getenv("GEMINI_API_KEY")
    GEMINI_MODEL_NAME   = os.getenv("GEMINI_MODEL_NAME")
