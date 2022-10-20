########################################################################################################################
################## Generated Code. DO NOT CHANGE THIS CODE. Change it in the generator and regenerate ##################
########################################################################################################################
from .db_Person import DB_Person
from .db_Person import DB_PersonInsertReturning
from .db_Person import DB_PersonUpdate
from .db_Person import DB_PersonSelectOne
from .db_Person import DB_PersonDeleteOne
from .db_Person import DB_PersonSelectOneByIDNumber
from .db_Person import DB_PersonSelectByGender
from .db_Person import DB_PersonSelectNameSurnameByGender
from .db_Person import DB_PersonSelectNameSurnameAndGenderAsStringByIDNumber
from .db_Person import DB_PersonSelectWithDynamicQuery
from .db_Person import DB_Person
from .db_ToDo_Item import DB_ToDo_Item
from .db_ToDo_Item import DB_ToDo_ItemInsert
from .db_ToDo_Item import DB_ToDo_ItemUpdate
from .db_ToDo_Item import DB_ToDo_ItemSelectOne
from .db_ToDo_Item import DB_ToDo_ItemDeleteOne
from .db_ToDo_Item import DB_ToDo_ItemSelectByTodoList_ID
from .db_ToDo_Item import DB_ToDo_ItemUpdateByItemDescription
from .db_ToDoList import DB_ToDoList
from .db_ToDoList import DB_ToDoListSelectAll
from .db_ToDoList import DB_ToDoListInsertReturning
from .db_ToDoList import DB_ToDoListUpdate
from .db_ToDoList import DB_ToDoListSelectOne
from .db_ToDoList import DB_ToDoListDeleteOne
from .db_ToDoList import DB_ToDoList

ALL_TABLES = [
    DB_Person,
    DB_ToDo_Item,
    DB_ToDoList,
]

ALL_PROCS = [
    DB_Person,
    DB_PersonDeleteOne,
    DB_PersonInsertReturning,
    DB_PersonSelectByGender,
    DB_PersonSelectNameSurnameAndGenderAsStringByIDNumber,
    DB_PersonSelectNameSurnameByGender,
    DB_PersonSelectOne,
    DB_PersonSelectOneByIDNumber,
    DB_PersonSelectWithDynamicQuery,
    DB_PersonUpdate,

    DB_ToDo_ItemDeleteOne,
    DB_ToDo_ItemInsert,
    DB_ToDo_ItemSelectByTodoList_ID,
    DB_ToDo_ItemSelectOne,
    DB_ToDo_ItemUpdate,
    DB_ToDo_ItemUpdateByItemDescription,

    DB_ToDoList,
    DB_ToDoListDeleteOne,
    DB_ToDoListInsertReturning,
    DB_ToDoListSelectAll,
    DB_ToDoListSelectOne,
    DB_ToDoListUpdate,

]


__all__ = [
    "DB_Person",
    "DB_ToDo_Item",
    "DB_ToDoList",

    "DB_Person",
    "DB_PersonDeleteOne",
    "DB_PersonInsertReturning",
    "DB_PersonSelectByGender",
    "DB_PersonSelectNameSurnameAndGenderAsStringByIDNumber",
    "DB_PersonSelectNameSurnameByGender",
    "DB_PersonSelectOne",
    "DB_PersonSelectOneByIDNumber",
    "DB_PersonSelectWithDynamicQuery",
    "DB_PersonUpdate",

    "DB_ToDo_ItemDeleteOne",
    "DB_ToDo_ItemInsert",
    "DB_ToDo_ItemSelectByTodoList_ID",
    "DB_ToDo_ItemSelectOne",
    "DB_ToDo_ItemUpdate",
    "DB_ToDo_ItemUpdateByItemDescription",

    "DB_ToDoList",
    "DB_ToDoListDeleteOne",
    "DB_ToDoListInsertReturning",
    "DB_ToDoListSelectAll",
    "DB_ToDoListSelectOne",
    "DB_ToDoListUpdate",

]
