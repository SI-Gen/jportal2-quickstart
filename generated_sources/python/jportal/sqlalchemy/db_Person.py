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
class DB_PersonInsertReturning:
    # Enum for Gender field
    class GenderEnum(enum.Enum):
        Male = 1
        Female = 2
        Unspecified = 3

        @classmethod
        def process_result_value_cls(cls, value, dialect):
            return DB_PersonInsertReturning.GenderEnum(value)


    #Outputs
    ID: int

    @classmethod
    def get_statement(cls
                     , FirstName: str
                     , MiddleName: str
                     , Surname: str
                     , IDNumber: str
                     , Gender: GenderEnum
                     , DateOfBirth: datetime
                     , LastUpdated: datetime
                     ) -> TextAsFrom:
        class _ret:
            sequence = "default," #postgres uses default for sequences
            output = ""
            tail = " RETURNING ID"
            #session.bind.dialect.name

        statement = sa.text(
                        f"/* PROC ToDoList_App.Person.Insert */"
                        f"insert into ToDoList_App.Person ("
                        f"  ID,"
                        f"  FirstName,"
                        f"  MiddleName,"
                        f"  Surname,"
                        f"  IDNumber,"
                        f"  Gender,"
                        f"  DateOfBirth,"
                        f"  LastUpdated"
                        f" ) "
                        f"{_ret.output}"
                        f" values ("
                        f"{_ret.sequence}"
                        f"  :FirstName,"
                        f"  :MiddleName,"
                        f"  :Surname,"
                        f"  :IDNumber,"
                        f"  :Gender,"
                        f"  :DateOfBirth,"
                        f"  :LastUpdated"
                        f" )"
                        f"{_ret.tail}")

        text_statement = statement.columns(ID=sa.types.Integer,
                                      )
        text_statement = text_statement.bindparams(FirstName=FirstName,
                                         MiddleName=MiddleName,
                                         Surname=Surname,
                                         IDNumber=IDNumber,
                                         Gender=Gender,
                                         DateOfBirth=DateOfBirth,
                                         LastUpdated=LastUpdated,
                                         )
        return text_statement

    @classmethod
    def execute(cls, session: Session, FirstName: str
                     , MiddleName: str
                     , Surname: str
                     , IDNumber: str
                     , Gender: GenderEnum
                     , DateOfBirth: datetime
                     , LastUpdated: datetime
                     ) -> Optional['DB_PersonInsertReturning']:
        params = process_bind_params(session, [db_types.NonNullableString,
                                        db_types.NonNullableString,
                                        db_types.NonNullableString,
                                        db_types.NonNullableString,
                                        sa.types.SmallInteger,
                                        sa.types.DateTime,
                                        sa.types.DateTime,
                                        ], [FirstName,
                                        MiddleName,
                                        Surname,
                                        IDNumber,
                                        Gender.value if isinstance(Gender, enum.Enum) else Gender,
                                        DateOfBirth,
                                        LastUpdated,
                                        ])
        res = session.execute(cls.get_statement(*params))
        rec = res.fetchone()
        if rec:
            res.close()
            return process_result_rec(DB_PersonInsertReturning, session, [sa.types.Integer,
                                        ], rec)

        return None

