SELECT current_database(), current_schema, "current_user"();

-- select * from information_schema.tables;

create schema coding_mentor_practice;
SET schema 'coding_mentor_practice';
create table species (
    id integer not null,
    temp_preferences varchar(1) check(temp_preferences in ('+', '-')),
    temp_limit integer not null,
    unique(id)
);
create table ponds(
    id integer not null,
    temperature integer not null,
    city varchar(10),
    unique(id)
);
create table ducks(
    id integer not null,
    name varchar(10),
    species_id integer not null,
    pond_id integer not null,
    unique (id)
);

-- pond_id, happy_ducks, order by pond_id, every pond should appear in this table

-- Example 1
insert into species
values
(30, '+', 15),
(40, '-', 20),
(50, '-', 31);

insert into ponds
values
(1, 13, 'Oregon'),
(2, 31, 'Oregano');

insert into ducks
values
(1, 'Martin', 50, 2),
(3, 'Bruno', 30, 1),
(9, 'Ignacio', 40, 2),
(27, 'Hedwig', 40, 1),
(81, 'Marina', 30, 2);


-- works for example 1 but not 2
select
    pond_id,
    count(*)
from ducks d
inner join species s on d.species_id = s.id
inner join ponds p on d.pond_id = p.id
where
    case
        when temp_preferences = '+' then temperature >= s.temp_limit
        else temperature <= s.temp_limit
    end = true
group by pond_id
order by pond_id;


truncate species;
truncate ponds;
truncate ducks;


-- Example 2
insert into species
values
(1, '+', 10);

insert into ponds
values
(10, 5, 'Bialystok');

insert into ducks
values
(10, 'Lotto', 1, 10);

-- works for 2, but not for 3
select
    pond_id,
    sum(
        case
            when (temp_preferences = '+' and temperature >= s.temp_limit) or (temp_preferences = '-' and temperature <= s.temp_limit) then 1
            else 0
        end
    ) as happy_ducks
from ducks d
inner join species s on d.species_id = s.id
inner join ponds p on d.pond_id = p.id
group by pond_id
order by pond_id;


-- My example 3
insert into species
values
(1, '+', 10);

insert into ponds
values
(10, 5, 'Bialystok'),
(20, 20, 'No Duck');

insert into ducks
values
(10, 'Lotto', 1, 10);

-- final answer here
select
    p.id as pond_id,
    sum(
        case
            when
                (temp_preferences = '+' and temperature >= s.temp_limit)
                    or (temp_preferences = '-' and temperature <= s.temp_limit)
                then 1
            else 0
        end
    ) as happy_ducks
    -- other option: count if
from ponds p
left join ducks d on d.pond_id = p.id
left join species s on d.species_id = s.id
group by p.id
order by p.id;
