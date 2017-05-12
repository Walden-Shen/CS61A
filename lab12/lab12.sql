-- Requires the contents of file states.sql to be loaded first.
.read states.sql

-- Tables in states.sql:
--   states(state):       US States + DC - HI - AK
--   landlocked(state):   Table of landlocked (not adjacent to ocean) states
--   adjacencies(s1, s2): States that are adjacent to each other

create table california as
  -- REPLACE THIS LINE
  select 'YOUR CODE HERE';

-- Finds lengths of possible paths between two states
create table distances as
  with
    distance(start, end, hops) as (
      -- REPLACE THIS LINE
      select 'Your', 'Code', 'Here'
    )
  select * from distance;

create table three_hops as
  -- REPLACE THIS LINE
  select 'YOUR CODE HERE';