@dataclass
class DB_PersonUpdate:
    # Enum for Gender field
    class GenderEnum(enum.Enum):
        Male = 1
        Female = 2
        Unspecified = 3

        @classmethod
        def process_result_value_cls(cls, value, dialect):
            return DB_PersonUpdate.GenderEnum(value)


    

    @classmethod
    def get_statement(cls
                     , FirstName: str
                     , MiddleName: str
                     , Surname: str
                     , IDNumber: str
                     , Gender: GenderEnum
                     , DateOfBirth: datetime
                     , LastUpdated: datetime
                     , ID: int
                     ) -> TextAsFrom:
        class _ret:
            sequence = "default," #postgres uses default for sequences
            output = ""
            tail = ""
            #session.bind.dialect.name

        statement = sa.text(
                        f"update ToDoList_App.Person"
                        f" set"
                        f"  FirstName = :FirstName"
                        f", MiddleName = :MiddleName"
                        f", Surname = :Surname"
                        f", IDNumber = :IDNumber"
                        f", Gender = :Gender"
                        f", DateOfBirth = :DateOfBirth"
                        f", LastUpdated = :LastUpdated"
                        f" where ID = :ID")

        text_statement = statement.columns()
        text_statement = text_statement.bindparams(FirstName=FirstName,
                                         MiddleName=MiddleName,
                                         Surname=Surname,
                                         IDNumber=IDNumber,
                                         Gender=Gender,
                                         DateOfBirth=DateOfBirth,
                                         LastUpdated=LastUpdated,
                                         ID=ID,
                                         )
        return text_statement

    @classmethod
    def execute(cls, session: Session, FirstName: str
                     , MiddleName: str
                     , Surname: str
                     , IDNumber: str
                     , Gender: GenderEnum
                     , DateOfBirth: datetime
                     , LastUpdated: datetime
                     , ID: int
                     ) -> None:
        params = process_bind_params(session, [db_types.NonNullableString,
                                        db_types.NonNullableString,
                                        db_types.NonNullableString,
                                        db_types.NonNullableString,
                                        sa.types.SmallInteger,
                                        sa.types.DateTime,
                                        sa.types.DateTime,
                                        sa.types.Integer,
                                        ], [FirstName,
                                        MiddleName,
                                        Surname,
                                        IDNumber,
                                        Gender.value if isinstance(Gender, enum.Enum) else Gender,
                                        DateOfBirth,
                                        LastUpdated,
                                        ID,
                                        ])
        res = session.execute(cls.get_statement(*params))
        res.close()

@dataclass
class DB_PersonSelectOne:
    # Enum for Gender field
    class GenderEnum(enum.Enum):
        Male = 1
        Female = 2
        Unspecified = 3

        @classmethod
        def process_result_value_cls(cls, value, dialect):
            return DB_PersonSelectOne.GenderEnum(value)


    #Outputs
    FirstName: str
    MiddleName: str
    Surname: str
    IDNumber: str
    Gender: GenderEnum
    DateOfBirth: datetime
    LastUpdated: datetime

    @classmethod
    def get_statement(cls
                     , ID: int
                     ) -> TextAsFrom:
        class _ret:
            sequence = "default," #postgres uses default for sequences
            output = " OUTPUT (FirstName,MiddleName,Surname,IDNumber,Gender,DateOfBirth,LastUpdated)"
            tail = " RETURNING FirstName MiddleName Surname IDNumber Gender DateOfBirth LastUpdated"
            #session.bind.dialect.name

        statement = sa.text(
                        f"/* PROC ToDoList_App.Person.SelectOne */"
                        f"select"
                        f"  FirstName"
                        f", MiddleName"
                        f", Surname"
                        f", IDNumber"
                        f", Gender"
                        f", DateOfBirth"
                        f", LastUpdated"
                        f" from ToDoList_App.Person"
                        f" where ID = :ID")

        text_statement = statement.columns(FirstName=db_types.NonNullableString,
                                      MiddleName=db_types.NonNullableString,
                                      Surname=db_types.NonNullableString,
                                      IDNumber=db_types.NonNullableString,
                                      Gender=sa.types.SmallInteger,
                                      DateOfBirth=sa.types.DateTime,
                                      LastUpdated=sa.types.DateTime,
                                      )
        text_statement = text_statement.bindparams(ID=ID,
                                         )
        return text_statement

    @classmethod
    def execute(cls, session: Session, ID: int
                     ) -> Optional['DB_PersonSelectOne']:
        params = process_bind_params(session, [sa.types.Integer,
                                        ], [ID,
                                        ])
        res = session.execute(cls.get_statement(*params))
        rec = res.fetchone()
        if rec:
            res.close()
            return process_result_rec(DB_PersonSelectOne, session, [db_types.NonNullableString,
                                        db_types.NonNullableString,
                                        db_types.NonNullableString,
                                        db_types.NonNullableString,
                                        DB_PersonSelectOne.GenderEnum,
                                        sa.types.DateTime,
                                        sa.types.DateTime,
                                        ], rec)

        return None

