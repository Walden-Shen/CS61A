/*
--1 basic
*/
create table parents as
select "abraham" as parent, "barack" as child union
select "abraham" 		  , "clinton"		  union
select "delano"			  , "clinton"		  union
select "clinton" 		  , "trump";

--select child from parents where parent = "abraham";

--select parent from parents where parent < child;

create table dogs as
select "abraham" as name, "long" as fur union
select "barack"  		, "short"		union
select "clinton" 		, "long" 		union
select "delano"			, "curly"		union
select "trump"			, "long";

--join table
--select parent from parents, dogs where child = name and fur = "long";

--select a.child as first, b.child as second from parents as a, parents as b
--where a.parent = b.parent and a.child < b.child;

create table grandparents as
select a.parent as grandog, b.child as grandpup
from parents as a, parents as b
where b.parent = a.child;

--select grandog from grandparents, dogs as c, dogs as d
--where grandog = c.name and grandpup = d.name and c.fur = d.fur;

/*
--2 string operation
*/
create table nouns as
select "the dog" as phrase union
select "the cat"		   union
select "the bird";

create table ands as
select first.phrase || " and " || second.phrase as phrase
from nouns as first, nouns as second
where first.phrase <> second.phrase;

--select subject.phrase || " chased " || object.phrase
--from ands as subject, ands as object
--where subject.phrase <> object.phrase;

with
	compounds(phrase, n) as (
		select phrase, 1 from nouns union
		select s.phrase || " that chased " || o.phrase, n + 1
			from compounds as s, nouns as o
			where s.phrase != o.phrase and n < 2
	)
select s.phrase || " pursued " || o.phrase
	from compounds as s, nouns as o;

/*
--3 local, recursive table
*/
with  --local tables. the with is like create local table
best(dog, owner) as (
	select "delano", "walden" union
	select "clinton", "john"
),
worst(dog, owner) as (
	select "trump", "lloyd"
)
select dog, owner from best;
--select parent from parents, best where child = dog

with -- recursive select
ancestors(ancestor, descendent) as (
	select parent, child from parents union
	select ancestor, child
		from ancestors, parents
		where parent = descendent
)
select * from ancestors;
--you can only use the odds in 'from' once
create table odds as 
	with
		odds(n) as (
			select 1 union
			select n + 2 from odds where n < 15
		)
	select n from odds;

create table fibs as
	with
		fib(previous, current) as (
			select 0, 1 union
			select current, previous + current from fib
			where current < 14
		)
	select previous as n from fib;

/*
--4 not interesting number
*/
create table pairs as
	with i(n) as (
		select 1 union
		select n + 1 from i where n < 50
	)
	select a.n as x, b.n as y from i as a, i as b where a.n <= b.n;

with
	cubes(x, y, cube) as (
		select x, y, x * x * x + y * y * y from pairs
	)
select first.x, first.y, second.x, second.y, first.cube
from cubes as first, cubes as second
where first.cube = second.cube and first.x < second.x
order by first.cube;

/*
--5.aggregation
*/
create table animals as
select "dog" as kind, 4 as legs, 20 as weight union
select "frog"		, 8		   , 20			  union
select "cat"		, 4		   , 10           union
select "parrot"		, 2		   , 5			  union
select "t-rex"		, 2		   , 12000;

select sum(weight), max(legs - weight), min(weight), avg(weight) from animals;
select legs, max(weight) from animals group by legs;
select count(*) from animals;
select count(distinct legs) from animals;
select weight / legs, count(*) from animals group by weight / legs having count(*) > 1;
select max(legs) - min(legs) from animals group by weight;
