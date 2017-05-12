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
      	select state, state, 0 from landlocked union
		select start, s2, hops + 1 from inland, adjacencies, landlocked where s1 = end and s2 = state and hops < 8
	)
  -- REPLACE THIS LINE
select s1 as start, s2 as end, 2 as hops from adjacencies union
select start.s1 as start, end.s2 as end, hops + 2 as hops
from adjacencies as start, adjacencies as end, inland where start.s2 = start and end.s1 = end;
