--Create titles table
create table titles(
title_id VARCHAR(20) NOT NULL,
title VARCHAR(20) NOT NULL,  
PRIMARY KEY (title_id)
);


--Create employees table
CREATE TABLE employees (
emp_no INT NOT NULL,
emp_title_id VARCHAR(20) NOT NULL,
birth_date VARCHAR(20),
first_name VARCHAR(20)  NOT NULL,
last_name VARCHAR(20)  NOT NULL,
sex VARCHAR(5)NOT NULL,
hire_date VARCHAR(10),
FOREIGN KEY (emp_title_id) REFERENCES titles (title_id),
PRIMARY KEY (emp_no)
);

SELECT * from employees

--Create departments table
CREATE TABLE departments(
dept_no VARCHAR(20) NOT NULL,
dept_name VARCHAR(20) NOT NULL,
PRIMARY KEY (dept_no)
);
SELECT * FROM departments;

 
--Create dept_emp table 
CREATE TABLE dept_emp (
emp_no INT NOT NULL,
dept_no VARCHAR(20) NOT NULL,
FOREIGN KEY (emp_no) REFERENCES employees (emp_no),
FOREIGN KEY (dept_no) REFERENCES departments (dept_no),
PRIMARY KEY (emp_no, dept_no)
);

 
--Create dept_manager table
create table dept_manager(
dept_no VARCHAR (20) NOT NULL,
emp_no INT,
FOREIGN KEY (dept_no) REFERENCES departments (dept_no),
FOREIGN KEY (emp_no) REFERENCES employees (emp_no),
PRIMARY KEY (dept_no, emp_no)
);

 
--Create salary table 
CREATE TABLE salary(
emp_no INT NOT NULL,
salary INT NOT NULL,
FOREIGN KEY (emp_no) REFERENCES employees (emp_no),  
PRIMARY KEY (emp_no)
);
