-- Requires the contents of file states.sql to be loaded first.
.read states.sql

-- Tables in states.sql:
--   states(state):       US States + DC - HI - AK
--   landlocked(state):   Table of landlocked (not adjacent to ocean) states
--   adjacencies(s1, s2): States that are adjacent to each other

create table alphabetical_paths as
  with
    paths(s, n, last) as (
      -- REPLACE THIS LINE
    	select s1 || ',' || s2, 2, s2 from adjacencies where s2 > s1 union
		select s || ',' || s2, n + 1, s2 from paths, adjacencies where s1 = last and s2 > s1
    )
  select s from paths where n > 6 order by -n;

-- Lengths of possible paths between two states that enter only
-- landlocked states along the way.
create table inland_distances as
  with
    inland(start, end, hops) as (
      -- REPLACE THIS LINE
      	select s1, s2, 1 from adjacencies, landlocked as a, landlocked as b where a.state = s1 and b.state = s2 union
		select start, s2, hops + 1 from inland, adjacencies, landlocked where s1 = end and s2 = state and hops < 10
    )
  -- REPLACE THIS LINE
select start as start, end as end, hops as hops from inland;
