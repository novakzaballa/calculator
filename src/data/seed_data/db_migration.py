""" Database migration code to create DB tables and seed data """

import logging
from crhelper import CfnResource
from src.data.db_connection import create_db, engine
from src.data.operation_records import Base
from src.data.seed_data.seed_data_handler import initialize_seed_data


helper = CfnResource(json_logging=False, log_level="WARNING", boto_level="CRITICAL")


def handler(event, context):
    """
    Custom event handler. It trigger automatically when the stack is built

    :param event: AWS Event
    :param context: AWS Context
    """
    helper(event, context)


def create_tables():
    """
    Creates DB tables
    """
    logging.info("Creating/Updating Tables")
    Base.metadata.create_all(bind=engine)


@helper.create
def create(event, _context):
    """
    Perform DB migrations

    :param Dict event: Handler event
    :param Dict context: Handler context
    """
    logging.info("Starting DB Migration")
    logging.info("Creating AuroraDB database and tables")
    create_db()
    create_tables()
    logging.info("Creating DynamoDB table")
    initialize_seed_data()

    logging.info("******** DB Migration Completed *********")


@helper.update
def update(event, _context):
    """
    _summary_

    :param _type_ event: _description_
    :param _type_ context: _description_
    """
    logging.info("******** DB Migration Update *********")



@helper.delete
def delete(event, _context):
    """
    _summary_

    :param _type_ event: _description_
    :param _type_ context: _description_
    """
    logging.info("******** DB Migration Completed delete *********")
