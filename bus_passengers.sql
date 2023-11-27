SET schema 'coding_mentor_practice';

create table buses
(
    id          integer primary key,
    origin      varchar not null,
    destination varchar not null,
    time        varchar not null,
    unique (origin, destination, time)
);

create table passengers
(
    id          integer primary key,
    origin      varchar not null,
    destination varchar not null,
    time        varchar not null
);

-- sample 1
INSERT INTO buses (id, origin, destination, time) VALUES
(10, 'Warsaw', 'Berlin', '10:55'),
(20, 'Berlin', 'Paris', '06:20'),
(21, 'Berlin', 'Paris', '14:08'),
(22, 'Berlin', 'Paris', '21:40'),
(30, 'Paris', 'Madrid', '13:30');

INSERT INTO passengers (id, origin, destination, time) VALUES
(1, 'Paris', 'Madrid', '13:30'),
(2, 'Paris', 'Madrid', '13:31'),
(10, 'Warsaw', 'Paris', '10:00'),
(11, 'Warsaw', 'Berlin', '22:31'),
(40, 'Berlin', 'Paris', '06:15'),
(41, 'Berlin', 'Paris', '06:50'),
(42, 'Berlin', 'Paris', '07:12'),
(43, 'Berlin', 'Paris', '12:03'),
(44, 'Berlin', 'Paris', '20:00');

-- sample 2
truncate buses;
truncate passengers;

INSERT INTO buses (id, origin, destination, time) VALUES
(100, 'Munich', 'Rome', '13:00'),
(200, 'Munich', 'Rome', '15:30'),
(300, 'Munich', 'Rome', '20:00');

INSERT INTO passengers (id, origin, destination, time) VALUES
(1, 'Munich', 'Rome', '10:01'),
(2, 'Munich', 'Rome', '11:30'),
(3, 'Munich', 'Rome', '11:30'),
(4, 'Munich', 'Rome', '12:03'),
(5, 'Munich', 'Rome', '13:00');


with match as (
select
    b.id as bus_id,
    p.id as pass_id,
    FIRST_VALUE(b.id) OVER (PARTITION BY p.id ORDER BY b.time) AS first_arrived_bus
from buses b
    left join passengers p
    on b.destination = p.destination
        and b.origin = p.origin
        and b.time >= p.time
order by p.id
)
select
    bus_id as id,
    count(case when bus_id = first_arrived_bus then pass_id end) as passengers_on_board
from match
group by bus_id
order by bus_id
;