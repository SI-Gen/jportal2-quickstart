from datetime import datetime
import sys
print("PYTHONPATH=",sys.path)
from jportal import sqlalchemy as jportal
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
                                                        "New List", 
                                                        jportal.DB_ToDoListInsertReturning.ListTypeEnum.Private,
                                                        "Some Description",
                                                        datetime.now())
                                                            
    return tdl_ret

### ToDoList ###
#Select One
def select_one_from_todo_list(session):
    rec = jportal.DB_ToDoListSelectOne.execute(session,1)
    print(f"ListName: {rec.ListName}")
    print(f"ListType: {rec.ListType}")
    print(f"Description: {rec.Description}")
    print("***")

### ToDoList ###
#Select All
def update_todo_list(session):
    recs = jportal.DB_ToDoListUpdate.execute(session,
                                                "Updated ListName",
                                                jportal.DB_ToDoListUpdate.ListTypeEnum.Private,
                                                "Updated description",
                                                datetime.now(),
                                                1)

select_all_from_todo_list(session)

tdl_ret = insert_returning_todo_list(session)
print(f"Added record {tdl_ret.ID} into ToDoList")

select_one_from_todo_list(session)
update_todo_list(session)
select_all_from_todo_list(session)




session.rollback() #For the demo, normally you'd call session.commit() here