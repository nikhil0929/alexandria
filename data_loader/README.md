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

3. Abstract Base Class for Connectors
   Purpose:
   Define a common interface that every data connector must implement. This interface ensures that no matter the source, each connector can:

Establish a connection to its data source.
Extract raw data.
Normalize or clean that data into a consistent format.
Methods (Conceptually):

connect(): Establish a connection to the data source (authentication, API setup, etc.).
extract(): Retrieve the raw data from the source.
normalize(): Convert the raw data into a common internal format that your application can work with (e.g., a standardized document or record structure).
Design Pattern:
This approach aligns with the Template Method pattern, where the abstract class defines the skeleton of the operation and concrete classes fill in the details.

2. Concrete Connector Classes
   Examples:
   GoogleDocsConnector
   NotionConnector
   SlackConnector
   Responsibility:
   Each concrete class implements the methods defined by the abstract connector. For example:
   A GoogleDocsConnector would handle OAuth and API calls to Google Docs, extract document content, and format it into your standard structure.
   A SlackConnector might fetch message logs, parse thread structures, and clean up timestamps or user mentions.
