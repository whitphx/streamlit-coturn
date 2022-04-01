import logging
import os

import streamlit as st
from streamlit_coturn.server import run_coturn

logging.basicConfig(level=logging.DEBUG)

st.write("Hello")

heroku_app_name = os.environ.get('HEROKU_APP_NAME')
if heroku_app_name:
    server_name = f"https://{heroku_app_name}.herokuapp.com"
else:
    server_name = "localhost"

run_coturn(listening_port=3478, tls_listening_port=5349, fingerprint=True, lt_cred_mech=True, server_name=server_name, realm=server_name, user="quest:password")