@dataclass
class DB_PersonDeleteOne:
    

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
                        f"/* PROC ToDoList_App.Person.DeleteOne */"
                        f"delete from ToDoList_App.Person"
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
class DB_PersonSelectOneByIDNumber:
    # Enum for Gender field
    class GenderEnum(enum.Enum):
        Male = 1
        Female = 2
        Unspecified = 3

        @classmethod
        def process_result_value_cls(cls, value, dialect):
            return DB_PersonSelectOneByIDNumber.GenderEnum(value)


    #Outputs
    ID: int
    FirstName: str
    MiddleName: str
    Surname: str
    IDNumber: str
    Gender: GenderEnum
    DateOfBirth: datetime
    LastUpdated: datetime

    @classmethod
    def get_statement(cls
                     , IDNumber: str
                     ) -> TextAsFrom:
        class _ret:
            sequence = "default," #postgres uses default for sequences
            output = " OUTPUT (ID,FirstName,MiddleName,Surname,IDNumber,Gender,DateOfBirth,LastUpdated)"
            tail = " RETURNING ID FirstName MiddleName Surname IDNumber Gender DateOfBirth LastUpdated"
            #session.bind.dialect.name

        statement = sa.text(
                        f"/* PROC ToDoList_App.Person.SelectOneByIDNumber */"
                        f"select"
                        f"  ID"
                        f", FirstName"
                        f", MiddleName"
                        f", Surname"
                        f", IDNumber"
                        f", Gender"
                        f", DateOfBirth"
                        f", LastUpdated"
                        f" from ToDoList_App.Person"
                        f" where IDNumber = :IDNumber")

        text_statement = statement.columns(ID=sa.types.Integer,
                                      FirstName=db_types.NonNullableString,
                                      MiddleName=db_types.NonNullableString,
                                      Surname=db_types.NonNullableString,
                                      IDNumber=db_types.NonNullableString,
                                      Gender=sa.types.SmallInteger,
                                      DateOfBirth=sa.types.DateTime,
                                      LastUpdated=sa.types.DateTime,
                                      )
        text_statement = text_statement.bindparams(IDNumber=IDNumber,
                                         )
        return text_statement

    @classmethod
    def execute(cls, session: Session, IDNumber: str
                     ) -> Optional['DB_PersonSelectOneByIDNumber']:
        params = process_bind_params(session, [db_types.NonNullableString,
                                        ], [IDNumber,
                                        ])
        res = session.execute(cls.get_statement(*params))
        rec = res.fetchone()
        if rec:
            res.close()
            return process_result_rec(DB_PersonSelectOneByIDNumber, session, [sa.types.Integer,
                                        db_types.NonNullableString,
                                        db_types.NonNullableString,
                                        db_types.NonNullableString,
                                        db_types.NonNullableString,
                                        DB_PersonSelectOneByIDNumber.GenderEnum,
                                        sa.types.DateTime,
                                        sa.types.DateTime,
                                        ], rec)

        return None

@dataclass
class DB_PersonSelectByGender:
    # Enum for Gender field
    class GenderEnum(enum.Enum):
        Male = 1
        Female = 2
        Unspecified = 3

        @classmethod
        def process_result_value_cls(cls, value, dialect):
            return DB_PersonSelectByGender.GenderEnum(value)


    # Enum for Gender field
    class GenderEnum(enum.Enum):
        Male = 1
        Female = 2
        Unspecified = 3

        @classmethod
        def process_result_value_cls(cls, value, dialect):
            return DB_PersonSelectByGender.GenderEnum(value)


    #Outputs
    ID: int
    FirstName: str
    MiddleName: str
    Surname: str
    IDNumber: str
    Gender: GenderEnum
    DateOfBirth: datetime
    LastUpdated: datetime

    @classmethod
    def get_statement(cls
                     , Gender: GenderEnum
                     ) -> TextAsFrom:
        class _ret:
            sequence = "default," #postgres uses default for sequences
            output = " OUTPUT (ID,FirstName,MiddleName,Surname,IDNumber,Gender,DateOfBirth,LastUpdated)"
            tail = " RETURNING ID FirstName MiddleName Surname IDNumber Gender DateOfBirth LastUpdated"
            #session.bind.dialect.name

        statement = sa.text(
                        f"/* PROC ToDoList_App.Person.SelectByGender */"
                        f"select"
                        f"  ID"
                        f", FirstName"
                        f", MiddleName"
                        f", Surname"
                        f", IDNumber"
                        f", Gender"
                        f", DateOfBirth"
                        f", LastUpdated"
                        f" from ToDoList_App.Person"
                        f" where Gender = :Gender")

        text_statement = statement.columns(ID=sa.types.Integer,
                                      FirstName=db_types.NonNullableString,
                                      MiddleName=db_types.NonNullableString,
                                      Surname=db_types.NonNullableString,
                                      IDNumber=db_types.NonNullableString,
                                      Gender=sa.types.SmallInteger,
                                      DateOfBirth=sa.types.DateTime,
                                      LastUpdated=sa.types.DateTime,
                                      )
        text_statement = text_statement.bindparams(Gender=Gender,
                                         )
        return text_statement

    @classmethod
    def execute(cls, session: Session, Gender: GenderEnum
                     ) -> List['DB_PersonSelectByGender']:
        params = process_bind_params(session, [sa.types.SmallInteger,
                                        ], [Gender.value if isinstance(Gender, enum.Enum) else Gender,
                                        ])
        res = session.execute(cls.get_statement(*params))
        recs = res.fetchall()
        return process_result_recs(DB_PersonSelectByGender, session, [sa.types.Integer,
                                        db_types.NonNullableString,
                                        db_types.NonNullableString,
                                        db_types.NonNullableString,
                                        db_types.NonNullableString,
                                        DB_PersonSelectByGender.GenderEnum,
                                        sa.types.DateTime,
                                        sa.types.DateTime,
                                        ], recs)

