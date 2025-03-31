create table customer(
customer_id varchar(5),
last_name varchar(5),
first_name varchar(10),
phone_number varchar(15),
email varchar(20),
date_of_birth date,
)

insert into customer values('c001','��','�μ�','010-1234-5678',null,'2000-10-01')
insert into customer values('c002','��','����','010-3333-3333','abc@ab.com','1998-10-20')
insert into customer values('c003','��','����','010-9876-0001','ddd@cc.com','1997-03-03')
insert into customer values('c004','��','�α�',null,'aaa@ab.com','1993-07-20')
insert into customer values('c005','��','�漷',null,null,'1980-04-30')

select * from customer

/����1

select concat(last_name, first_name) as fullname
from customer

/����2

select case when phone_number = phone_number  then phone_number
            else email
			end
as cantact_info from customer

select isnull(phone_number, email) as contact_info from customer

/����3

select 2023-year(date_of_birth) as age
from customer

/����4

select 
as ageband from