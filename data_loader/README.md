# Data Loader

This directory is responsible for 2 tasks:

1. Data ingestion and collection
   - Gather data from external knowledge sources such as Notion, google docs, slack, etc
   - Create "connectors"/ functions that can be called to pull data
   - Schedule data extraction
     - automate periodic extraction to keep knowledge base updated over time
2. Data Preprocessing step
   - cleaning and normalization
   - chunking
   - metadata tagging
