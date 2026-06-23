from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.entity.artifact_entity import DataIngestionArtifact
from networksecurity.entity.config_entity import DataIngestionConfig
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import TrainingPipelineConfig
from networksecurity.exception.exception import NetworkSecurityException
import sys

if __name__=='__main__':
    try:
        training_pipeline_config=TrainingPipelineConfig()
        data_ingestion_config=DataIngestionConfig(training_pipeline_config)
        data_ingestion=DataIngestion(data_ingestion_config)
        logging.info("Initiating data ingestion")
        dataingestion_artifact=data_ingestion.initiate_data_ingestion()
    except Exception as e:
           raise NetworkSecurityException(e,sys) 