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
import csv

def process_uploaded_file(uploaded_file):
    # Read the file content
    file_content = uploaded_file.getvalue().decode("utf-8").splitlines()

    count = 0
    header = file_content[0]
    limit = 5000
    data = []
    file_counter = 0
    output_files = []

    for row in file_content:
        if count > limit:
            output_filename = f"output_{file_counter}.csv"
            with open(output_filename, "w") as f:
                # ...[the same processing code you provided, just skipping for brevity]...

            output_files.append(output_filename)
            count = 0
            file_counter += 1
            data = []
        else:
            data.append(row)
            count += 1

    return output_files

st.set_page_config(page_title="Row Smasher")

st.header("Row Smasher")

uploaded_file = st.file_uploader("Choose a file", type=['csv'], accept_multiple_files=False)

if uploaded_file:
    output_files = process_uploaded_file(uploaded_file)
    for file in output_files:
        with open(file, "r") as f:
            btn = st.download_button(
                label=f"Download {file}",
                data=f,
                file_name=file,
                mime="text/csv"
            )








if __name__ == "__main__":
    run()
