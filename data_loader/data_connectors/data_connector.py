"""
Define a common interface that every data connector must implement.
"""
from abc import ABC, abstractmethod


class DataConnector(ABC):
    @abstractmethod
    def connect():
        """
        Establish a connection to its data source
        """
        pass

    @abstractmethod
    def extract():
        """
        Extract raw data
        """
        pass

    @abstractmethod
    def normalize():
        """
        Normalize or clean data into a consistent format
        """
        pass
