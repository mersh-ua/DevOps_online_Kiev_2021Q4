USE epam;

INSERT INTO academic_subjects (subj_name,subj_duration) 
VALUES('Netwotking',12), 
      ('Databases',3),
      ('Linux',12),  
      ('Git',3),
      ('VM',3), 
      ('Clouds',6),
      ('History of KPSS',48);

INSERT INTO students (student_name) 
VALUES('Nikola Tesla'), 
      ('Niko Pirosmani'),
      ('Nicolaus Copernicus'),
      ('Nikolay Pirogov'),
      ('Nikolay Nosov');

INSERT INTO labs (student_id,subj_id,lab_code,lab_status)
VALUES(1,1,'Lab X',true),
      (1,1,'Lab Y',true),
      (1,1,'Lab Z',false),
      (2,7,'Lab H',true),
      (4,2,'Lab A',true),
      (4,2,'Lab B',false),
      (4,2,'Lab C',false),
      (5,7,'Lab H',true);
