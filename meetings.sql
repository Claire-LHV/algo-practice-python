SET schema 'coding_mentor_practice';

-- just playing aroun with the syntax here
select
    '09:15' > '08:00',
    '08:00' between '07:59' and '09:15',
    cast('07:59' as time),
    '09:20'::TIME,
    '08:00'::TIME between '07:59'::TIME and '09:15'::TIME;



create table meetings(
    id integer primary key ,
    start_time varchar,
    end_time varchar
);

insert into meetings
values
(1, '08:00', '09:15'),
(2, '13:20', '15:20'),
(3, '10:00', '14:00'),
(4, '13:55', '16:25'),
(5, '14:00', '17:45'),
(6, '14:05', '17:45')
;

select
    count(*) as least_rooms_needed
from meetings a
join meetings b on b.start_time >= a.start_time and b.start_time < a.end_time -- and a.id != b.id
group by a.id
order by least_rooms_needed desc
limit 1


