import os
import streamlit as st


def get_api_key():
    """Read the key from Streamlit secrets,
    or from an environment variable.
    """
    try:
        return st.secrets["MY_API_KEY"]
    except Exception:
        return os.environ.get("MY_API_KEY")


st.title("API key demo")

key = get_api_key()

if not key:
    st.warning(
        "No API key found. Add MY_API_KEY to your app's Secrets."
    )
    st.stop()

st.success("API key found.")

st.write(f"Key starts with: {key[:3]}***")