@dataclass
class DB_PersonSelectNameSurnameByGender:
    # Enum for Gender field
    class GenderEnum(enum.Enum):
        Male = 1
        Female = 2
        Unspecified = 3

        @classmethod
        def process_result_value_cls(cls, value, dialect):
            return DB_PersonSelectNameSurnameByGender.GenderEnum(value)


    #Outputs
    FirstName: str
    Surname: str

    @classmethod
    def get_statement(cls
                     , Gender: GenderEnum
                     ) -> TextAsFrom:
        class _ret:
            sequence = "default," #postgres uses default for sequences
            output = " OUTPUT (FirstName,Surname)"
            tail = " RETURNING FirstName Surname"
            #session.bind.dialect.name

        statement = sa.text(
                        f"/* PROC ToDoList_App.Person.SelectNameSurnameByGender */"
                        f"select"
                        f"  FirstName"
                        f", Surname"
                        f" from ToDoList_App.Person"
                        f" where Gender = :Gender")

        text_statement = statement.columns(FirstName=db_types.NonNullableString,
                                      Surname=db_types.NonNullableString,
                                      )
        text_statement = text_statement.bindparams(Gender=Gender,
                                         )
        return text_statement

    @classmethod
    def execute(cls, session: Session, Gender: GenderEnum
                     ) -> List['DB_PersonSelectNameSurnameByGender']:
        params = process_bind_params(session, [sa.types.SmallInteger,
                                        ], [Gender.value if isinstance(Gender, enum.Enum) else Gender,
                                        ])
        res = session.execute(cls.get_statement(*params))
        recs = res.fetchall()
        return process_result_recs(DB_PersonSelectNameSurnameByGender, session, [db_types.NonNullableString,
                                        db_types.NonNullableString,
                                        ], recs)

@dataclass
class DB_PersonSelectNameSurnameAndGenderAsStringByIDNumber:
    #Outputs
    FirstName: str
    Surname: str
    Gender: str

    @classmethod
    def get_statement(cls
                     , IDNumber: str
                     ) -> TextAsFrom:
        class _ret:
            sequence = "default," #postgres uses default for sequences
            output = " OUTPUT (FirstName,Surname,Gender)"
            tail = " RETURNING FirstName Surname Gender"
            #session.bind.dialect.name

        statement = sa.text(
                        f"/* PROC ToDoList_App.Person.SelectNameSurnameAndGenderAsStringByIDNumber */"
                        f"SELECT "
                        f"FirstName, "
                        f"Surname, "
                        f"CASE "
                        f"WHEN Gender = 1 THEN 'Male' "
                        f"WHEN Gender = 2 THEN 'Female' "
                        f"WHEN Gender = 3 THEN 'Unspecified' "
                        f"END "
                        f"FROM "
                        f"Person "
                        f"WHERE "
                        f"IDNumber = :IDNumber ")

        text_statement = statement.columns(FirstName=db_types.NonNullableString,
                                      Surname=db_types.NonNullableString,
                                      Gender=db_types.NonNullableString,
                                      )
        text_statement = text_statement.bindparams(IDNumber=IDNumber,
                                         )
        return text_statement

    @classmethod
    def execute(cls, session: Session, IDNumber: str
                     ) -> List['DB_PersonSelectNameSurnameAndGenderAsStringByIDNumber']:
        params = process_bind_params(session, [db_types.NonNullableString,
                                        ], [IDNumber,
                                        ])
        res = session.execute(cls.get_statement(*params))
        recs = res.fetchall()
        return process_result_recs(DB_PersonSelectNameSurnameAndGenderAsStringByIDNumber, session, [db_types.NonNullableString,
                                        db_types.NonNullableString,
                                        db_types.NonNullableString,
                                        ], recs)

