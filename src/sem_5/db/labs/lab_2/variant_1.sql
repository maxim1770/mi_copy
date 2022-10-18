-- 2.2.1 -
select * from D8_EXAMS
where EXAM_DATE between "10-01-2002" and "20-01-2002";


-- 2.2.2
select D8_SUBJECT.SUBJ_NAME from D8_EXAMS
join D8_SUBJECT on D8_EXAMS.SUBJ_ID = D8_SUBJECT.SUBJ_ID
where STUD_ID IN (12, 32);


-- 2.2.3 +
select SUBJ_NAME from D8_SUBJECT
where SUBJ_NAME like 'И%';


-- 2.2.4 +
select * from D8_STUDENT
where NAME like 'И%' or NAME like 'С%';


-- 2.2.5 +
select * from D8_EXAMS
where MARK is null;


-- 2.2.6 +
select * from D8_EXAMS
where MARK is not null;


-- 2.2.7 +
select * from D8_LECTURER
where CITY like '%-%';


-- 2.2.8 +
select * from D8_UNIVERSITY
where CITY like '%"%"%';


-- 2.2.9 +
select * from D8_SUBJECT
where SUBJ_NAME like '%ИЯ';


-- 2.2.10 +
select * from D8_UNIVERSITY
where UNIV_NAME like '%УНИВЕРСИТЕТ%';


-- 2.2.11 +
select * from D8_STUDENT
where SURNAME like 'КОВ%' or SURNAME like 'КУЗ%';


-- 2.2.12 -
select * from D8_SUBJECT
where SUBJ_NAME like '%\_%' escape '\';


-- 2.2.13 -
select * from D8_UNIVERSITY
where UNIV_NAME like '%\_%\_%\_%..' ESCAPE '\';


-- 2.2.14 +
select * from D8_STUDENT
where SURNAME like '___';
