SET schema 'coding_mentor_practice';

create table transfers
(
    name  varchar(30) not null,
    money integer     not null
);

insert into transfers
values ('Andrea', -10000),
       ('Mark', 149513),
       ('Kassidy', -5816),
       ('Andrea', 17500),
       ('Andrea', 2500),
       ('Jim', 100000),
       ('Jim', -50),
       ('Jim', -50),
       ('Jim', -50),
       ('Kassidy', -2013);

select name,
       sum(case when money > 0 then money else 0 end) as sum_of_deposits,
       sum(case when money < 0 then abs(money) else 0 end) as sum_of_withdrawals
from transfers
group by name
order by name
;
