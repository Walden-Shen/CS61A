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
