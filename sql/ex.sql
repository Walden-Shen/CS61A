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

select grandog from grandparents, dogs as c, dogs as d
where grandog = c.name and grandpup = d.name and c.fur = d.fur;

create table nouns as
select "the dog" as phrase union
select "the cat"		   union
select "the bird";

create table ands as
select first.phrase || " and " || second.phrase as phrase
from nouns as first, nouns as second
where first.phrase <> second.phrase;

select subject.phrase || " chased " || object.phrase
from ands as subject, ands as object
where subject.phrase <> object.phrase;
