SET schema 'coding_mentor_practice';

create table plays
(
    id     integer     not null,
    title  varchar(40) not null,
    writer varchar(40) not null,
    unique (id)
);

create table reservations
(
    id                integer     not null,
    play_id           integer     not null,
    number_of_tickets integer     not null,
    theater           varchar(40) not null,
    unique (id)
);
-- sample 1
insert into plays
    values
(189, 'Queens and Kings of Madagascar', 'Paul Sat'),
(123, 'Merlin', 'Lee Roy'),
(142, 'Key of the tea', 'Max Rogers'),
(144, 'ROMEance Comedy', 'Boring Ashell'),
(145, 'Nameless.', 'Note Nul');

insert into reservations
    values
(13, 109, 12, 'Mc Rayleigh Theater'),
(24, 109, 34, 'Mc Rayleigh Theater'),
(37, 145, 84, 'Mc Rayleigh Theater'),
(49, 145, 45, 'Mc Rayleigh Theater'),
(51, 145, 41, 'Mc Rayleigh Theater'),
(68, 123, 3, 'Mc Rayleigh Theater'),
(83, 142, 46, 'Mc Rayleigh Theater');


-- sample 2
truncate table plays;
truncate table reservations;

insert into plays
    values
(34, 'The opera of the phantom', 'Lero Gastonx'),
(35, 'The legend of the cake', 'Oscar Glad'),
(36, 'Stone swords', 'Arthur King');

insert into reservations
    values
(10, 36, 13, 'Arthur King Theater'),
(30, 35, 20, 'The Legend Theater'),
(31, 36, 21, 'The Legend Theater'),
(32, 35, 23, 'The Legend Theater'),
(33, 36, 19, 'The Legend Theater'),
(40, 34, 29, 'The Jupiter Assembly Theater'),
(41, 34, 19, 'The Jupiter Assembly Theater'),
(42, 34, 6, 'The Jupiter Assembly Theater');


select p.id as id, p.title, coalesce(sum(r.number_of_tickets), 0) as reserved_tickets
from plays p
    left join reservations r on p.id = r.play_id
group by 1, 2;
