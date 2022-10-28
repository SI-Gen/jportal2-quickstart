CREATE SCHEMA IF NOT EXISTS ToDoList_App;
DROP TABLE IF EXISTS ToDoList_App.ToDoList CASCADE;

CREATE TABLE ToDoList_App.ToDoList
( ID serial
, ListName varchar(255)
, ListType smallint
, Description varchar(255)
, LastUpdated timestamp
);

ALTER TABLE ToDoList_App.ToDoList ALTER ID SET NOT NULL;
ALTER TABLE ToDoList_App.ToDoList ALTER ListName SET NOT NULL;
ALTER TABLE ToDoList_App.ToDoList ALTER ListType SET NOT NULL;
ALTER TABLE ToDoList_App.ToDoList ALTER Description SET NOT NULL;
ALTER TABLE ToDoList_App.ToDoList ALTER LastUpdated SET NOT NULL;

ALTER TABLE ToDoList_App.ToDoList
 ADD CONSTRAINT TODOLIST_PKEY PRIMARY KEY
  ( ID
  )
;

INSERT INTO ToDoList_App.ToDoList(ListName,ListType,Description,LastUpdated) VALUES ('Takeon Test List 1', 1, 'Take on test list description', CURRENT_DATE )

DROP TABLE IF EXISTS ToDoList_App.ToDo_Item CASCADE;

CREATE TABLE ToDoList_App.ToDo_Item
( ID serial
, TodoList_ID integer
, ItemName varchar(255)
, ItemDescription text
, LastUpdated timestamp
);

ALTER TABLE ToDoList_App.ToDo_Item ALTER ID SET NOT NULL;
ALTER TABLE ToDoList_App.ToDo_Item ALTER TodoList_ID SET NOT NULL;
ALTER TABLE ToDoList_App.ToDo_Item ALTER ItemName SET NOT NULL;
ALTER TABLE ToDoList_App.ToDo_Item ALTER ItemDescription SET NOT NULL;
ALTER TABLE ToDoList_App.ToDo_Item ALTER LastUpdated SET NOT NULL;

ALTER TABLE ToDoList_App.ToDo_Item
 ADD CONSTRAINT TODO_ITEM_PKEY PRIMARY KEY
  ( ID
  )
;

DROP TABLE IF EXISTS ToDoList_App.Person CASCADE;

CREATE TABLE ToDoList_App.Person
( ID serial
, FirstName varchar(255)
, MiddleName varchar(255)
, Surname varchar(255)
, IDNumber varchar(50)
, Gender smallint
, DateOfBirth date
, LastUpdated timestamp
);

-- DROP INDEX PERSON_IDX_SURNAME_FIRSTNAME;

CREATE INDEX PERSON_IDX_SURNAME_FIRSTNAME ON ToDoList_App.Person
( Surname
, FirstName
);

ALTER TABLE ToDoList_App.Person ALTER ID SET NOT NULL;
ALTER TABLE ToDoList_App.Person ALTER FirstName SET NOT NULL;
ALTER TABLE ToDoList_App.Person ALTER MiddleName SET NOT NULL;
ALTER TABLE ToDoList_App.Person ALTER Surname SET NOT NULL;
ALTER TABLE ToDoList_App.Person ALTER IDNumber SET NOT NULL;
ALTER TABLE ToDoList_App.Person ALTER Gender SET NOT NULL;
ALTER TABLE ToDoList_App.Person ALTER DateOfBirth SET NOT NULL;
ALTER TABLE ToDoList_App.Person ALTER LastUpdated SET NOT NULL;

ALTER TABLE ToDoList_App.Person
 ADD CONSTRAINT PERSON_PKEY PRIMARY KEY
  ( ID
  )
;
ALTER TABLE ToDoList_App.Person
 ADD CONSTRAINT PERSON_UNQ_IDNUMBER UNIQUE
  ( IDNumber
  )
;

INSERT INTO ToDoList_App.Person(FirstName,MiddleName,Surname,IDNumber,Gender, DateOfBirth, LastUpdated)
VALUES ('Johnny', 'B.', 'Goode','0000000000',1,'1960-01-01', CURRENT_DATE );
INSERT INTO ToDoList_App.Person(FirstName,MiddleName,Surname,IDNumber,Gender, DateOfBirth, LastUpdated)
VALUES ('Johnny', '', 'Dangerously','1111111111',1,'1970-01-01', CURRENT_DATE );
INSERT INTO ToDoList_App.Person(FirstName,MiddleName,Surname,IDNumber,Gender, DateOfBirth, LastUpdated)
VALUES ('A', 'N', 'Other','2222222222',2,'1980-10-10', CURRENT_DATE );
INSERT INTO ToDoList_App.Person(FirstName,MiddleName,Surname,IDNumber,Gender, DateOfBirth, LastUpdated)
VALUES ('Fee', 'Fi', 'Fofum','3333333333',3,'1940-04-04', CURRENT_DATE );

