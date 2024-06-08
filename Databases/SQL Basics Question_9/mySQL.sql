CREATE TABLE students(
    id int Not NULL PRIMARY KEY,
    name VARCHar(20),
    grade int
);

INSERT INTO students(id,name, grade)
VALUES (1,"Kiran", 4), (2,"gnanu", 2);


SELECT * FROM students;