

## 逻辑计划图参考
1. org/apache/spark/sql/catalyst/parser/PlanParserSuite.scala


### select
```
-- single comment
SELECT * FROM a
'Project [*]
+- 'UnresolvedRelation [a]


-- single comment\
with line continuity
SELECT * FROM a
'Project [*]
+- 'UnresolvedRelation [a]

sELEct * FroM a
'Project [*]
+- 'UnresolvedRelation [a]

select * fRoM a
'Project [*]
+- 'UnresolvedRelation [a]

SELECT * FROM a
'Project [*]
+- 'UnresolvedRelation [a]
```






### union
```
select * from a union select * from b
'Distinct
+- 'Union
   :- 'Project [*]
   :  +- 'UnresolvedRelation [a]
   +- 'Project [*]
      +- 'UnresolvedRelation [b]

select * from a union distinct select * from b
'Distinct
+- 'Union
   :- 'Project [*]
   :  +- 'UnresolvedRelation [a]
   +- 'Project [*]
      +- 'UnresolvedRelation [b]

select * from a union all select * from b
'Union
:- 'Project [*]
:  +- 'UnresolvedRelation [a]
+- 'Project [*]
   +- 'UnresolvedRelation [b]

```
### except

```
select * from a except select * from b
'Except false
:- 'Project [*]
:  +- 'UnresolvedRelation [a]
+- 'Project [*]
   +- 'UnresolvedRelation [b]

select * from a except distinct select * from b
'Except false
:- 'Project [*]
:  +- 'UnresolvedRelation [a]
+- 'Project [*]
   +- 'UnresolvedRelation [b]

select * from a except all select * from b
'ExceptAll true
:- 'Project [*]
:  +- 'UnresolvedRelation [a]
+- 'Project [*]
   +- 'UnresolvedRelation [b]

select * from a minus select * from b
'Except false
:- 'Project [*]
:  +- 'UnresolvedRelation [a]
+- 'Project [*]
   +- 'UnresolvedRelation [b]

select * from a minus all select * from b
'ExceptAll true
:- 'Project [*]
:  +- 'UnresolvedRelation [a]
+- 'Project [*]
   +- 'UnresolvedRelation [b]

select * from a minus distinct select * from b
'Except false
:- 'Project [*]
:  +- 'UnresolvedRelation [a]
+- 'Project [*]
   +- 'UnresolvedRelation [b]

select * from a intersect select * from b
'Intersect false
:- 'Project [*]
:  +- 'UnresolvedRelation [a]
+- 'Project [*]
   +- 'UnresolvedRelation [b]

select * from a intersect distinct select * from b
'Intersect false
:- 'Project [*]
:  +- 'UnresolvedRelation [a]
+- 'Project [*]
   +- 'UnresolvedRelation [b]

select * from a intersect all select * from b
'IntersectAll true
:- 'Project [*]
:  +- 'UnresolvedRelation [a]
+- 'Project [*]
   +- 'UnresolvedRelation [b]



with cte1 as (select * from a) select * from cte1
CTE [cte1]
:  +- 'SubqueryAlias cte1
:     +- 'Project [*]
:        +- 'UnresolvedRelation [a]
+- 'Project [*]
   +- 'UnresolvedRelation [cte1]

with cte1 (select 1) select * from cte1
CTE [cte1]
:  +- 'SubqueryAlias cte1
:     +- 'Project [unresolvedalias(1, None)]
:        +- OneRowRelation
+- 'Project [*]
   +- 'UnresolvedRelation [cte1]

with cte1 (select 1), cte2 as (select * from cte1) select * from cte2
CTE [cte1, cte2]
:  :- 'SubqueryAlias cte1
:  :  +- 'Project [unresolvedalias(1, None)]
:  :     +- OneRowRelation
:  +- 'SubqueryAlias cte2
:     +- 'Project [*]
:        +- 'UnresolvedRelation [cte1]
+- 'Project [*]
   +- 'UnresolvedRelation [cte2]


select 1

'Project [unresolvedalias(1, None)]
+- OneRowRelation

select a, b
'Project ['a, 'b]
+- OneRowRelation

select a, b from db.c
'Project ['a, 'b]
+- 'UnresolvedRelation [db, c]

select a, b from db.c where x < 1
'Project ['a, 'b]
+- 'Filter ('x < 1)
   +- 'UnresolvedRelation [db, c]

select a, b from db.c having x < 1
'UnresolvedHaving ('x < 1)
+- 'Aggregate ['a, 'b]
   +- 'UnresolvedRelation [db, c]

select distinct a, b from db.c
'Distinct
+- 'Project ['a, 'b]
   +- 'UnresolvedRelation [db, c]

select all a, b from db.c
'Project ['a, 'b]
+- 'UnresolvedRelation [db, c]

select from tbl
'Project ['from AS tbl#0]
+- OneRowRelation

select a from 1k.2m
'Project ['a]
+- 'UnresolvedRelation [1k, 2m]



from a select b, c
'Project ['b, 'c]
+- 'UnresolvedRelation [a]

from db.a select b, c where d < 1
'Project ['b, 'c]
+- 'Filter ('d < 1)
   +- 'UnresolvedRelation [db, a]

from a select distinct b, c
'Distinct
+- 'Project ['b, 'c]
   +- 'UnresolvedRelation [a]



from a select * select * where s < 10
'Union
:- 'Project [*]
:  +- 'UnresolvedRelation [a]
+- 'Project [*]
   +- 'Filter ('s < 10)
      +- 'UnresolvedRelation [a]

from a insert into tbl1 select * insert into tbl2 select * where s < 10
'Union
:- 'InsertIntoStatement 'UnresolvedRelation [tbl1], false, false
:  +- 'Project [*]
:     +- 'UnresolvedRelation [a]
+- 'InsertIntoStatement 'UnresolvedRelation [tbl2], false, false
   +- 'Project [*]
      +- 'Filter ('s < 10)
         +- 'UnresolvedRelation [a]

select * from (from a select * select *)
'Project [*]
+- 'SubqueryAlias __auto_generated_subquery_name
   +- 'Union
      :- 'Project [*]
      :  +- 'UnresolvedRelation [a]
      +- 'Project [*]
         +- 'UnresolvedRelation [a]



select * from t
'Project [*]
+- 'UnresolvedRelation [t]

select * from t limit 10
'GlobalLimit 10
+- 'LocalLimit 10
   +- 'Project [*]
      +- 'UnresolvedRelation [t]

select * from t window w1 as ()
'WithWindowDefinition Map(w1 -> windowspecdefinition(unspecifiedframe$()))
+- 'Project [*]
   +- 'UnresolvedRelation [t]

select * from t window w1 as () limit 10
'GlobalLimit 10
+- 'LocalLimit 10
   +- 'WithWindowDefinition Map(w1 -> windowspecdefinition(unspecifiedframe$()))
      +- 'Project [*]
         +- 'UnresolvedRelation [t]

select * from t order by a, b desc
'Sort ['a ASC NULLS FIRST, 'b DESC NULLS LAST], true
+- 'Project [*]
   +- 'UnresolvedRelation [t]

select * from t order by a, b desc limit 10
'GlobalLimit 10
+- 'LocalLimit 10
   +- 'Sort ['a ASC NULLS FIRST, 'b DESC NULLS LAST], true
      +- 'Project [*]
         +- 'UnresolvedRelation [t]

select * from t order by a, b desc window w1 as ()
'WithWindowDefinition Map(w1 -> windowspecdefinition(unspecifiedframe$()))
+- 'Sort ['a ASC NULLS FIRST, 'b DESC NULLS LAST], true
   +- 'Project [*]
      +- 'UnresolvedRelation [t]

select * from t order by a, b desc window w1 as () limit 10
'GlobalLimit 10
+- 'LocalLimit 10
   +- 'WithWindowDefinition Map(w1 -> windowspecdefinition(unspecifiedframe$()))
      +- 'Sort ['a ASC NULLS FIRST, 'b DESC NULLS LAST], true
         +- 'Project [*]
            +- 'UnresolvedRelation [t]

select * from t sort by a, b desc
'Sort ['a ASC NULLS FIRST, 'b DESC NULLS LAST], false
+- 'Project [*]
   +- 'UnresolvedRelation [t]

select * from t sort by a, b desc limit 10
'GlobalLimit 10
+- 'LocalLimit 10
   +- 'Sort ['a ASC NULLS FIRST, 'b DESC NULLS LAST], false
      +- 'Project [*]
         +- 'UnresolvedRelation [t]

select * from t sort by a, b desc window w1 as ()
'WithWindowDefinition Map(w1 -> windowspecdefinition(unspecifiedframe$()))
+- 'Sort ['a ASC NULLS FIRST, 'b DESC NULLS LAST], false
   +- 'Project [*]
      +- 'UnresolvedRelation [t]

select * from t sort by a, b desc window w1 as () limit 10
'GlobalLimit 10
+- 'LocalLimit 10
   +- 'WithWindowDefinition Map(w1 -> windowspecdefinition(unspecifiedframe$()))
      +- 'Sort ['a ASC NULLS FIRST, 'b DESC NULLS LAST], false
         +- 'Project [*]
            +- 'UnresolvedRelation [t]



insert overwrite table s select * from t
'InsertIntoStatement 'UnresolvedRelation [s], true, false
+- 'Project [*]
   +- 'UnresolvedRelation [t]

insert overwrite table s partition (e = 1) if not exists select * from t
'InsertIntoStatement 'UnresolvedRelation [s], Map(e -> Some(1)), true, true
+- 'Project [*]
   +- 'UnresolvedRelation [t]

insert into s select * from t
'InsertIntoStatement 'UnresolvedRelation [s], false, false
+- 'Project [*]
   +- 'UnresolvedRelation [t]

insert into table s partition (c = 'd', e = 1) select * from t
'InsertIntoStatement 'UnresolvedRelation [s], Map(c -> Some(d), e -> Some(1)), false, false
+- 'Project [*]
   +- 'UnresolvedRelation [t]

from t insert into s select * limit 1 insert into u select * where x > 5
'Union
:- 'InsertIntoStatement 'UnresolvedRelation [s], false, false
:  +- 'GlobalLimit 1
:     +- 'LocalLimit 1
:        +- 'Project [*]
:           +- 'UnresolvedRelation [t]
+- 'InsertIntoStatement 'UnresolvedRelation [u], false, false
   +- 'Project [*]
      +- 'Filter ('x > 5)
         +- 'UnresolvedRelation [t]



select a, b, sum(c) as c from d group by a, b
'Aggregate ['a, 'b], ['a, 'b, 'sum('c) AS c#2]
+- 'UnresolvedRelation [d]

select a, b, sum(c) as c from d group by a, b with cube
'Aggregate [cube('a, 'b)], ['a, 'b, 'sum('c) AS c#4]
+- 'UnresolvedRelation [d]

select a, b, sum(c) as c from d group by a, b with rollup
'Aggregate [rollup('a, 'b)], ['a, 'b, 'sum('c) AS c#6]
+- 'UnresolvedRelation [d]

select a, b, sum(c) as c from d group by a, b grouping sets((a, b), (a), ())
'GroupingSets [List('a, 'b), List('a), List()], ['a, 'b], ['a, 'b, 'sum('c) AS c#8]
+- 'UnresolvedRelation [d]



select * from t limit 10
'GlobalLimit 10
+- 'LocalLimit 10
   +- 'Project [*]
      +- 'UnresolvedRelation [t]

select * from t limit cast(9 / 4 as int)
'GlobalLimit cast((9 / 4) as int)
+- 'LocalLimit cast((9 / 4) as int)
   +- 'Project [*]
      +- 'UnresolvedRelation [t]



select * from t
window w1 as (partition by a, b order by c rows between 1 preceding and 1 following),
       w2 as w1,
       w3 as w1
'WithWindowDefinition Map(w1 -> windowspecdefinition('a, 'b, 'c ASC NULLS FIRST, specifiedwindowframe(RowFrame, -1, 1)), w2 -> windowspecdefinition('a, 'b, 'c ASC NULLS FIRST, specifiedwindowframe(RowFrame, -1, 1)), w3 -> windowspecdefinition('a, 'b, 'c ASC NULLS FIRST, specifiedwindowframe(RowFrame, -1, 1)))
+- 'Project [*]
   +- 'UnresolvedRelation [t]



select * from t lateral view explode(x) expl as x
'Project [*]
+- 'Generate 'explode('x), false, expl, ['x]
   +- 'UnresolvedRelation [t]

select *
from t
lateral view explode(x) expl
lateral view outer json_tuple(x, y) jtup q, z
'Project [*]
+- 'Generate 'json_tuple('x, 'y), true, jtup, ['q, 'z]
   +- 'Generate 'explode('x), false, expl
      +- 'UnresolvedRelation [t]

from t1
lateral view explode(x) expl as x
insert into t2
select *
lateral view json_tuple(x, y) jtup q, z
insert into t3
select *
where s < 10
      
'Union
:- 'InsertIntoStatement 'UnresolvedRelation [t2], false, false
:  +- 'Project [*]
:     +- 'Generate 'json_tuple('x, 'y), false, jtup, ['q, 'z]
:        +- 'Generate 'explode('x), false, expl, ['x]
:           +- 'UnresolvedRelation [t1]
+- 'InsertIntoStatement 'UnresolvedRelation [t3], false, false
   +- 'Project [*]
      +- 'Filter ('s < 10)
         +- 'Generate 'explode('x), false, expl, ['x]
            +- 'UnresolvedRelation [t1]

select * from t lateral view posexplode(x) posexpl as x, y
'Project [*]
+- 'Generate 'posexplode('x), false, posexpl, ['x, 'y]
   +- 'UnresolvedRelation [t]



select * from t as tt cross join u
'Project [*]
+- 'Join Cross
   :- 'SubqueryAlias tt
   :  +- 'UnresolvedRelation [t]
   +- 'UnresolvedRelation [u]

select * from t as tt , u
'Project [*]
+- 'Join Inner
   :- 'SubqueryAlias tt
   :  +- 'UnresolvedRelation [t]
   +- 'UnresolvedRelation [u]

select * from t as tt join u
'Project [*]
+- 'Join Inner
   :- 'SubqueryAlias tt
   :  +- 'UnresolvedRelation [t]
   +- 'UnresolvedRelation [u]

select * from t join u as uu on a = b
'Project [*]
+- 'Join Inner, ('a = 'b)
   :- 'UnresolvedRelation [t]
   +- 'SubqueryAlias uu
      +- 'UnresolvedRelation [u]

select * from t tt natural join u as uu
'Project [*]
+- 'Join NaturalJoin(Inner)
   :- 'SubqueryAlias tt
   :  +- 'UnresolvedRelation [t]
   +- 'SubqueryAlias uu
      +- 'UnresolvedRelation [u]

select * from t join u using(a, b)
'Project [*]
+- 'Join UsingJoin(Inner,List(a, b))
   :- 'UnresolvedRelation [t]
   +- 'UnresolvedRelation [u]

select * from t as tt inner join u
'Project [*]
+- 'Join Inner
   :- 'SubqueryAlias tt
   :  +- 'UnresolvedRelation [t]
   +- 'UnresolvedRelation [u]

select * from t inner join u as uu on a = b
'Project [*]
+- 'Join Inner, ('a = 'b)
   :- 'UnresolvedRelation [t]
   +- 'SubqueryAlias uu
      +- 'UnresolvedRelation [u]

select * from t tt natural inner join u as uu
'Project [*]
+- 'Join NaturalJoin(Inner)
   :- 'SubqueryAlias tt
   :  +- 'UnresolvedRelation [t]
   +- 'SubqueryAlias uu
      +- 'UnresolvedRelation [u]

select * from t inner join u using(a, b)
'Project [*]
+- 'Join UsingJoin(Inner,List(a, b))
   :- 'UnresolvedRelation [t]
   +- 'UnresolvedRelation [u]

select * from t as tt left join u
'Project [*]
+- 'Join LeftOuter
   :- 'SubqueryAlias tt
   :  +- 'UnresolvedRelation [t]
   +- 'UnresolvedRelation [u]

select * from t left join u as uu on a = b
'Project [*]
+- 'Join LeftOuter, ('a = 'b)
   :- 'UnresolvedRelation [t]
   +- 'SubqueryAlias uu
      +- 'UnresolvedRelation [u]

select * from t tt natural left join u as uu
'Project [*]
+- 'Join NaturalJoin(LeftOuter)
   :- 'SubqueryAlias tt
   :  +- 'UnresolvedRelation [t]
   +- 'SubqueryAlias uu
      +- 'UnresolvedRelation [u]

select * from t left join u using(a, b)
'Project [*]
+- 'Join UsingJoin(LeftOuter,List(a, b))
   :- 'UnresolvedRelation [t]
   +- 'UnresolvedRelation [u]

select * from t as tt left outer join u
'Project [*]
+- 'Join LeftOuter
   :- 'SubqueryAlias tt
   :  +- 'UnresolvedRelation [t]
   +- 'UnresolvedRelation [u]

select * from t left outer join u as uu on a = b
'Project [*]
+- 'Join LeftOuter, ('a = 'b)
   :- 'UnresolvedRelation [t]
   +- 'SubqueryAlias uu
      +- 'UnresolvedRelation [u]

select * from t tt natural left outer join u as uu
'Project [*]
+- 'Join NaturalJoin(LeftOuter)
   :- 'SubqueryAlias tt
   :  +- 'UnresolvedRelation [t]
   +- 'SubqueryAlias uu
      +- 'UnresolvedRelation [u]

select * from t left outer join u using(a, b)
'Project [*]
+- 'Join UsingJoin(LeftOuter,List(a, b))
   :- 'UnresolvedRelation [t]
   +- 'UnresolvedRelation [u]

select * from t as tt right join u
'Project [*]
+- 'Join RightOuter
   :- 'SubqueryAlias tt
   :  +- 'UnresolvedRelation [t]
   +- 'UnresolvedRelation [u]

select * from t right join u as uu on a = b
'Project [*]
+- 'Join RightOuter, ('a = 'b)
   :- 'UnresolvedRelation [t]
   +- 'SubqueryAlias uu
      +- 'UnresolvedRelation [u]

select * from t tt natural right join u as uu
'Project [*]
+- 'Join NaturalJoin(RightOuter)
   :- 'SubqueryAlias tt
   :  +- 'UnresolvedRelation [t]
   +- 'SubqueryAlias uu
      +- 'UnresolvedRelation [u]

select * from t right join u using(a, b)
'Project [*]
+- 'Join UsingJoin(RightOuter,List(a, b))
   :- 'UnresolvedRelation [t]
   +- 'UnresolvedRelation [u]

select * from t as tt right outer join u
'Project [*]
+- 'Join RightOuter
   :- 'SubqueryAlias tt
   :  +- 'UnresolvedRelation [t]
   +- 'UnresolvedRelation [u]

select * from t right outer join u as uu on a = b
'Project [*]
+- 'Join RightOuter, ('a = 'b)
   :- 'UnresolvedRelation [t]
   +- 'SubqueryAlias uu
      +- 'UnresolvedRelation [u]

select * from t tt natural right outer join u as uu
'Project [*]
+- 'Join NaturalJoin(RightOuter)
   :- 'SubqueryAlias tt
   :  +- 'UnresolvedRelation [t]
   +- 'SubqueryAlias uu
      +- 'UnresolvedRelation [u]

select * from t right outer join u using(a, b)
'Project [*]
+- 'Join UsingJoin(RightOuter,List(a, b))
   :- 'UnresolvedRelation [t]
   +- 'UnresolvedRelation [u]

select * from t as tt full join u
'Project [*]
+- 'Join FullOuter
   :- 'SubqueryAlias tt
   :  +- 'UnresolvedRelation [t]
   +- 'UnresolvedRelation [u]

select * from t full join u as uu on a = b
'Project [*]
+- 'Join FullOuter, ('a = 'b)
   :- 'UnresolvedRelation [t]
   +- 'SubqueryAlias uu
      +- 'UnresolvedRelation [u]

select * from t tt natural full join u as uu
'Project [*]
+- 'Join NaturalJoin(FullOuter)
   :- 'SubqueryAlias tt
   :  +- 'UnresolvedRelation [t]
   +- 'SubqueryAlias uu
      +- 'UnresolvedRelation [u]

select * from t full join u using(a, b)
'Project [*]
+- 'Join UsingJoin(FullOuter,List(a, b))
   :- 'UnresolvedRelation [t]
   +- 'UnresolvedRelation [u]

select * from t as tt full outer join u
'Project [*]
+- 'Join FullOuter
   :- 'SubqueryAlias tt
   :  +- 'UnresolvedRelation [t]
   +- 'UnresolvedRelation [u]

select * from t full outer join u as uu on a = b
'Project [*]
+- 'Join FullOuter, ('a = 'b)
   :- 'UnresolvedRelation [t]
   +- 'SubqueryAlias uu
      +- 'UnresolvedRelation [u]

select * from t tt natural full outer join u as uu
'Project [*]
+- 'Join NaturalJoin(FullOuter)
   :- 'SubqueryAlias tt
   :  +- 'UnresolvedRelation [t]
   +- 'SubqueryAlias uu
      +- 'UnresolvedRelation [u]

select * from t full outer join u using(a, b)
'Project [*]
+- 'Join UsingJoin(FullOuter,List(a, b))
   :- 'UnresolvedRelation [t]
   +- 'UnresolvedRelation [u]

select * from t as tt left semi join u
'Project [*]
+- 'Join LeftSemi
   :- 'SubqueryAlias tt
   :  +- 'UnresolvedRelation [t]
   +- 'UnresolvedRelation [u]

select * from t left semi join u as uu on a = b
'Project [*]
+- 'Join LeftSemi, ('a = 'b)
   :- 'UnresolvedRelation [t]
   +- 'SubqueryAlias uu
      +- 'UnresolvedRelation [u]

select * from t left semi join u using(a, b)
'Project [*]
+- 'Join UsingJoin(LeftSemi,List(a, b))
   :- 'UnresolvedRelation [t]
   +- 'UnresolvedRelation [u]

select * from t as tt semi join u
'Project [*]
+- 'Join LeftSemi
   :- 'SubqueryAlias tt
   :  +- 'UnresolvedRelation [t]
   +- 'UnresolvedRelation [u]

select * from t semi join u as uu on a = b
'Project [*]
+- 'Join LeftSemi, ('a = 'b)
   :- 'UnresolvedRelation [t]
   +- 'SubqueryAlias uu
      +- 'UnresolvedRelation [u]

select * from t semi join u using(a, b)
'Project [*]
+- 'Join UsingJoin(LeftSemi,List(a, b))
   :- 'UnresolvedRelation [t]
   +- 'UnresolvedRelation [u]

select * from t as tt left anti join u
'Project [*]
+- 'Join LeftAnti
   :- 'SubqueryAlias tt
   :  +- 'UnresolvedRelation [t]
   +- 'UnresolvedRelation [u]

select * from t left anti join u as uu on a = b
'Project [*]
+- 'Join LeftAnti, ('a = 'b)
   :- 'UnresolvedRelation [t]
   +- 'SubqueryAlias uu
      +- 'UnresolvedRelation [u]

select * from t left anti join u using(a, b)
'Project [*]
+- 'Join UsingJoin(LeftAnti,List(a, b))
   :- 'UnresolvedRelation [t]
   +- 'UnresolvedRelation [u]

select * from t as tt anti join u
'Project [*]
+- 'Join LeftAnti
   :- 'SubqueryAlias tt
   :  +- 'UnresolvedRelation [t]
   +- 'UnresolvedRelation [u]

select * from t anti join u as uu on a = b
'Project [*]
+- 'Join LeftAnti, ('a = 'b)
   :- 'UnresolvedRelation [t]
   +- 'SubqueryAlias uu
      +- 'UnresolvedRelation [u]

select * from t anti join u using(a, b)
'Project [*]
+- 'Join UsingJoin(LeftAnti,List(a, b))
   :- 'UnresolvedRelation [t]
   +- 'UnresolvedRelation [u]

select * from a join b join c right join d
'Project [*]
+- 'Join RightOuter
   :- 'Join Inner
   :  :- 'Join Inner
   :  :  :- 'UnresolvedRelation [a]
   :  :  +- 'UnresolvedRelation [b]
   :  +- 'UnresolvedRelation [c]
   +- 'UnresolvedRelation [d]

select * from t1 cross join t2 join t3 on t3.id = t1.id join t4 on t4.id = t1.id
'Project [*]
+- 'Join Inner, ('t4.id = 't1.id)
   :- 'Join Inner, ('t3.id = 't1.id)
   :  :- 'Join Cross
   :  :  :- 'UnresolvedRelation [t1]
   :  :  +- 'UnresolvedRelation [t2]
   :  +- 'UnresolvedRelation [t3]
   +- 'UnresolvedRelation [t4]

select * from t1 inner join (t2 inner join t3 on col3 = col2) on col3 = col1
'Project [*]
+- 'Join Inner, ('col3 = 'col1)
   :- 'UnresolvedRelation [t1]
   +- 'Join Inner, ('col3 = 'col2)
      :- 'UnresolvedRelation [t2]
      +- 'UnresolvedRelation [t3]

select * from t1 inner join (t2 inner join t3) on col3 = col2
'Project [*]
+- 'Join Inner, ('col3 = 'col2)
   :- 'UnresolvedRelation [t1]
   +- 'Join Inner
      :- 'UnresolvedRelation [t2]
      +- 'UnresolvedRelation [t3]

select * from t1 inner join (t2 inner join t3 on col3 = col2)
'Project [*]
+- 'Join Inner
   :- 'UnresolvedRelation [t1]
   +- 'Join Inner, ('col3 = 'col2)
      :- 'UnresolvedRelation [t2]
      +- 'UnresolvedRelation [t3]

select * from t1, t3 join t2 on t1.col1 = t2.col2
'Project [*]
+- 'Join Inner, ('t1.col1 = 't2.col2)
   :- 'Join Inner
   :  :- 'UnresolvedRelation [t1]
   :  +- 'UnresolvedRelation [t3]
   +- 'UnresolvedRelation [t2]


select * from t tablesample(100 rows)
'Project [*]
+- 'GlobalLimit 100
   +- 'LocalLimit 100
      +- 'UnresolvedRelation [t]


select * from t tablesample(43 percent) as x
'Project [*]
+- 'Sample 0.0, 0.43, false, 10
   +- 'SubqueryAlias x
      +- 'UnresolvedRelation [t]

select * from t tablesample(bucket 4 out of 10) as x
'Project [*]
+- 'Sample 0.0, 0.4, false, 10
   +- 'SubqueryAlias x
      +- 'UnresolvedRelation [t]



select id from (t0)
'Project ['id]
+- 'UnresolvedRelation [t0]

select id from ((((((t0))))))
'Project ['id]
+- 'UnresolvedRelation [t0]

(select * from t1) union distinct (select * from t2)
'Distinct
+- 'Union
   :- 'Project [*]
   :  +- 'UnresolvedRelation [t1]
   +- 'Project [*]
      +- 'UnresolvedRelation [t2]

select * from ((select * from t1) union (select * from t2)) t
'Project [*]
+- 'SubqueryAlias t
   +- 'Distinct
      +- 'Union
         :- 'Project [*]
         :  +- 'UnresolvedRelation [t1]
         +- 'Project [*]
            +- 'UnresolvedRelation [t2]

select  id
from (((select id from t0)
       union all
       (select  id from t0))
      union all
      (select id from t0)) as u_1
      
'Project ['id]
+- 'SubqueryAlias u_1
   +- 'Union
      :- 'Union
      :  :- 'Project ['id]
      :  :  +- 'UnresolvedRelation [t0]
      :  +- 'Project ['id]
      :     +- 'UnresolvedRelation [t0]
      +- 'Project ['id]
         +- 'UnresolvedRelation [t0]



select (select max(b) from s) ss from t
'Project [scalar-subquery#10 [] AS ss#11]
:  +- 'Project [unresolvedalias('max('b), None)]
:     +- 'UnresolvedRelation [s]
+- 'UnresolvedRelation [t]

select * from t where a = (select b from s)
'Project [*]
+- 'Filter ('a = scalar-subquery#14 [])
   :  +- 'Project ['b]
   :     +- 'UnresolvedRelation [s]
   +- 'UnresolvedRelation [t]

select g from t group by g having a > (select b from s)
'UnresolvedHaving ('a > scalar-subquery#16 [])
:  +- 'Project ['b]
:     +- 'UnresolvedRelation [s]
+- 'Aggregate ['g], ['g]
   +- 'UnresolvedRelation [t]



table t
'UnresolvedRelation [t]

table d.t
'UnresolvedRelation [d, t]



select * from range(2)
'Project [*]
+- 'UnresolvedTableValuedFunction range, [2]



SELECT * FROM range(10) AS t
'Project [*]
+- 'SubqueryAlias t
   +- 'UnresolvedTableValuedFunction range, [10]

SELECT * FROM range(7) AS t(a)
'Project [*]
+- 'SubqueryAlias t
   +- 'UnresolvedTableValuedFunction range, [7], [a]



SELECT * FROM testData AS t(col1, col2)
'Project [*]
+- 'UnresolvedSubqueryColumnAliases [col1, col2]
   +- 'SubqueryAlias t
      +- 'UnresolvedRelation [testData]



SELECT * FROM (SELECT a AS x, b AS y FROM t) t(col1, col2)
'Project [*]
+- 'UnresolvedSubqueryColumnAliases [col1, col2]
   +- 'SubqueryAlias t
      +- 'Project ['a AS x#18, 'b AS y#19]
         +- 'UnresolvedRelation [t]



SELECT * FROM (src1 s1 INNER JOIN src2 s2 ON s1.id = s2.id) dst(a, b, c, d)
'Project [*]
+- 'UnresolvedSubqueryColumnAliases [a, b, c, d]
   +- 'SubqueryAlias dst
      +- 'Join Inner, ('s1.id = 's2.id)
         :- 'SubqueryAlias s1
         :  +- 'UnresolvedRelation [src1]
         +- 'SubqueryAlias s2
            +- 'UnresolvedRelation [src2]



values 1, 2, 3, 4
'UnresolvedInlineTable [col1], [List(1), List(2), List(3), List(4)]

values (1, 'a'), (2, 'b') as tbl(a, b)
'SubqueryAlias tbl
+- 'UnresolvedInlineTable [a, b], [List(1, a), List(2, b)]



select a, b from db.c where x !< 1
'Project ['a, 'b]
+- 'Filter ('x >= 1)
   +- 'UnresolvedRelation [db, c]

select a, b from db.c where x !> 1
'Project ['a, 'b]
+- 'Filter ('x <= 1)
   +- 'UnresolvedRelation [db, c]














SELECT * FROM a
UNION
SELECT * FROM b
EXCEPT
SELECT * FROM c
INTERSECT
SELECT * FROM d
      
'Except false
:- 'Distinct
:  +- 'Union
:     :- 'Project [*]
:     :  +- 'UnresolvedRelation [a]
:     +- 'Project [*]
:        +- 'UnresolvedRelation [b]
+- 'Intersect false
   :- 'Project [*]
   :  +- 'UnresolvedRelation [c]
   +- 'Project [*]
      +- 'UnresolvedRelation [d]


SELECT * FROM a
UNION
SELECT * FROM b
EXCEPT ALL
SELECT * FROM c
INTERSECT ALL
SELECT * FROM d
      
'ExceptAll true
:- 'Distinct
:  +- 'Union
:     :- 'Project [*]
:     :  +- 'UnresolvedRelation [a]
:     +- 'Project [*]
:        +- 'UnresolvedRelation [b]
+- 'IntersectAll true
   :- 'Project [*]
   :  +- 'UnresolvedRelation [c]
   +- 'Project [*]
      +- 'UnresolvedRelation [d]


SELECT * FROM a
UNION
SELECT * FROM b
EXCEPT
SELECT * FROM c
INTERSECT
SELECT * FROM d
      
'Intersect false
:- 'Except false
:  :- 'Distinct
:  :  +- 'Union
:  :     :- 'Project [*]
:  :     :  +- 'UnresolvedRelation [a]
:  :     +- 'Project [*]
:  :        +- 'UnresolvedRelation [b]
:  +- 'Project [*]
:     +- 'UnresolvedRelation [c]
+- 'Project [*]
   +- 'UnresolvedRelation [d]


SELECT * FROM a
UNION
SELECT * FROM b
EXCEPT ALL
SELECT * FROM c
INTERSECT ALL
SELECT * FROM d
      
'IntersectAll true
:- 'ExceptAll true
:  :- 'Distinct
:  :  +- 'Union
:  :     :- 'Project [*]
:  :     :  +- 'UnresolvedRelation [a]
:  :     +- 'Project [*]
:  :        +- 'UnresolvedRelation [b]
:  +- 'Project [*]
:     +- 'UnresolvedRelation [c]
+- 'Project [*]
   +- 'UnresolvedRelation [d]


SELECT * FROM a
UNION
SELECT * FROM b
EXCEPT
SELECT * FROM c
INTERSECT
SELECT * FROM d
      
'Except false
:- 'Distinct
:  +- 'Union
:     :- 'Project [*]
:     :  +- 'UnresolvedRelation [a]
:     +- 'Project [*]
:        +- 'UnresolvedRelation [b]
+- 'Intersect false
   :- 'Project [*]
   :  +- 'UnresolvedRelation [c]
   +- 'Project [*]
      +- 'UnresolvedRelation [d]


SELECT * FROM a
UNION
SELECT * FROM b
EXCEPT ALL
SELECT * FROM c
INTERSECT ALL
SELECT * FROM d
      
'ExceptAll true
:- 'Distinct
:  +- 'Union
:     :- 'Project [*]
:     :  +- 'UnresolvedRelation [a]
:     +- 'Project [*]
:        +- 'UnresolvedRelation [b]
+- 'IntersectAll true
   :- 'Project [*]
   :  +- 'UnresolvedRelation [c]
   +- 'Project [*]
      +- 'UnresolvedRelation [d]







TABLE testcat.db.tab
'UnresolvedRelation [testcat, db, tab]

SELECT * FROM testcat.db.tab
'Project [*]
+- 'UnresolvedRelation [testcat, db, tab]


WITH cte1 AS (SELECT * FROM testcat.db.tab)
SELECT * FROM cte1
      
CTE [cte1]
:  +- 'SubqueryAlias cte1
:     +- 'Project [*]
:        +- 'UnresolvedRelation [testcat, db, tab]
+- 'Project [*]
   +- 'UnresolvedRelation [cte1]

SELECT /*+ BROADCAST(tab) */ * FROM testcat.db.tab
'UnresolvedHint BROADCAST, ['tab]
+- 'Project [*]
   +- 'UnresolvedRelation [testcat, db, tab]



WITH t(x) AS (SELECT c FROM a) SELECT * FROM t
CTE [t]
:  +- 'SubqueryAlias t
:     +- 'UnresolvedSubqueryColumnAliases [x]
:        +- 'Project ['c]
:           +- 'UnresolvedRelation [a]
+- 'Project [*]
   +- 'UnresolvedRelation [t]



select 1;
'Project [unresolvedalias(1, None)]
+- OneRowRelation

select a, b;
'Project ['a, 'b]
+- OneRowRelation

select a, b from db.c;;;
'Project ['a, 'b]
+- 'UnresolvedRelation [db, c]

select a, b from db.c; ;;  ;
'Project ['a, 'b]
+- 'UnresolvedRelation [db, c]
```