from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.entity.artifact_entity import DataIngestionArtifact
from networksecurity.components.data_validation import DataValidation, DataValidationConfig
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
        logging.info("Data ingestion completed")
        data_validation_config=DataValidationConfig(training_pipeline_config)
        data_validation=DataValidation(dataingestion_artifact,data_validation_config)
        data_validation_artifact=data_validation.initiate_data_validation()
        logging.info("Data validation completed")


    except Exception as e:
           raise NetworkSecurityException(e,sys) 