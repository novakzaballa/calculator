""" Database migration code to create DB tables and seed data """

from crhelper import CfnResource
from src.data.db_connection import create_db, engine
from src.data.operation_records import Base


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
    print("****** Creating/Updating Tables ******")
    Base.metadata.create_all(bind=engine)


@helper.create
def create(event, _context):
    """
    Perform DB migrations

    :param Dict event: Handler event
    :param Dict context: Handler context
    """
    print(event)
    print("******** Starting DB Migration *********")
    create_db()
    create_tables()
    print("******** DB Migration Completed *********")


@helper.update
def update(event, _context):
    """
    _summary_

    :param _type_ event: _description_
    :param _type_ context: _description_
    """
    print("******** DB Migration Update *********")
    print(event)



@helper.delete
def delete(event, _context):
    """
    _summary_

    :param _type_ event: _description_
    :param _type_ context: _description_
    """
    print("******** DB Migration Completed delete *********")
    print(event)
