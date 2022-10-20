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
recs = jportal.DB_ToDoListSelectAll.execute(session)
print(recs)

#Insert
tdl_ret = jportal.DB_ToDoListInsertReturning.execute(session, 
                                                        "ListXXX", 
                                                        jportal.DB_ToDoListInsertReturning.ListTypeEnum.Private,
                                                        "Some Description",
                                                        datetime.now)
print(f"Added record {tdl_ret.ID} into ToDoList")