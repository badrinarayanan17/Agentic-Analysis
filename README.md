# Multi-Agent System for Real-Time Data Analysis

## Overview

This repository showcases a Multi-Agent System (MAS) designed to automate real-time data analysis on Reddit using various Large Language Models (LLMs). The system includes agents responsible for data collection, preprocessing, and model analysis, all integrated seamlessly using the `crewAI` framework.

## Table of Contents

- [Introduction](#introduction)
- [System Architecture](#system-architecture)
- [Model Evaluation](#model-evaluation)
- [Installation](#installation)
- [Usage](#usage)
- [Results](#results)
- [Conclusion](#conclusion)
- [Acknowledgement](#acknowledegment)

## Introduction

In the modern AI landscape, Multi-Agent Systems (MAS) are increasingly important for automating complex workflows. This project implements a MAS for real-time data analysis, focusing on sentiment analysis of Reddit data related to the 2024 Olympics. The system employs various LLMs to scrape data, preprocess it, and evaluate the performance of the models on sentiment analysis tasks.

## System Architecture

The architecture consists of three primary components: Agents, Tasks, and Tools. These elements are meshed together using the `crewAI` framework to automate the entire data analysis pipeline.

### Agents

1. **Data Collection Agent**
   - **Role:** Social Media Data Collector
   - **Goal:** Scrape real-time data from Reddit about the given topic (e.g., Olympics 2024).
   - **Backstory:** A dedicated data scraper specializing in social media information from Reddit.

2. **Preprocessing Agent**
   - **Role:** Data Preprocessor
   - **Goal:** Clean and preprocess the scraped social media data for subsequent analysis.
   - **Backstory:** A meticulous agent ensuring the data is ready for model analysis.

3. **Model Analysis Agent**
   - **Role:** Model Analyzer
   - **Goal:** Apply the specified LLM to the preprocessed data and evaluate its performance on sentiment analysis.
   - **Backstory:** An analytical expert focused on evaluating LLM performance.

### Tasks

1. **Data Collection Task**
   - **Description:** Scrape real-time data from Reddit on the specified topic, ensuring relevance and comprehensive coverage.
   - **Expected Output:** A dataset of comments related to the topic.
  
2. **Preprocessing Task**
   - **Description:** Clean and preprocess the scraped social media data, focusing on making it ready for analysis.
   - **Expected Output:** A clean, preprocessed dataset.
  
3. **Analyzer Task**
   - **Description:** Evaluate the given LLM model on the preprocessed data, focusing on metrics like accuracy, precision, recall, F1 score, etc.
   - **Expected Output:** An evaluation report in markdown format.

### Tools

1. **Serper Dev Tool**
   - **Functionality:** Interacts with Google indexes and Wikipedia articles to collect real-time data and provide accurate responses.
   - **Integration:** This tool is invoked within the Data Collection Agent to enhance its data-gathering capabilities.

## Model Evaluation

The LLM models evaluated in this project include:

1. **Llama3.1-70b-versatile**
2. **Llama3-70b-8192**
3. **Llama3-8b-8192**
3. **Gemma2-9b-it**
4. **Mixtral-8x7b-32768**

**Note:** The Gemma2-9b-it and Mixtral-8x7b-32768 models produced irrelevant responses, highlighting the importance of model selection for specific tasks. Rather than evaluating themselves, it gave the code to perform the task.

## Installation

To install the required dependencies, use the following command:

   - pip install crewai langchain_google_genai py-dotenv crewai_tools langchain_groq

## Python Dependency

   - To execute crewAI, you need to have python version more than 3.9. 3.10 or greater is recommendable.

## Usage

1. **Clone the repository:**

   git clone https://github.com/badrinarayanan17/Agentic-Analysis

   cd Agentic-Analysis

2. **Set up environment variables in a .env file**

   GOOGLE_API_KEY=your_google_api_key

   GROQ_API_KEY=your_groq_api_key

   SERPER_API_KEY=your_serper_api_key

3. **Run the System**
    
   python crew.py

4. **View the Output**

   The system will produce an evaluation report for the specified topic (e.g., Olympics 2024) using the selected LLM models. The report will include performance metrics such as accuracy, precision, recall, F1   
   score, and others.
   
## Results

The following metrics were used to evaluate the performance of the LLM models

  - Sentiment Analysis Accuracy, Precision, Recall, F1 Score, Perplexity, ROCAUC

### Llama3.1-70b-versatile LLM Model

  | Metric                      | Value  |
  |-----------------------------|--------|
  | Sentiment Analysis Accuracy | 92.1% |
  | Precision                   | 0.91   |
  | Recall                      | 0.93   |
  | F1 Score                    | 0.92   |
  | Perplexity                  | 12.5   |

## Conclusion

  This Multi-Agent System effectively automates the real-time data analysis workflow on Reddit, demonstrating the power of agentic approaches in AI. The Llama3.1-70b-versatile model showed the best overall   
  performance, making it particularly suitable for sentiment analysis tasks.

## Acknowledgement

  CrewAI Framework: For providing the tools necessary to build this MAS.

  Groq Cloud: For the LLM models used in this project.

  Serper Dev Tools: For real-time data collection capabilities.
