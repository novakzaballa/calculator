""" Data layer code for handling OperationRecord entity """

from decimal import Decimal
import logging
from typing import List

from sqlalchemy import (
    BOOLEAN,
    NUMERIC,
    TIMESTAMP,
    VARCHAR,
    Column,
    Integer,
    func,
    text,
    update,
)

from src.data.db_connection import Base, get_db_session
from src.data.users import get_user_initial_balance
from src.model.aggregates.user_operation_record import OperationRecord


class OperationRecordData(Base):
    """Class that represents de model entity for the operation records"""

    __tablename__ = "operation_record"

    id = Column("id", Integer, primary_key=True, autoincrement="ignore_fk")
    operation_id = Column("operation_id", VARCHAR(50))
    user_id = Column("user_id", VARCHAR(128))
    amount = Column("amount", NUMERIC(10, 2))
    user_balance = Column("user_balance", NUMERIC(10, 2))
    operation_response = Column("operation_response", VARCHAR(250))
    date = Column("date", TIMESTAMP(timezone=True))
    deleted = Column("deleted", BOOLEAN)


def save_operation_record(operation_record: OperationRecord):
    """
    Saves the operation records to the service DynamoDB table.

    :param OperationRecord operation_record: OperationRecord model object built with the data needed
    """
    db_session = get_db_session()
    operation_record_data = OperationRecordData(**operation_record.dict(exclude={"id"}))
    db_session.add(operation_record_data)
    db_session.commit()


def get_user_balance(user_id: str) -> Decimal:
    """
    Retrieves the current user credit balance from operation_records

    :param str user_id: User ID
    :raises ValueError: When user not found in the DB
    :return Decimal: User's credit balance
    """

    db_session = get_db_session()

    last_balance = (
        db_session.query(OperationRecordData.user_balance)
        .filter(OperationRecordData.user_id == user_id)
        .order_by(OperationRecordData.date.desc())
        .limit(1)
        .scalar()
    )

    if last_balance is not None:
        return last_balance

    return get_user_initial_balance(user_id)


def get_user_operation_record_page(
    user_id: str,
    page_number: int,
    rows_per_page: int,
    sort_by: str = "date",
    sort_type: str = "desc",
    operation_id: str = None,
    show_deleted: bool = None,
) -> List[OperationRecord]:
    """
    Returns the paginated operation records of a user.

    :param str user_id: The ID of the User owning the operation records returned
    :param int page_number: The number of the page to be returned.
    :param int rows_per_page: The number of records per page.
    :return List[OperationRecord]: The page result set as a list of OperationRecord
    """

    db_session = get_db_session()

    start = rows_per_page * (page_number - 1)
    end = start + rows_per_page

    query = db_session.query(
        OperationRecordData.id,
        OperationRecordData.operation_id,
        OperationRecordData.amount,
        OperationRecordData.user_balance,
        OperationRecordData.operation_response,
        OperationRecordData.date,
        OperationRecordData.deleted,
        func.count(OperationRecordData.id).over().label("total"),
    ).filter(OperationRecordData.user_id == user_id)

    if operation_id:
        query = query.filter(OperationRecordData.operation_id == operation_id)

    if show_deleted is False:
        query = query.filter(OperationRecordData.deleted.is_(True))

    query = query.order_by(text(sort_by + " " + sort_type)).slice(start, end)

    result: List[OperationRecordData] = query.all()

    count = 0

    if len(result) > 0:
        count = result[0].total

    return [
        OperationRecord.from_orm(operation_record).dict(exclude={"user_id"})
        for operation_record in result
    ], count


def soft_delete_operation_record(operation_record_id: int):
    """
    Soft delete the operation record with the given ID

    :param int operation_record_id: Operation record ID to be soft deleted
    """

    db_session = get_db_session()
    statement = (
        update(OperationRecordData)
        .where(OperationRecordData.id == operation_record_id)
        .values(deleted=True)
    )

    db_session.execute(statement)
    db_session.commit()