@dataclass
class DB_PersonSelectWithDynamicQuery:
    # Enum for Gender field
    class GenderEnum(enum.Enum):
        Male = 1
        Female = 2
        Unspecified = 3

        @classmethod
        def process_result_value_cls(cls, value, dialect):
            return DB_PersonSelectWithDynamicQuery.GenderEnum(value)


    #Outputs
    FirstName: str
    Surname: str
    Gender: str

    @classmethod
    def get_statement(cls
                     , Gender: GenderEnum
                     , MyDynamicWhereClause: str) -> TextAsFrom:
        class _ret:
            sequence = "default," #postgres uses default for sequences
            output = " OUTPUT (FirstName,Surname,Gender)"
            tail = " RETURNING FirstName Surname Gender"
            #session.bind.dialect.name

        statement = sa.text(
                        f"/* PROC ToDoList_App.Person.SelectWithDynamicQuery */"
                        f"SELECT "
                        f"FirstName, "
                        f"Surname, "
                        f" "
                        f"SQLCODE "
                        f"SELECT "
                        f"FirstName "
                        f",Surname "
                        f",Gender "
                        f"FROM "
                        f"ToDoList_App.Person "
                        f"WHERE "
                        f"Gender = :Gender "
                        f"AND  "
                        f"{MyDynamicWhereClause}"
                        f" ")

        text_statement = statement.columns(FirstName=db_types.NonNullableString,
                                      Surname=db_types.NonNullableString,
                                      Gender=db_types.NonNullableString,
                                      )
        text_statement = text_statement.bindparams(Gender=Gender,
                                         )
        return text_statement

    @classmethod
    def execute(cls, session: Session, Gender: GenderEnum
                     , MyDynamicWhereClause: str) -> List['DB_PersonSelectWithDynamicQuery']:
        params = process_bind_params(session, [sa.types.SmallInteger,
                                        db_types.NonNullableString,], [Gender.value if isinstance(Gender, enum.Enum) else Gender,
                                        MyDynamicWhereClause,])
        res = session.execute(cls.get_statement(*params))
        recs = res.fetchall()
        return process_result_recs(DB_PersonSelectWithDynamicQuery, session, [db_types.NonNullableString,
                                        db_types.NonNullableString,
                                        db_types.NonNullableString,
                                        ], recs)

@dataclass
class DB_PersonStaticData:
    

    @classmethod
    def get_statement(cls
                     ) -> TextAsFrom:
        class _ret:
            sequence = "default," #postgres uses default for sequences
            output = ""
            tail = ""
            #session.bind.dialect.name

        statement = sa.text(
                        f"INSERT INTO ToDoList_App.Person(FirstName,MiddleName,Surname,IDNumber,Gender, DateOfBirth, LastUpdated)"
                        f"VALUES ('Johnny', 'B.', 'Goode','0000000000',1,'1960-01-01', CURRENT_DATE );"
                        f"INSERT INTO ToDoList_App.Person(FirstName,MiddleName,Surname,IDNumber,Gender, DateOfBirth, LastUpdated)"
                        f"VALUES ('Johnny', '', 'Dangerously','1111111111',1,'1970-01-01', CURRENT_DATE );"
                        f"INSERT INTO ToDoList_App.Person(FirstName,MiddleName,Surname,IDNumber,Gender, DateOfBirth, LastUpdated)"
                        f"VALUES ('A', 'N', 'Other','2222222222',2,'1980-10-10', CURRENT_DATE );"
                        f"INSERT INTO ToDoList_App.Person(FirstName,MiddleName,Surname,IDNumber,Gender, DateOfBirth, LastUpdated)"
                        f"VALUES ('Fee', 'Fi', 'Fofum','3333333333',3,'1940-04-04', CURRENT_DATE );")

        text_statement = statement.columns()
        return text_statement

    @classmethod
    def execute(cls, session: Session) -> None:
        res = session.execute(cls.get_statement())
        res.close()
