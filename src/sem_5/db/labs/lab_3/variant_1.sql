-- 2.4.1 +
select count(*) from D8_EXAMS
where SUBJ_ID == 20;


-- 2.4.2 +
select count(distinct SUBJ_ID ) from D8_EXAMS;


-- 2.4.3 +
select STUD_ID, min(MARK) from D8_EXAMS
group by STUD_ID;


-- 2.4.4 +
select STUD_ID, max(MARK) from D8_EXAMS
group by STUD_ID;


-- 2.4.5 +
select SURNAME from D8_STUDENT
where SURNAME like 'И%'
order by SURNAME
limit 1;


-- 2.4.6 +
select SUBJ_NAME, max(SEMESTR) from D8_SUBJECT
group by SUBJ_NAME;


-- 7.	Напишите запрос, который для каждого конкретного дня сдачи экзамена выводит данные о количестве студентов, сдававших экзамен в этот день.
-- 2.4.7 -
select SUBJ_NAME, max(SEMESTR) from D8_SUBJECT
group by SUBJ_NAME;


-- 2.4.8 +
select STUD_ID, avg(MARK) from D8_EXAMS
group by STUD_ID;


-- 2.4.9 +-
select SUBJ_ID, avg(MARK) from D8_EXAMS
group by SUBJ_ID;


-- 2.4.10 +
select SUBJ_ID, count(*) from D8_EXAMS
where MARK >= 3
group by SUBJ_ID;


-- 2.4.11 +
select SEMESTR, count(*) from D8_SUBJECT
group by SEMESTR;


-- 2.4.12 +
select UNIV_ID, sum(STIPEND) as sum_stipend from D8_STUDENT
group by UNIV_ID
order by sum_stipend desc;


-- 2.4.13 +
select SEMESTR, sum(HOUR) from D8_SUBJECT
group by SEMESTR;


-- 2.4.14 +
select STUD_ID, avg(MARK) from D8_EXAMS
group by EXAM_ID, STUD_ID;


-- 2.4.15 +
select STUD_ID, SUBJ_ID, avg(MARK) from D8_EXAMS
group by SUBJ_ID, STUD_ID
order by STUD_ID;