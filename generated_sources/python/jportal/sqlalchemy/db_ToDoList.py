########################################################################################################################
################## Generated Code. DO NOT CHANGE THIS CODE. Change it in the generator and regenerate ##################
########################################################################################################################

from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Any, Optional
import enum
import sqlalchemy as sa
from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import TextAsFrom

from .common.db_common import DBMixin, Base, DBColumn
from .common import db_types
from .common.processing import process_result_recs, process_result_rec, process_bind_params




@dataclass
class DB_ToDoListSelectAll:
    # Enum for ListType field
    class ListTypeEnum(enum.Enum):
        Private = 1
        Public = 2

        @classmethod
        def process_result_value_cls(cls, value, dialect):
            return DB_ToDoListSelectAll.ListTypeEnum(value)


    #Outputs
    ID: int
    ListName: str
    ListType: ListTypeEnum
    Description: str
    LastUpdated: datetime

    @classmethod
    def get_statement(cls
                     ) -> TextAsFrom:
        class _ret:
            sequence = "default," #postgres uses default for sequences
            output = " OUTPUT (ID,ListName,ListType,Description,LastUpdated)"
            tail = " RETURNING ID ListName ListType Description LastUpdated"
            #session.bind.dialect.name

        statement = sa.text(
                        f"/* PROC ToDoList_App.ToDoList.SelectAll */"
                        f"select"
                        f"  ID"
                        f", ListName"
                        f", ListType"
                        f", Description"
                        f", LastUpdated"
                        f" from ToDoList_App.ToDoList")

        text_statement = statement.columns(ID=sa.types.Integer,
                                      ListName=db_types.NonNullableString,
                                      ListType=sa.types.SmallInteger,
                                      Description=db_types.NonNullableString,
                                      LastUpdated=sa.types.DateTime,
                                      )
        return text_statement

    @classmethod
    def execute(cls, session: Session) -> List['DB_ToDoListSelectAll']:
        res = session.execute(cls.get_statement())
        recs = res.fetchall()
        return process_result_recs(DB_ToDoListSelectAll, session, [sa.types.Integer,
                                        db_types.NonNullableString,
                                        DB_ToDoListSelectAll.ListTypeEnum,
                                        db_types.NonNullableString,
                                        sa.types.DateTime,
                                        ], recs)

@dataclass
class DB_ToDoListInsertReturning:
    # Enum for ListType field
    class ListTypeEnum(enum.Enum):
        Private = 1
        Public = 2

        @classmethod
        def process_result_value_cls(cls, value, dialect):
            return DB_ToDoListInsertReturning.ListTypeEnum(value)


    #Outputs
    ID: int

    @classmethod
    def get_statement(cls
                     , ListName: str
                     , ListType: ListTypeEnum
                     , Description: str
                     , LastUpdated: datetime
                     ) -> TextAsFrom:
        class _ret:
            sequence = "default," #postgres uses default for sequences
            output = ""
            tail = " RETURNING ID"
            #session.bind.dialect.name

        statement = sa.text(
                        f"/* PROC ToDoList_App.ToDoList.Insert */"
                        f"insert into ToDoList_App.ToDoList ("
                        f"  ID,"
                        f"  ListName,"
                        f"  ListType,"
                        f"  Description,"
                        f"  LastUpdated"
                        f" ) "
                        f"{_ret.output}"
                        f" values ("
                        f"{_ret.sequence}"
                        f"  :ListName,"
                        f"  :ListType,"
                        f"  :Description,"
                        f"  :LastUpdated"
                        f" )"
                        f"{_ret.tail}")

        text_statement = statement.columns(ID=sa.types.Integer,
                                      )
        text_statement = text_statement.bindparams(ListName=ListName,
                                         ListType=ListType,
                                         Description=Description,
                                         LastUpdated=LastUpdated,
                                         )
        return text_statement

    @classmethod
    def execute(cls, session: Session, ListName: str
                     , ListType: ListTypeEnum
                     , Description: str
                     , LastUpdated: datetime
                     ) -> Optional['DB_ToDoListInsertReturning']:
        params = process_bind_params(session, [db_types.NonNullableString,
                                        sa.types.SmallInteger,
                                        db_types.NonNullableString,
                                        sa.types.DateTime,
                                        ], [ListName,
                                        ListType.value if isinstance(ListType, enum.Enum) else ListType,
                                        Description,
                                        LastUpdated,
                                        ])
        res = session.execute(cls.get_statement(*params))
        rec = res.fetchone()
        if rec:
            res.close()
            return process_result_rec(DB_ToDoListInsertReturning, session, [sa.types.Integer,
                                        ], rec)

        return None

