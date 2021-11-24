-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.


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

