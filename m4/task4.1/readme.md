<h1>EPAM DevOps Courses</h1>
<h2>Lab 4.1 Databases</h2>

<details><summary>Database schema and script for it creation</summary><br>
<img src=t4.1_db_schema.png>


```sql
CREATE DATABASE IF NOT EXISTS epam;

USE epam;

CREATE TABLE IF NOT EXISTS labs (
    student_id int NOT NULL,
    subj_id int NOT NULL,
    lab_code varchar(12) NOT NULL,
    lab_status boolean NOT NULL 
);

CREATE TABLE IF NOT EXISTS students (
    student_id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    student_name varchar(50) NOT NULL 
);

CREATE TABLE IF NOT EXISTS academic_subjects (
    subj_id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    subj_name varchar(50) NOT NULL,
    subj_duration int NOT NULL 
);

ALTER TABLE `labs` ADD CONSTRAINT `fk_labs_student_id` FOREIGN KEY(`student_id`)
REFERENCES `students` (`student_id`);

ALTER TABLE `labs` ADD CONSTRAINT `fk_labs_subj_id` FOREIGN KEY(`subj_id`)
REFERENCES `academic_subjects` (`subj_id`);
```

</details>

<details><summary>Database creation</summary><br>
<img src=t4.1_run_sql.png>
<img src=t4.1_schow.png>
</details>
