# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="Hello",
        page_icon="👋",
    )

    st.write("# Welcome to the awesome Row Smasher! 👋")

    st.image("https://media2.giphy.com/media/0qiwSa0SwH8DTNjQyR/giphy.gif?cid=ecf05e47hw2vwfrxcc51m5i0sm7am01i1ana5kw9ng3q7dnj&ep=v1_gifs_search&rid=giphy.gif&ct=g", use_column_width=True)
  
    uploaded_file = st.file_uploader("Choose a file", type=['csv', 'xlsx'], accept_multiple_files=False)
   
    if st.button("Submit"):
        if uploaded_file:
            st.success("File submitted successfully!")
        else:
            st.warning("Please upload a file.")









if __name__ == "__main__":
    run()
