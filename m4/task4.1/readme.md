<h1>EPAM DevOps Courses</h1>
<h2>Lab 4.1 Databases</h2>

<details><summary>Database schema and tables creation</summary><br>
<img src=t4.1_db_schema.png>

|H1|H2|
|--|-|
|abc|123|
|xyz|000|


```sql
CREATE TABLE `labs` (
    `student_id` int  NOT NULL ,
    `subj_id` int  NOT NULL ,
    `lab_code` varchar(12)  NOT NULL ,
    `lab_status` boolean  NOT NULL 
);

CREATE TABLE `students` (
    `student_id` int  NOT NULL ,
    `student_name` varchar(50)  NOT NULL ,
    PRIMARY KEY (
        `student_id`
    )
);

CREATE TABLE `academic_subjects` (
    `subj_id` int  NOT NULL ,
    `subj_name` varchar(50)  NOT NULL ,
    `subj_duration` int  NOT NULL ,
    PRIMARY KEY (
        `subj_id`
    )
);

ALTER TABLE `labs` ADD CONSTRAINT `fk_labs_student_id` FOREIGN KEY(`student_id`)
REFERENCES `students` (`student_id`);

ALTER TABLE `labs` ADD CONSTRAINT `fk_labs_subj_id` FOREIGN KEY(`subj_id`)
REFERENCES `academic_subjects` (`subj_id`);
```

</details>
