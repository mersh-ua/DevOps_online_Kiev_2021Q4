use epam;

select students.student_name, academic_subjects.subj_name, labs.lab_code, labs.lab_status
 from students, academic_subjects, labs
 where students.student_id = labs.student_id and labs.subj_id = academic_subjects.subj_id
 order by labs.lab_status;
