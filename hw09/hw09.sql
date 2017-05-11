create table parents as
  select "abraham" as parent, "barack" as child union
  select "abraham"          , "clinton"         union
  select "delano"           , "herbert"         union
  select "fillmore"         , "abraham"         union
  select "fillmore"         , "delano"          union
  select "fillmore"         , "grover"          union
  select "eisenhower"       , "fillmore";

create table dogs as
  select "abraham" as name, "long" as fur, 26 as height union
  select "barack"         , "short"      , 52           union
  select "clinton"        , "long"       , 47           union
  select "delano"         , "long"       , 46           union
  select "eisenhower"     , "short"      , 35           union
  select "fillmore"       , "curly"      , 32           union
  select "grover"         , "short"      , 28           union
  select "herbert"        , "curly"      , 31;

create table sizes as
  select "toy" as size, 24 as min, 28 as max union
  select "mini",        28,        35        union
  select "medium",      35,        45        union
  select "standard",    45,        60;

-------------------------------------------------------------
-- PLEASE DO NOT CHANGE ANY SQL STATEMENTS ABOVE THIS LINE --
-------------------------------------------------------------

-- The size of each dog
create table size_of_dogs as
select name, size from dogs, sizes where min <= height and height <= max;


-- All dogs with parents ordered by decreasing height of their parent
create table by_height as
--select name from dogs, parents where name = child order by parent desc;
select child from dogs as a, dogs as b, parents where child = a.name and b.name = parent order by b.height desc;


-- Sentences about siblings that are the same size
create table sentences as
with siblings(a, b) as (
	select dogsa.child as a, dogsb.child as b 
	from parents as dogsa, parents as dogsb 
	where dogsa.parent = dogsb.parent and dogsa.child <> dogsb.child and dogsa.child < dogsb.child
	)
select a || " and " || b || " are " || first.size || " siblings" from siblings, size_of_dogs as first, size_of_dogs as second
	where first.name = a and second.name = b and first.size = second.size;
	
-- Ways to stack 4 dogs to a height of at least 170, ordered by total height
create table stacks as
	/*select first.name || ", " || second.name || ", " || third.name || ", " || fourth.name, first.height + second.height + third.height + fourth.height
	from dogs as first, dogs as second, dogs as third, dogs as fourth
	where first.name > second.name and second.name > third.name and third.name > fourth.name and first.height + second.height + third.height + fourth.height >= 170
	order by first.height + second.height + third.height + fourth.height asc;*/
	with stack(names_of_dog, last_dog, last_height, stack_height, stack_size) as (
		select name, name, height, height, 1 from dogs union
		select a.names_of_dog || ", " || b.name, b.name, b.height, a.stack_height + b.height, a.stack_size + 1
			from stack as a, dogs as b
			where b.name != a.last_dog and a.stack_size < 4 and a.last_height < b.height
		)
	select names_of_dog, stack_height from stack where stack_size = 4 and stack_height >= 170;

create table tallest as
select height, name from dogs group by height / 10 having count(*) > 1 and height = max(height);

-- All non-parent relations ordered by height difference
create table non_parents as
select "REPLACE THIS LINE WITH YOUR SOLUTION";


