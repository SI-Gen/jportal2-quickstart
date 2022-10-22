from datetime import datetime
import sys
print("PYTHONPATH=",sys.path)
import jportal as jportal
import sqlalchemy as sa
from sqlalchemy.orm import Session

engine = sa.create_engine("postgresql+psycopg2://postgres:magic_password@localhost/postgres")



session = Session(engine)

### ToDoList ###
#Select All
def select_all_from_todo_list(session):
    recs = jportal.DB_ToDoListSelectAll.execute(session)
    for rec in recs:
        print(f"ID: {rec.ID}")
        print(f"ListName: {rec.ListName}")
        print(f"ListType: {rec.ListType}")
        print(f"Description: {rec.Description}")
        print("***")

### ToDoList ###
#Insert Returning
def insert_returning_todo_list(session):
    #Insert
    tdl_ret = jportal.DB_ToDoListInsertReturning.execute(session, 
                                                        "ListXXX", 
                                                        jportal.DB_ToDoListInsertReturning.ListTypeEnum.Private,
                                                        "Some Description",
                                                        datetime.now())
                                                            
    return tdl_ret


select_all_from_todo_list(session)

tdl_ret = insert_returning_todo_list(session)
print(f"Added record {tdl_ret.ID} into ToDoList")

select_all_from_todo_list(session)

session.rollback() #For the demo, normally you'd call session.commit() here