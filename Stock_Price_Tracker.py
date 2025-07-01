{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPSmLYlVoKTTxOMwe/DyVkp",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/rpanchal126/devtraining-needit-utah/blob/main/Stock_Price_Tracker.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 10,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "wA-WscP4ul2e",
        "outputId": "9c99031a-c61f-4c1d-8c5d-468d1ff0771a"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "2025-07-01 22:08:52.754 WARNING streamlit.runtime.scriptrunner_utils.script_run_context: Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-07-01 22:08:52.757 WARNING streamlit.runtime.scriptrunner_utils.script_run_context: Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-07-01 22:08:52.903 \n",
            "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
            "  command:\n",
            "\n",
            "    streamlit run /usr/local/lib/python3.11/dist-packages/colab_kernel_launcher.py [ARGUMENTS]\n",
            "2025-07-01 22:08:52.906 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-07-01 22:08:52.909 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-07-01 22:08:52.912 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-07-01 22:08:52.914 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-07-01 22:08:52.917 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-07-01 22:08:52.919 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-07-01 22:08:52.921 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-07-01 22:08:52.924 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-07-01 22:08:52.926 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-07-01 22:08:52.928 Session state does not function when running a script without `streamlit run`\n",
            "2025-07-01 22:08:52.931 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-07-01 22:08:52.933 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-07-01 22:08:52.935 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-07-01 22:08:52.938 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-07-01 22:08:52.939 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-07-01 22:08:52.942 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-07-01 22:08:52.944 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-07-01 22:08:52.946 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-07-01 22:08:52.948 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-07-01 22:08:52.950 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-07-01 22:08:53.081 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-07-01 22:08:53.082 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-07-01 22:08:53.083 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
          ]
        }
      ],
      "source": [
        "import streamlit as st\n",
        "import requests\n",
        "import pandas as pd\n",
        "import matplotlib.pyplot as plt\n",
        "\n",
        "#Set page config\n",
        "st.set_page_config(page_title=\"Stock Prize Tracker\", layout=\"centered\")\n",
        "st.title(\"stock Prize tracket App\")\n",
        "st.write(\"track historical stock prizes with live chart\")\n",
        "\n",
        "#Input from User\n",
        "symbol = st.text_input(\"Enter Stock Symbol: \").upper()\n",
        "time_range = st.selectbox (\"Select Time Range: \", [\"Last 5 Years\", \"Last 1 Year\", \"Last 6 Months\", \"Last 1 Month\", \"Last Week\"])\n",
        "\n",
        "#Get today's date\n",
        "today = pd.Timestamp.now()\n",
        "\n",
        "#Filter based on Choice\n",
        "if time_range == \"Last 5 Years\":\n",
        "  start_date = today - pd.DateOffset(years=5)\n",
        "\n",
        "elif time_range == \"Last 1 Year\":\n",
        "  start_date = today - pd.DateOffset(years=1)\n",
        "\n",
        "elif time_range == \"Last 6 Months\":\n",
        "  start_date = today - pd.DateOffset(months=6)\n",
        "\n",
        "elif time_range == \"Last 1 Month\":\n",
        "  start_date = today - pd.DateOffset(months=1)\n",
        "\n",
        "else:\n",
        "  start_date = today - pd.DateOffset(weeks=1)\n",
        "\n",
        "#Enter your API details\n",
        "API_KEY = \"66351QX0KQ8XIC67\"\n",
        "\n",
        "#Ask for Stock Symbol\n",
        "#symbol = input(\"Enter your Stock Symbol: \").upper()\n",
        "\n",
        "#Define API Endpoint\n",
        "url = f\"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={API_KEY}&outputsize=full\"\n",
        "\n",
        "#Get the data\n",
        "response = requests.get(url)\n",
        "data = response.json()\n",
        "\n",
        "#Check if response is valid\n",
        "if \"Time Series (Daily)\" in data:\n",
        "  daily_data = data[\"Time Series (Daily)\"]\n",
        "\n",
        "  #Convert to dataframe\n",
        "  df = pd.DataFrame.from_dict(daily_data, orient=\"index\")\n",
        "  df = df.rename(columns={\n",
        "      \"1. open\": \"Open\",\n",
        "      \"2. high\": \"High\",\n",
        "      \"3. low\": \"Low\",\n",
        "      \"4. close\": \"Close\",\n",
        "      \"5. volume\": \"Volume\"\n",
        "  })\n",
        "\n",
        "  #Convert index to datetime and sort\n",
        "  df.index = pd.to_datetime(df.index)\n",
        "  df = df.sort_index()\n",
        "\n",
        "  #Convert Columns to Numeric\n",
        "  df = df.astype(float)\n",
        "\n",
        "\n",
        "  #Filter by selected time range\n",
        "  df_filtered = df[df.index >= start_date]\n",
        "\n",
        "  st.subheader(f\"Closing Prices for {symbol}\")\n",
        "  st.line_chart(df_filtered[\"Close\"])\n",
        "\n",
        "  st.write(f\"Average Closing Price:** ${df_filtered['Close'].mean():.2f}\")\n",
        "  st.write(f\"Maximum Closing Price:** ${df_filtered['Close'].max():.2f}\")\n",
        "  st.write(f\"Minimum Closing Price:** ${df_filtered['Close'].min():.2f}\")\n",
        "\n",
        "  #Show Raw Data Checkbox\n",
        "  if st.checkbox(\"Show Raw Data\"):\n",
        "      st.write(df_filtered.tail())\n",
        "\n",
        "else:\n",
        "  st.error(\"Invalid Stock Symbol\")\n",
        "\n"
      ]
    }
  ]
}