@dataclass
class DB_ToDoListUpdate:
    # Enum for ListType field
    class ListTypeEnum(enum.Enum):
        Private = 1
        Public = 2

        @classmethod
        def process_result_value_cls(cls, value, dialect):
            return DB_ToDoListUpdate.ListTypeEnum(value)


    

    @classmethod
    def get_statement(cls
                     , ListName: str
                     , ListType: ListTypeEnum
                     , Description: str
                     , LastUpdated: datetime
                     , ID: int
                     ) -> TextAsFrom:
        class _ret:
            sequence = "default," #postgres uses default for sequences
            output = ""
            tail = ""
            #session.bind.dialect.name

        statement = sa.text(
                        f"update ToDoList_App.ToDoList"
                        f" set"
                        f"  ListName = :ListName"
                        f", ListType = :ListType"
                        f", Description = :Description"
                        f", LastUpdated = :LastUpdated"
                        f" where ID = :ID")

        text_statement = statement.columns()
        text_statement = text_statement.bindparams(ListName=ListName,
                                         ListType=ListType,
                                         Description=Description,
                                         LastUpdated=LastUpdated,
                                         ID=ID,
                                         )
        return text_statement

    @classmethod
    def execute(cls, session: Session, ListName: str
                     , ListType: ListTypeEnum
                     , Description: str
                     , LastUpdated: datetime
                     , ID: int
                     ) -> None:
        params = process_bind_params(session, [db_types.NonNullableString,
                                        sa.types.SmallInteger,
                                        db_types.NonNullableString,
                                        sa.types.DateTime,
                                        sa.types.Integer,
                                        ], [ListName,
                                        ListType.value if isinstance(ListType, enum.Enum) else ListType,
                                        Description,
                                        LastUpdated,
                                        ID,
                                        ])
        res = session.execute(cls.get_statement(*params))
        res.close()

@dataclass
class DB_ToDoListSelectOne:
    # Enum for ListType field
    class ListTypeEnum(enum.Enum):
        Private = 1
        Public = 2

        @classmethod
        def process_result_value_cls(cls, value, dialect):
            return DB_ToDoListSelectOne.ListTypeEnum(value)


    #Outputs
    ListName: str
    ListType: ListTypeEnum
    Description: str
    LastUpdated: datetime

    @classmethod
    def get_statement(cls
                     , ID: int
                     ) -> TextAsFrom:
        class _ret:
            sequence = "default," #postgres uses default for sequences
            output = " OUTPUT (ListName,ListType,Description,LastUpdated)"
            tail = " RETURNING ListName ListType Description LastUpdated"
            #session.bind.dialect.name

        statement = sa.text(
                        f"/* PROC ToDoList_App.ToDoList.SelectOne */"
                        f"select"
                        f"  ListName"
                        f", ListType"
                        f", Description"
                        f", LastUpdated"
                        f" from ToDoList_App.ToDoList"
                        f" where ID = :ID")

        text_statement = statement.columns(ListName=db_types.NonNullableString,
                                      ListType=sa.types.SmallInteger,
                                      Description=db_types.NonNullableString,
                                      LastUpdated=sa.types.DateTime,
                                      )
        text_statement = text_statement.bindparams(ID=ID,
                                         )
        return text_statement

    @classmethod
    def execute(cls, session: Session, ID: int
                     ) -> Optional['DB_ToDoListSelectOne']:
        params = process_bind_params(session, [sa.types.Integer,
                                        ], [ID,
                                        ])
        res = session.execute(cls.get_statement(*params))
        rec = res.fetchone()
        if rec:
            res.close()
            return process_result_rec(DB_ToDoListSelectOne, session, [db_types.NonNullableString,
                                        DB_ToDoListSelectOne.ListTypeEnum,
                                        db_types.NonNullableString,
                                        sa.types.DateTime,
                                        ], rec)

        return None

@dataclass
class DB_ToDoListDeleteOne:
    

    @classmethod
    def get_statement(cls
                     , ID: int
                     ) -> TextAsFrom:
        class _ret:
            sequence = "default," #postgres uses default for sequences
            output = ""
            tail = ""
            #session.bind.dialect.name

        statement = sa.text(
                        f"/* PROC ToDoList_App.ToDoList.DeleteOne */"
                        f"delete from ToDoList_App.ToDoList"
                        f" where ID = :ID")

        text_statement = statement.columns()
        text_statement = text_statement.bindparams(ID=ID,
                                         )
        return text_statement

    @classmethod
    def execute(cls, session: Session, ID: int
                     ) -> None:
        params = process_bind_params(session, [sa.types.Integer,
                                        ], [ID,
                                        ])
        res = session.execute(cls.get_statement(*params))
        res.close()

@dataclass
class DB_ToDoListStaticData:
    

    @classmethod
    def get_statement(cls
                     ) -> TextAsFrom:
        class _ret:
            sequence = "default," #postgres uses default for sequences
            output = ""
            tail = ""
            #session.bind.dialect.name

        statement = sa.text(
                        f"INSERT INTO ToDoList_App.ToDoList(ListName,ListType,Description,LastUpdated) VALUES ('Takeon Test List 1', 1, 'Take on test list description', CURRENT_DATE )")

        text_statement = statement.columns()
        return text_statement

    @classmethod
    def execute(cls, session: Session) -> None:
        res = session.execute(cls.get_statement())
        res.close()
