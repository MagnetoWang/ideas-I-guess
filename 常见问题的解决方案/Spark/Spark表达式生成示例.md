
## 表达式参考
1. org/apache/spark/sql/catalyst/parser/ExpressionParserSuite.scala


```
SQL 表达式字符串
*
Expression 表达式结构
*

SQL 表达式字符串
a.b.*
Expression 表达式结构
List(a, b).*


SQL 表达式字符串
a
Expression 表达式结构
'a

SQL 表达式字符串
a as b
Expression 表达式结构

'a AS b#0

SQL 表达式字符串
a b
Expression 表达式结构
'a AS b#0

SQL 表达式字符串
a as (b, c)
Expression 表达式结构
'a AS List(b, c)

SQL 表达式字符串
a() (b, c)
Expression 表达式结构
'a() AS List(b, c)

SQL 表达式字符串
1SL
Expression 表达式结构
'1SL

SQL 表达式字符串
a.* b
Expression 表达式结构
List(a).* AS b#3



SQL 表达式字符串
a and b
Expression 表达式结构
('a AND 'b)

SQL 表达式字符串
a or b
Expression 表达式结构
('a OR 'b)

SQL 表达式字符串
a and b or c and d
Expression 表达式结构
(('a AND 'b) OR ('c AND 'd))

SQL 表达式字符串
a or b or c and d
Expression 表达式结构
(('a OR 'b) OR ('c AND 'd))

SQL 表达式字符串
a or b or c or d or e or f
Expression 表达式结构
((('a OR 'b) OR 'c) OR (('d OR 'e) OR 'f))

SQL 表达式字符串
a and b and c and d and e and f
Expression 表达式结构
((('a AND 'b) AND 'c) AND (('d AND 'e) AND 'f))





SQL 表达式字符串
not a
Expression 表达式结构
NOT 'a

SQL 表达式字符串
!a
Expression 表达式结构
NOT 'a

SQL 表达式字符串
not true > true
Expression 表达式结构
NOT (true > true)



SQL 表达式字符串
exists (select 1 from b where b.x = a.x)
Expression 表达式结构
exists#5 []



SQL 表达式字符串
a = b
Expression 表达式结构
('a = 'b)

SQL 表达式字符串
a == b
Expression 表达式结构
('a = 'b)

SQL 表达式字符串
a <=> b
Expression 表达式结构
('a <=> 'b)

SQL 表达式字符串
a <> b
Expression 表达式结构
NOT ('a = 'b)

SQL 表达式字符串
a != b
Expression 表达式结构
NOT ('a = 'b)

SQL 表达式字符串
a < b
Expression 表达式结构
('a < 'b)

SQL 表达式字符串
a <= b
Expression 表达式结构
('a <= 'b)

SQL 表达式字符串
a !> b
Expression 表达式结构
('a <= 'b)

SQL 表达式字符串
a > b
Expression 表达式结构
('a > 'b)

SQL 表达式字符串
a >= b
Expression 表达式结构
('a >= 'b)

SQL 表达式字符串
a !< b
Expression 表达式结构
('a >= 'b)



SQL 表达式字符串
a between b and c
Expression 表达式结构
(('a >= 'b) AND ('a <= 'c))

SQL 表达式字符串
a not between b and c
Expression 表达式结构
NOT (('a >= 'b) AND ('a <= 'c))



SQL 表达式字符串
a in (b, c, d)
Expression 表达式结构
'a IN ('b,'c,'d)

SQL 表达式字符串
a not in (b, c, d)
Expression 表达式结构
NOT 'a IN ('b,'c,'d)



SQL 表达式字符串
a in (select b from c)
Expression 表达式结构
'a IN (list#7 [])

SQL 表达式字符串
(a, b, c) in (select d, e, f from g)
Expression 表达式结构
named_struct(a, 'a, b, 'b, c, 'c) IN (list#9 [])

SQL 表达式字符串
(a, b) in (select c from d)
Expression 表达式结构
named_struct(a, 'a, b, 'b) IN (list#11 [])

SQL 表达式字符串
(a) in (select b from c)
Expression 表达式结构
'a IN (list#13 [])



SQL 表达式字符串
a like 'pattern%'
Expression 表达式结构
'a LIKE pattern%

SQL 表达式字符串
a not like 'pattern%'
Expression 表达式结构
NOT 'a LIKE pattern%

SQL 表达式字符串
a rlike 'pattern%'
Expression 表达式结构
'a RLIKE pattern%

SQL 表达式字符串
a not rlike 'pattern%'
Expression 表达式结构
NOT 'a RLIKE pattern%

SQL 表达式字符串
a regexp 'pattern%'
Expression 表达式结构
'a RLIKE pattern%

SQL 表达式字符串
a not regexp 'pattern%'
Expression 表达式结构
NOT 'a RLIKE pattern%



SQL 表达式字符串
a like 'pattern%' escape '#'
Expression 表达式结构
'a LIKE pattern% ESCAPE '#'

SQL 表达式字符串
a like 'pattern%' escape '"'
Expression 表达式结构
'a LIKE pattern% ESCAPE '"'

SQL 表达式字符串
a not like 'pattern%' escape '#'
Expression 表达式结构
NOT 'a LIKE pattern% ESCAPE '#'

SQL 表达式字符串
a not like 'pattern%' escape '"'
Expression 表达式结构
NOT 'a LIKE pattern% ESCAPE '"'



SQL 表达式字符串
a rlike '^\x20[\x20-\x23]+$'
Expression 表达式结构
'a RLIKE ^\x20[\x20-\x23]+$

SQL 表达式字符串
a rlike 'pattern\\'
Expression 表达式结构
'a RLIKE pattern\\

SQL 表达式字符串
a rlike 'pattern\t\n'
Expression 表达式结构
'a RLIKE pattern\t\n



SQL 表达式字符串
a is null
Expression 表达式结构
isnull('a)

SQL 表达式字符串
a is not null
Expression 表达式结构
isnotnull('a)

SQL 表达式字符串
a = b is null
Expression 表达式结构
isnull(('a = 'b))

SQL 表达式字符串
a = b is not null
Expression 表达式结构
isnotnull(('a = 'b))



SQL 表达式字符串
a is distinct from b
Expression 表达式结构
NOT ('a <=> 'b)

SQL 表达式字符串
a is not distinct from b
Expression 表达式结构
('a <=> 'b)



SQL 表达式字符串
a * b
Expression 表达式结构
('a * 'b)

SQL 表达式字符串
a / b
Expression 表达式结构
('a / 'b)

SQL 表达式字符串
a DIV b
Expression 表达式结构
('a div 'b)

SQL 表达式字符串
a % b
Expression 表达式结构
('a % 'b)

SQL 表达式字符串
a + b
Expression 表达式结构
('a + 'b)

SQL 表达式字符串
a - b
Expression 表达式结构
('a - 'b)

SQL 表达式字符串
a & b
Expression 表达式结构
('a & 'b)

SQL 表达式字符串
a ^ b
Expression 表达式结构
('a ^ 'b)

SQL 表达式字符串
a | b
Expression 表达式结构
('a | 'b)

SQL 表达式字符串
a * t | b ^ c & d - e + f % g DIV h / i * k
Expression 表达式结构
(('a * 't) | ('b ^ ('c & (('d - 'e) + (((('f % 'g) div 'h) / 'i) * 'k)))))


SQL 表达式字符串
+a
Expression 表达式结构
positive('a)


SQL 表达式字符串
-a
Expression 表达式结构
-'a

SQL 表达式字符串
~a
Expression 表达式结构
~'a

SQL 表达式字符串
-+~~a
Expression 表达式结构
-positive(~~'a)



SQL 表达式字符串
cast(a as int)
Expression 表达式结构
cast('a as int)

SQL 表达式字符串
cast(a as timestamp)
Expression 表达式结构
cast('a as timestamp)

SQL 表达式字符串
cast(a as array<int>)
Expression 表达式结构
cast('a as array<int>)

SQL 表达式字符串
cast(cast(a as int) as long)
Expression 表达式结构
cast(cast('a as int) as bigint)



SQL 表达式字符串
foo()
Expression 表达式结构
'foo()

SQL 表达式字符串
foo.bar()
Expression 表达式结构
'foo.bar()

SQL 表达式字符串
foo(*)
Expression 表达式结构
'foo(*)

SQL 表达式字符串
count(*)
Expression 表达式结构
'count(1)

SQL 表达式字符串
foo(a, b)
Expression 表达式结构
'foo('a, 'b)

SQL 表达式字符串
foo(all a, b)
Expression 表达式结构
'foo('a, 'b)

SQL 表达式字符串
foo(distinct a, b)
Expression 表达式结构
'foo('a, 'b)

SQL 表达式字符串
grouping(distinct a, b)
Expression 表达式结构
'grouping('a, 'b)

SQL 表达式字符串
`select`(all a, b)
Expression 表达式结构
'select('a, 'b)



SQL 表达式字符串
x -> x + 1
Expression 表达式结构
lambdafunction((lambda 'x + 1), lambda 'x, false)

SQL 表达式字符串
(x, y) -> x + y
Expression 表达式结构
lambdafunction((lambda 'x + lambda 'y), lambda 'x, lambda 'y, false)



SQL 表达式字符串
foo(*) over w1
Expression 表达式结构
unresolvedwindowexpression('foo(*), WindowSpecReference(w1))

SQL 表达式字符串
foo(*) over ()
Expression 表达式结构
'foo(*) windowspecdefinition(unspecifiedframe$())

SQL 表达式字符串
foo(*) over (partition by a, b)
Expression 表达式结构
'foo(*) windowspecdefinition('a, 'b, unspecifiedframe$())

SQL 表达式字符串
foo(*) over (distribute by a, b)
Expression 表达式结构
'foo(*) windowspecdefinition('a, 'b, unspecifiedframe$())

SQL 表达式字符串
foo(*) over (cluster by a, b)
Expression 表达式结构
'foo(*) windowspecdefinition('a, 'b, unspecifiedframe$())

SQL 表达式字符串
foo(*) over (order by a desc, b asc)
Expression 表达式结构
'foo(*) windowspecdefinition('a DESC NULLS LAST, 'b ASC NULLS FIRST, unspecifiedframe$())

SQL 表达式字符串
foo(*) over (sort by a desc, b asc)
Expression 表达式结构
'foo(*) windowspecdefinition('a DESC NULLS LAST, 'b ASC NULLS FIRST, unspecifiedframe$())

SQL 表达式字符串
foo(*) over (partition by a, b order by c)
Expression 表达式结构
'foo(*) windowspecdefinition('a, 'b, 'c ASC NULLS FIRST, unspecifiedframe$())

SQL 表达式字符串
foo(*) over (distribute by a, b sort by c)
Expression 表达式结构
'foo(*) windowspecdefinition('a, 'b, 'c ASC NULLS FIRST, unspecifiedframe$())

SQL 表达式字符串
sum(product + 1) over (partition by ((product) + (1)) order by 2)
Expression 表达式结构
'sum(('product + 1)) windowspecdefinition(('product + 1), 2 ASC NULLS FIRST, unspecifiedframe$())

SQL 表达式字符串
sum(product + 1) over (partition by ((product / 2) + 1) order by 2)
Expression 表达式结构
'sum(('product + 1)) windowspecdefinition((('product / 2) + 1), 2 ASC NULLS FIRST, unspecifiedframe$())



SQL 表达式字符串
foo(*) over (partition by a order by b rows unbounded preceding)
Expression 表达式结构
'foo(*) windowspecdefinition('a, 'b ASC NULLS FIRST, specifiedwindowframe(RowFrame, unboundedpreceding$(), currentrow$()))

SQL 表达式字符串
foo(*) over (partition by a order by b rows 2147483648 preceding)
Expression 表达式结构
'foo(*) windowspecdefinition('a, 'b ASC NULLS FIRST, specifiedwindowframe(RowFrame, -2147483648, currentrow$()))

SQL 表达式字符串
foo(*) over (partition by a order by b rows 10 preceding)
Expression 表达式结构
'foo(*) windowspecdefinition('a, 'b ASC NULLS FIRST, specifiedwindowframe(RowFrame, -10, currentrow$()))

SQL 表达式字符串
foo(*) over (partition by a order by b rows 3 + 1 preceding)
Expression 表达式结构
'foo(*) windowspecdefinition('a, 'b ASC NULLS FIRST, specifiedwindowframe(RowFrame, -(3 + 1), currentrow$()))

SQL 表达式字符串
foo(*) over (partition by a order by b rows 0 preceding)
Expression 表达式结构
'foo(*) windowspecdefinition('a, 'b ASC NULLS FIRST, specifiedwindowframe(RowFrame, -0, currentrow$()))

SQL 表达式字符串
foo(*) over (partition by a order by b rows current row)
Expression 表达式结构
'foo(*) windowspecdefinition('a, 'b ASC NULLS FIRST, specifiedwindowframe(RowFrame, currentrow$(), currentrow$()))

SQL 表达式字符串
foo(*) over (partition by a order by b rows 0 following)
Expression 表达式结构
'foo(*) windowspecdefinition('a, 'b ASC NULLS FIRST, specifiedwindowframe(RowFrame, 0, currentrow$()))

SQL 表达式字符串
foo(*) over (partition by a order by b rows 3 + 1 following)
Expression 表达式结构
'foo(*) windowspecdefinition('a, 'b ASC NULLS FIRST, specifiedwindowframe(RowFrame, (3 + 1), currentrow$()))

SQL 表达式字符串
foo(*) over (partition by a order by b rows 10 following)
Expression 表达式结构
'foo(*) windowspecdefinition('a, 'b ASC NULLS FIRST, specifiedwindowframe(RowFrame, 10, currentrow$()))

SQL 表达式字符串
foo(*) over (partition by a order by b rows 2147483649 following)
Expression 表达式结构
'foo(*) windowspecdefinition('a, 'b ASC NULLS FIRST, specifiedwindowframe(RowFrame, 2147483649, currentrow$()))

SQL 表达式字符串
foo(*) over (partition by a order by b rows unbounded following)
Expression 表达式结构
'foo(*) windowspecdefinition('a, 'b ASC NULLS FIRST, specifiedwindowframe(RowFrame, unboundedfollowing$(), currentrow$()))

SQL 表达式字符串
foo(*) over (partition by a order by b rows between unbounded preceding and 5 following)
Expression 表达式结构
'foo(*) windowspecdefinition('a, 'b ASC NULLS FIRST, specifiedwindowframe(RowFrame, unboundedpreceding$(), 5))

SQL 表达式字符串
foo(*) over (partition by a order by b rows between unbounded preceding and 3 + 1 following)
Expression 表达式结构
'foo(*) windowspecdefinition('a, 'b ASC NULLS FIRST, specifiedwindowframe(RowFrame, unboundedpreceding$(), (3 + 1)))

SQL 表达式字符串
foo(*) over (partition by a order by b rows between unbounded preceding and 2147483649 following)
Expression 表达式结构
'foo(*) windowspecdefinition('a, 'b ASC NULLS FIRST, specifiedwindowframe(RowFrame, unboundedpreceding$(), 2147483649))

SQL 表达式字符串
foo(*) over (partition by a order by b rows between unbounded preceding and current row)
Expression 表达式结构
'foo(*) windowspecdefinition('a, 'b ASC NULLS FIRST, specifiedwindowframe(RowFrame, unboundedpreceding$(), currentrow$()))

SQL 表达式字符串
foo(*) over (partition by a order by b rows between 2147483648 preceding and current row)
Expression 表达式结构
'foo(*) windowspecdefinition('a, 'b ASC NULLS FIRST, specifiedwindowframe(RowFrame, -2147483648, currentrow$()))

SQL 表达式字符串
foo(*) over (partition by a order by b rows between 10 preceding and current row)
Expression 表达式结构
'foo(*) windowspecdefinition('a, 'b ASC NULLS FIRST, specifiedwindowframe(RowFrame, -10, currentrow$()))

SQL 表达式字符串
foo(*) over (partition by a order by b rows between 3 + 1 preceding and current row)
Expression 表达式结构
'foo(*) windowspecdefinition('a, 'b ASC NULLS FIRST, specifiedwindowframe(RowFrame, -(3 + 1), currentrow$()))

SQL 表达式字符串
foo(*) over (partition by a order by b rows between 0 preceding and current row)
Expression 表达式结构
'foo(*) windowspecdefinition('a, 'b ASC NULLS FIRST, specifiedwindowframe(RowFrame, -0, currentrow$()))

SQL 表达式字符串
foo(*) over (partition by a order by b rows between current row and current row)
Expression 表达式结构
'foo(*) windowspecdefinition('a, 'b ASC NULLS FIRST, specifiedwindowframe(RowFrame, currentrow$(), currentrow$()))

SQL 表达式字符串
foo(*) over (partition by a order by b rows between current row and 0 following)
Expression 表达式结构
'foo(*) windowspecdefinition('a, 'b ASC NULLS FIRST, specifiedwindowframe(RowFrame, currentrow$(), 0))

SQL 表达式字符串
foo(*) over (partition by a order by b rows between current row and 5 following)
Expression 表达式结构
'foo(*) windowspecdefinition('a, 'b ASC NULLS FIRST, specifiedwindowframe(RowFrame, currentrow$(), 5))

SQL 表达式字符串
foo(*) over (partition by a order by b rows between current row and 3 + 1 following)
Expression 表达式结构
'foo(*) windowspecdefinition('a, 'b ASC NULLS FIRST, specifiedwindowframe(RowFrame, currentrow$(), (3 + 1)))

SQL 表达式字符串
foo(*) over (partition by a order by b rows between current row and 2147483649 following)
Expression 表达式结构
'foo(*) windowspecdefinition('a, 'b ASC NULLS FIRST, specifiedwindowframe(RowFrame, currentrow$(), 2147483649))

SQL 表达式字符串
foo(*) over (partition by a order by b rows between current row and unbounded following)
Expression 表达式结构
'foo(*) windowspecdefinition('a, 'b ASC NULLS FIRST, specifiedwindowframe(RowFrame, currentrow$(), unboundedfollowing$()))

SQL 表达式字符串
foo(*) over (partition by a order by b rows between 2147483648 preceding and unbounded following)
Expression 表达式结构
'foo(*) windowspecdefinition('a, 'b ASC NULLS FIRST, specifiedwindowframe(RowFrame, -2147483648, unboundedfollowing$()))

SQL 表达式字符串
foo(*) over (partition by a order by b rows between 10 preceding and unbounded following)
Expression 表达式结构
'foo(*) windowspecdefinition('a, 'b ASC NULLS FIRST, specifiedwindowframe(RowFrame, -10, unboundedfollowing$()))

SQL 表达式字符串
foo(*) over (partition by a order by b rows between 3 + 1 preceding and unbounded following)
Expression 表达式结构
'foo(*) windowspecdefinition('a, 'b ASC NULLS FIRST, specifiedwindowframe(RowFrame, -(3 + 1), unboundedfollowing$()))

SQL 表达式字符串
foo(*) over (partition by a order by b rows between 0 preceding and unbounded following)
Expression 表达式结构
'foo(*) windowspecdefinition('a, 'b ASC NULLS FIRST, specifiedwindowframe(RowFrame, -0, unboundedfollowing$()))

SQL 表达式字符串
foo(*) over (partition by a order by b rows between 10 preceding and 5 following)
Expression 表达式结构
'foo(*) windowspecdefinition('a, 'b ASC NULLS FIRST, specifiedwindowframe(RowFrame, -10, 5))

SQL 表达式字符串
foo(*) over (partition by a order by b rows between unbounded preceding and unbounded following)
Expression 表达式结构
'foo(*) windowspecdefinition('a, 'b ASC NULLS FIRST, specifiedwindowframe(RowFrame, unboundedpreceding$(), unboundedfollowing$()))

SQL 表达式字符串
foo(*) over (partition by a order by b range unbounded preceding)
Expression 表达式结构
'foo(*) windowspecdefinition('a, 'b ASC NULLS FIRST, specifiedwindowframe(RangeFrame, unboundedpreceding$(), currentrow$()))

SQL 表达式字符串
foo(*) over (partition by a order by b range 2147483648 preceding)
Expression 表达式结构
'foo(*) windowspecdefinition('a, 'b ASC NULLS FIRST, specifiedwindowframe(RangeFrame, -2147483648, currentrow$()))

SQL 表达式字符串
foo(*) over (partition by a order by b range 10 preceding)
Expression 表达式结构
'foo(*) windowspecdefinition('a, 'b ASC NULLS FIRST, specifiedwindowframe(RangeFrame, -10, currentrow$()))

SQL 表达式字符串
foo(*) over (partition by a order by b range 3 + 1 preceding)
Expression 表达式结构
'foo(*) windowspecdefinition('a, 'b ASC NULLS FIRST, specifiedwindowframe(RangeFrame, -(3 + 1), currentrow$()))

SQL 表达式字符串
foo(*) over (partition by a order by b range 0 preceding)
Expression 表达式结构
'foo(*) windowspecdefinition('a, 'b ASC NULLS FIRST, specifiedwindowframe(RangeFrame, -0, currentrow$()))

SQL 表达式字符串
foo(*) over (partition by a order by b range current row)
Expression 表达式结构
'foo(*) windowspecdefinition('a, 'b ASC NULLS FIRST, specifiedwindowframe(RangeFrame, currentrow$(), currentrow$()))

SQL 表达式字符串
foo(*) over (partition by a order by b range 0 following)
Expression 表达式结构
'foo(*) windowspecdefinition('a, 'b ASC NULLS FIRST, specifiedwindowframe(RangeFrame, 0, currentrow$()))

SQL 表达式字符串
foo(*) over (partition by a order by b range 3 + 1 following)
Expression 表达式结构
'foo(*) windowspecdefinition('a, 'b ASC NULLS FIRST, specifiedwindowframe(RangeFrame, (3 + 1), currentrow$()))

SQL 表达式字符串
foo(*) over (partition by a order by b range 10 following)
Expression 表达式结构
'foo(*) windowspecdefinition('a, 'b ASC NULLS FIRST, specifiedwindowframe(RangeFrame, 10, currentrow$()))

SQL 表达式字符串
foo(*) over (partition by a order by b range 2147483649 following)
Expression 表达式结构
'foo(*) windowspecdefinition('a, 'b ASC NULLS FIRST, specifiedwindowframe(RangeFrame, 2147483649, currentrow$()))

SQL 表达式字符串
foo(*) over (partition by a order by b range unbounded following)
Expression 表达式结构
'foo(*) windowspecdefinition('a, 'b ASC NULLS FIRST, specifiedwindowframe(RangeFrame, unboundedfollowing$(), currentrow$()))

SQL 表达式字符串
foo(*) over (partition by a order by b range between unbounded preceding and 5 following)
Expression 表达式结构
'foo(*) windowspecdefinition('a, 'b ASC NULLS FIRST, specifiedwindowframe(RangeFrame, unboundedpreceding$(), 5))

SQL 表达式字符串
foo(*) over (partition by a order by b range between unbounded preceding and 3 + 1 following)
Expression 表达式结构
'foo(*) windowspecdefinition('a, 'b ASC NULLS FIRST, specifiedwindowframe(RangeFrame, unboundedpreceding$(), (3 + 1)))

SQL 表达式字符串
foo(*) over (partition by a order by b range between unbounded preceding and 2147483649 following)
Expression 表达式结构
'foo(*) windowspecdefinition('a, 'b ASC NULLS FIRST, specifiedwindowframe(RangeFrame, unboundedpreceding$(), 2147483649))

SQL 表达式字符串
foo(*) over (partition by a order by b range between unbounded preceding and current row)
Expression 表达式结构
'foo(*) windowspecdefinition('a, 'b ASC NULLS FIRST, specifiedwindowframe(RangeFrame, unboundedpreceding$(), currentrow$()))

SQL 表达式字符串
foo(*) over (partition by a order by b range between 2147483648 preceding and current row)
Expression 表达式结构
'foo(*) windowspecdefinition('a, 'b ASC NULLS FIRST, specifiedwindowframe(RangeFrame, -2147483648, currentrow$()))

SQL 表达式字符串
foo(*) over (partition by a order by b range between 10 preceding and current row)
Expression 表达式结构
'foo(*) windowspecdefinition('a, 'b ASC NULLS FIRST, specifiedwindowframe(RangeFrame, -10, currentrow$()))

SQL 表达式字符串
foo(*) over (partition by a order by b range between 3 + 1 preceding and current row)
Expression 表达式结构
'foo(*) windowspecdefinition('a, 'b ASC NULLS FIRST, specifiedwindowframe(RangeFrame, -(3 + 1), currentrow$()))

SQL 表达式字符串
foo(*) over (partition by a order by b range between 0 preceding and current row)
Expression 表达式结构
'foo(*) windowspecdefinition('a, 'b ASC NULLS FIRST, specifiedwindowframe(RangeFrame, -0, currentrow$()))

SQL 表达式字符串
foo(*) over (partition by a order by b range between current row and current row)
Expression 表达式结构
'foo(*) windowspecdefinition('a, 'b ASC NULLS FIRST, specifiedwindowframe(RangeFrame, currentrow$(), currentrow$()))

SQL 表达式字符串
foo(*) over (partition by a order by b range between current row and 0 following)
Expression 表达式结构
'foo(*) windowspecdefinition('a, 'b ASC NULLS FIRST, specifiedwindowframe(RangeFrame, currentrow$(), 0))

SQL 表达式字符串
foo(*) over (partition by a order by b range between current row and 5 following)
Expression 表达式结构
'foo(*) windowspecdefinition('a, 'b ASC NULLS FIRST, specifiedwindowframe(RangeFrame, currentrow$(), 5))

SQL 表达式字符串
foo(*) over (partition by a order by b range between current row and 3 + 1 following)
Expression 表达式结构
'foo(*) windowspecdefinition('a, 'b ASC NULLS FIRST, specifiedwindowframe(RangeFrame, currentrow$(), (3 + 1)))

SQL 表达式字符串
foo(*) over (partition by a order by b range between current row and 2147483649 following)
Expression 表达式结构
'foo(*) windowspecdefinition('a, 'b ASC NULLS FIRST, specifiedwindowframe(RangeFrame, currentrow$(), 2147483649))

SQL 表达式字符串
foo(*) over (partition by a order by b range between current row and unbounded following)
Expression 表达式结构
'foo(*) windowspecdefinition('a, 'b ASC NULLS FIRST, specifiedwindowframe(RangeFrame, currentrow$(), unboundedfollowing$()))

SQL 表达式字符串
foo(*) over (partition by a order by b range between 2147483648 preceding and unbounded following)
Expression 表达式结构
'foo(*) windowspecdefinition('a, 'b ASC NULLS FIRST, specifiedwindowframe(RangeFrame, -2147483648, unboundedfollowing$()))

SQL 表达式字符串
foo(*) over (partition by a order by b range between 10 preceding and unbounded following)
Expression 表达式结构
'foo(*) windowspecdefinition('a, 'b ASC NULLS FIRST, specifiedwindowframe(RangeFrame, -10, unboundedfollowing$()))

SQL 表达式字符串
foo(*) over (partition by a order by b range between 3 + 1 preceding and unbounded following)
Expression 表达式结构
'foo(*) windowspecdefinition('a, 'b ASC NULLS FIRST, specifiedwindowframe(RangeFrame, -(3 + 1), unboundedfollowing$()))

SQL 表达式字符串
foo(*) over (partition by a order by b range between 0 preceding and unbounded following)
Expression 表达式结构
'foo(*) windowspecdefinition('a, 'b ASC NULLS FIRST, specifiedwindowframe(RangeFrame, -0, unboundedfollowing$()))

SQL 表达式字符串
foo(*) over (partition by a order by b range between 10 preceding and 5 following)
Expression 表达式结构
'foo(*) windowspecdefinition('a, 'b ASC NULLS FIRST, specifiedwindowframe(RangeFrame, -10, 5))

SQL 表达式字符串
foo(*) over (partition by a order by b range between unbounded preceding and unbounded following)
Expression 表达式结构
'foo(*) windowspecdefinition('a, 'b ASC NULLS FIRST, specifiedwindowframe(RangeFrame, unboundedpreceding$(), unboundedfollowing$()))



SQL 表达式字符串
(a, b)
Expression 表达式结构
named_struct(NamePlaceholder, 'a, NamePlaceholder, 'b)

SQL 表达式字符串
(a, b, c)
Expression 表达式结构
named_struct(NamePlaceholder, 'a, NamePlaceholder, 'b, NamePlaceholder, 'c)

SQL 表达式字符串
(a as b, b as c)
Expression 表达式结构
named_struct(NamePlaceholder, 'a AS b#15, NamePlaceholder, 'b AS c#16)



SQL 表达式字符串
(select max(val) from tbl) > current
Expression 表达式结构
(scalar-subquery#19 [] > 'current)

SQL 表达式字符串
a = (select b from s)
Expression 表达式结构
('a = scalar-subquery#21 [])



SQL 表达式字符串
case a when 1 then b when 2 then c else d end
Expression 表达式结构
CASE WHEN ('a = 1) THEN 'b WHEN ('a = 2) THEN 'c ELSE 'd END

SQL 表达式字符串
case (a or b) when true then c when false then d else e end
Expression 表达式结构
CASE WHEN (('a OR 'b) = true) THEN 'c WHEN (('a OR 'b) = false) THEN 'd ELSE 'e END

SQL 表达式字符串
case 'a'='a' when true then 1 end
Expression 表达式结构
CASE WHEN ((a = a) = true) THEN 1 END

SQL 表达式字符串
case when a = 1 then b when a = 2 then c else d end
Expression 表达式结构
CASE WHEN ('a = 1) THEN 'b WHEN ('a = 2) THEN 'c ELSE 'd END

SQL 表达式字符串
case when (1) + case when a > b then c else d end then f else g end
Expression 表达式结构
CASE WHEN (1 + CASE WHEN ('a > 'b) THEN 'c ELSE 'd END) THEN 'f ELSE 'g END



SQL 表达式字符串
a.b
Expression 表达式结构
'a.b

SQL 表达式字符串
`select`.b
Expression 表达式结构
'select.b

SQL 表达式字符串
(a + b).b
Expression 表达式结构
('a + 'b)[b]

SQL 表达式字符串
struct(a, b).b
Expression 表达式结构
named_struct(NamePlaceholder, 'a, NamePlaceholder, 'b)[b]



SQL 表达式字符串
a
Expression 表达式结构
'a

SQL 表达式字符串
1a
Expression 表达式结构
'1a

SQL 表达式字符串
`select`
Expression 表达式结构
'select

SQL 表达式字符串
columns
Expression 表达式结构
'columns



SQL 表达式字符串
a[b]
Expression 表达式结构
'a['b]

SQL 表达式字符串
a[1 + 1]
Expression 表达式结构
'a[(1 + 1)]

SQL 表达式字符串
`c`.a[b]
Expression 表达式结构
'c.a['b]



SQL 表达式字符串
(a)
Expression 表达式结构
'a

SQL 表达式字符串
r * (a + b)
Expression 表达式结构
('r * ('a + 'b))



SQL 表达式字符串
dAte '2016-03-11'
Expression 表达式结构
16871

SQL 表达式字符串
tImEstAmp '2016-03-11 20:54:00.000'
Expression 表达式结构
1457758440000000

SQL 表达式字符串
InterVal 'interval 3 month 1 hour'
Expression 表达式结构
3 months 1 hours

SQL 表达式字符串
INTERVAL '3 month 1 hour'
Expression 表达式结构
3 months 1 hours

SQL 表达式字符串
-interval '3 month 1 hour'
Expression 表达式结构
-3 months 1 hours

SQL 表达式字符串
interval '1 year 3 months 2 weeks 2 days 1 hour 3 minutes 2 seconds 100 millisecond 200 microseconds'
Expression 表达式结构
1 years 3 months 16 days 1 hours 3 minutes 2.1002 seconds

SQL 表达式字符串
X'A'
Expression 表达式结构
0x0A

SQL 表达式字符串
x'A10C'
Expression 表达式结构
0xA10C



SQL 表达式字符串
null
Expression 表达式结构
null

SQL 表达式字符串
trUe
Expression 表达式结构
true

SQL 表达式字符串
False
Expression 表达式结构
false

SQL 表达式字符串
787324
Expression 表达式结构
787324

SQL 表达式字符串
7873247234798249234
Expression 表达式结构
7873247234798249234

SQL 表达式字符串
78732472347982492793712334
Expression 表达式结构
78732472347982492793712334

SQL 表达式字符串
7873247234798249279371.2334
Expression 表达式结构
7873247234798249279371.2334

SQL 表达式字符串
9.0e1
Expression 表达式结构
90.0

SQL 表达式字符串
.9e+2
Expression 表达式结构
90.0

SQL 表达式字符串
0.9e+2
Expression 表达式结构
90.0

SQL 表达式字符串
900e-1BD
Expression 表达式结构
90.0

SQL 表达式字符串
900.0E-1BD
Expression 表达式结构
90.00

SQL 表达式字符串
9.e+1BD
Expression 表达式结构
90

SQL 表达式字符串
10Y
Expression 表达式结构
10

SQL 表达式字符串
10S
Expression 表达式结构
10

SQL 表达式字符串
10L
Expression 表达式结构
10

SQL 表达式字符串
10.0D
Expression 表达式结构
10.0

SQL 表达式字符串
90912830918230182310293801923652346786BD
Expression 表达式结构
90912830918230182310293801923652346786

SQL 表达式字符串
123.0E-28BD
Expression 表达式结构
1.230E-26

SQL 表达式字符串
123.08BD
Expression 表达式结构
123.08



SQL 表达式字符串
123.0BD
Expression 表达式结构
123.0

SQL 表达式字符串
123BD
Expression 表达式结构
123

SQL 表达式字符串
123E10BD
Expression 表达式结构
1230000000000

SQL 表达式字符串
123E+10BD
Expression 表达式结构
1230000000000

SQL 表达式字符串
123E-10BD
Expression 表达式结构
1.23E-8

SQL 表达式字符串
1.23E10BD
Expression 表达式结构
12300000000

SQL 表达式字符串
-1.23E10BD
Expression 表达式结构
-12300000000



SQL 表达式字符串
9e1
Expression 表达式结构
90

SQL 表达式字符串
9e-1
Expression 表达式结构
0.9

SQL 表达式字符串
-9e1
Expression 表达式结构
-90

SQL 表达式字符串
9.0e1
Expression 表达式结构
90

SQL 表达式字符串
.9e+2
Expression 表达式结构
90

SQL 表达式字符串
0.9e+2
Expression 表达式结构
90



SQL 表达式字符串
"hello"
Expression 表达式结构
hello

SQL 表达式字符串
'hello'
Expression 表达式结构
hello

SQL 表达式字符串
"hello" 'world'
Expression 表达式结构
helloworld

SQL 表达式字符串
'hello' " " 'world'
Expression 表达式结构
hello world

SQL 表达式字符串
'pattern%'
Expression 表达式结构
pattern%

SQL 表达式字符串
'no-pattern\%'
Expression 表达式结构
no-pattern\%

SQL 表达式字符串
'pattern\\%'
Expression 表达式结构
pattern\\%

SQL 表达式字符串
'pattern\\\%'
Expression 表达式结构
pattern\\\%

SQL 表达式字符串
'\0'
Expression 表达式结构
\0

SQL 表达式字符串
'\"'
Expression 表达式结构
\"

SQL 表达式字符串
'\b'
Expression 表达式结构
\b

SQL 表达式字符串
'\n'
Expression 表达式结构
\n

SQL 表达式字符串
'\r'
Expression 表达式结构
\r

SQL 表达式字符串
'\t'
Expression 表达式结构
\t

SQL 表达式字符串
'\110\145\154\154\157\041'
Expression 表达式结构
\110\145\154\154\157\041

SQL 表达式字符串
'\u0057\u006F\u0072\u006C\u0064\u0020\u003A\u0029'
Expression 表达式结构
\u0057\u006F\u0072\u006C\u0064\u0020\u003A\u0029

SQL 表达式字符串
"hello"
Expression 表达式结构
hello

SQL 表达式字符串
'hello'
Expression 表达式结构
hello

SQL 表达式字符串
"hello" 'world'
Expression 表达式结构
helloworld

SQL 表达式字符串
'hello' " " 'world'
Expression 表达式结构
hello world

SQL 表达式字符串
'pattern%'
Expression 表达式结构
pattern%

SQL 表达式字符串
'no-pattern\%'
Expression 表达式结构
no-pattern\%

SQL 表达式字符串
'pattern\\%'
Expression 表达式结构
pattern\%

SQL 表达式字符串
'pattern\\\%'
Expression 表达式结构
pattern\\%

SQL 表达式字符串
'\0'
Expression 表达式结构
 

SQL 表达式字符串
'\''
Expression 表达式结构
'

SQL 表达式字符串
'\"'
Expression 表达式结构
"

SQL 表达式字符串
'\b'
Expression 表达式结构


SQL 表达式字符串
'\n'
Expression 表达式结构



SQL 表达式字符串
'\r'
Expression 表达式结构


SQL 表达式字符串
'\t'
Expression 表达式结构
	

SQL 表达式字符串
'\Z'
Expression 表达式结构


SQL 表达式字符串
'\110\145\154\154\157\041'
Expression 表达式结构
Hello!

SQL 表达式字符串
'\u0057\u006F\u0072\u006C\u0064\u0020\u003A\u0029'
Expression 表达式结构
World :)



SQL 表达式字符串
interval 0 year
Expression 表达式结构
0 seconds

SQL 表达式字符串
-interval 0 year
Expression 表达式结构
-0 seconds

SQL 表达式字符串
interval '0' year
Expression 表达式结构
0 seconds

SQL 表达式字符串
-interval '0' year
Expression 表达式结构
-0 seconds

SQL 表达式字符串
interval 10 year
Expression 表达式结构
10 years

SQL 表达式字符串
-interval 10 year
Expression 表达式结构
-10 years

SQL 表达式字符串
interval '10' year
Expression 表达式结构
10 years

SQL 表达式字符串
-interval '10' year
Expression 表达式结构
-10 years

SQL 表达式字符串
interval -7 year
Expression 表达式结构
-7 years

SQL 表达式字符串
-interval -7 year
Expression 表达式结构
--7 years

SQL 表达式字符串
interval '-7' year
Expression 表达式结构
-7 years

SQL 表达式字符串
-interval '-7' year
Expression 表达式结构
--7 years

SQL 表达式字符串
interval 21 year
Expression 表达式结构
21 years

SQL 表达式字符串
-interval 21 year
Expression 表达式结构
-21 years

SQL 表达式字符串
interval '21' year
Expression 表达式结构
21 years

SQL 表达式字符串
-interval '21' year
Expression 表达式结构
-21 years

SQL 表达式字符串
interval 0 years
Expression 表达式结构
0 seconds

SQL 表达式字符串
-interval 0 years
Expression 表达式结构
-0 seconds

SQL 表达式字符串
interval '0' years
Expression 表达式结构
0 seconds

SQL 表达式字符串
-interval '0' years
Expression 表达式结构
-0 seconds

SQL 表达式字符串
interval 10 years
Expression 表达式结构
10 years

SQL 表达式字符串
-interval 10 years
Expression 表达式结构
-10 years

SQL 表达式字符串
interval '10' years
Expression 表达式结构
10 years

SQL 表达式字符串
-interval '10' years
Expression 表达式结构
-10 years

SQL 表达式字符串
interval -7 years
Expression 表达式结构
-7 years

SQL 表达式字符串
-interval -7 years
Expression 表达式结构
--7 years

SQL 表达式字符串
interval '-7' years
Expression 表达式结构
-7 years

SQL 表达式字符串
-interval '-7' years
Expression 表达式结构
--7 years

SQL 表达式字符串
interval 21 years
Expression 表达式结构
21 years

SQL 表达式字符串
-interval 21 years
Expression 表达式结构
-21 years

SQL 表达式字符串
interval '21' years
Expression 表达式结构
21 years

SQL 表达式字符串
-interval '21' years
Expression 表达式结构
-21 years

SQL 表达式字符串
interval 0 month
Expression 表达式结构
0 seconds

SQL 表达式字符串
-interval 0 month
Expression 表达式结构
-0 seconds

SQL 表达式字符串
interval '0' month
Expression 表达式结构
0 seconds

SQL 表达式字符串
-interval '0' month
Expression 表达式结构
-0 seconds

SQL 表达式字符串
interval 10 month
Expression 表达式结构
10 months

SQL 表达式字符串
-interval 10 month
Expression 表达式结构
-10 months

SQL 表达式字符串
interval '10' month
Expression 表达式结构
10 months

SQL 表达式字符串
-interval '10' month
Expression 表达式结构
-10 months

SQL 表达式字符串
interval -7 month
Expression 表达式结构
-7 months

SQL 表达式字符串
-interval -7 month
Expression 表达式结构
--7 months

SQL 表达式字符串
interval '-7' month
Expression 表达式结构
-7 months

SQL 表达式字符串
-interval '-7' month
Expression 表达式结构
--7 months

SQL 表达式字符串
interval 21 month
Expression 表达式结构
1 years 9 months

SQL 表达式字符串
-interval 21 month
Expression 表达式结构
-1 years 9 months

SQL 表达式字符串
interval '21' month
Expression 表达式结构
1 years 9 months

SQL 表达式字符串
-interval '21' month
Expression 表达式结构
-1 years 9 months

SQL 表达式字符串
interval 0 months
Expression 表达式结构
0 seconds

SQL 表达式字符串
-interval 0 months
Expression 表达式结构
-0 seconds

SQL 表达式字符串
interval '0' months
Expression 表达式结构
0 seconds

SQL 表达式字符串
-interval '0' months
Expression 表达式结构
-0 seconds

SQL 表达式字符串
interval 10 months
Expression 表达式结构
10 months

SQL 表达式字符串
-interval 10 months
Expression 表达式结构
-10 months

SQL 表达式字符串
interval '10' months
Expression 表达式结构
10 months

SQL 表达式字符串
-interval '10' months
Expression 表达式结构
-10 months

SQL 表达式字符串
interval -7 months
Expression 表达式结构
-7 months

SQL 表达式字符串
-interval -7 months
Expression 表达式结构
--7 months

SQL 表达式字符串
interval '-7' months
Expression 表达式结构
-7 months

SQL 表达式字符串
-interval '-7' months
Expression 表达式结构
--7 months

SQL 表达式字符串
interval 21 months
Expression 表达式结构
1 years 9 months

SQL 表达式字符串
-interval 21 months
Expression 表达式结构
-1 years 9 months

SQL 表达式字符串
interval '21' months
Expression 表达式结构
1 years 9 months

SQL 表达式字符串
-interval '21' months
Expression 表达式结构
-1 years 9 months

SQL 表达式字符串
interval 0 week
Expression 表达式结构
0 seconds

SQL 表达式字符串
-interval 0 week
Expression 表达式结构
-0 seconds

SQL 表达式字符串
interval '0' week
Expression 表达式结构
0 seconds

SQL 表达式字符串
-interval '0' week
Expression 表达式结构
-0 seconds

SQL 表达式字符串
interval 10 week
Expression 表达式结构
70 days

SQL 表达式字符串
-interval 10 week
Expression 表达式结构
-70 days

SQL 表达式字符串
interval '10' week
Expression 表达式结构
70 days

SQL 表达式字符串
-interval '10' week
Expression 表达式结构
-70 days

SQL 表达式字符串
interval -7 week
Expression 表达式结构
-49 days

SQL 表达式字符串
-interval -7 week
Expression 表达式结构
--49 days

SQL 表达式字符串
interval '-7' week
Expression 表达式结构
-49 days

SQL 表达式字符串
-interval '-7' week
Expression 表达式结构
--49 days

SQL 表达式字符串
interval 21 week
Expression 表达式结构
147 days

SQL 表达式字符串
-interval 21 week
Expression 表达式结构
-147 days

SQL 表达式字符串
interval '21' week
Expression 表达式结构
147 days

SQL 表达式字符串
-interval '21' week
Expression 表达式结构
-147 days

SQL 表达式字符串
interval 0 weeks
Expression 表达式结构
0 seconds

SQL 表达式字符串
-interval 0 weeks
Expression 表达式结构
-0 seconds

SQL 表达式字符串
interval '0' weeks
Expression 表达式结构
0 seconds

SQL 表达式字符串
-interval '0' weeks
Expression 表达式结构
-0 seconds

SQL 表达式字符串
interval 10 weeks
Expression 表达式结构
70 days

SQL 表达式字符串
-interval 10 weeks
Expression 表达式结构
-70 days

SQL 表达式字符串
interval '10' weeks
Expression 表达式结构
70 days

SQL 表达式字符串
-interval '10' weeks
Expression 表达式结构
-70 days

SQL 表达式字符串
interval -7 weeks
Expression 表达式结构
-49 days

SQL 表达式字符串
-interval -7 weeks
Expression 表达式结构
--49 days

SQL 表达式字符串
interval '-7' weeks
Expression 表达式结构
-49 days

SQL 表达式字符串
-interval '-7' weeks
Expression 表达式结构
--49 days

SQL 表达式字符串
interval 21 weeks
Expression 表达式结构
147 days

SQL 表达式字符串
-interval 21 weeks
Expression 表达式结构
-147 days

SQL 表达式字符串
interval '21' weeks
Expression 表达式结构
147 days

SQL 表达式字符串
-interval '21' weeks
Expression 表达式结构
-147 days

SQL 表达式字符串
interval 0 day
Expression 表达式结构
0 seconds

SQL 表达式字符串
-interval 0 day
Expression 表达式结构
-0 seconds

SQL 表达式字符串
interval '0' day
Expression 表达式结构
0 seconds

SQL 表达式字符串
-interval '0' day
Expression 表达式结构
-0 seconds

SQL 表达式字符串
interval 10 day
Expression 表达式结构
10 days

SQL 表达式字符串
-interval 10 day
Expression 表达式结构
-10 days

SQL 表达式字符串
interval '10' day
Expression 表达式结构
10 days

SQL 表达式字符串
-interval '10' day
Expression 表达式结构
-10 days

SQL 表达式字符串
interval -7 day
Expression 表达式结构
-7 days

SQL 表达式字符串
-interval -7 day
Expression 表达式结构
--7 days

SQL 表达式字符串
interval '-7' day
Expression 表达式结构
-7 days

SQL 表达式字符串
-interval '-7' day
Expression 表达式结构
--7 days

SQL 表达式字符串
interval 21 day
Expression 表达式结构
21 days

SQL 表达式字符串
-interval 21 day
Expression 表达式结构
-21 days

SQL 表达式字符串
interval '21' day
Expression 表达式结构
21 days

SQL 表达式字符串
-interval '21' day
Expression 表达式结构
-21 days

SQL 表达式字符串
interval 0 days
Expression 表达式结构
0 seconds

SQL 表达式字符串
-interval 0 days
Expression 表达式结构
-0 seconds

SQL 表达式字符串
interval '0' days
Expression 表达式结构
0 seconds

SQL 表达式字符串
-interval '0' days
Expression 表达式结构
-0 seconds

SQL 表达式字符串
interval 10 days
Expression 表达式结构
10 days

SQL 表达式字符串
-interval 10 days
Expression 表达式结构
-10 days

SQL 表达式字符串
interval '10' days
Expression 表达式结构
10 days

SQL 表达式字符串
-interval '10' days
Expression 表达式结构
-10 days

SQL 表达式字符串
interval -7 days
Expression 表达式结构
-7 days

SQL 表达式字符串
-interval -7 days
Expression 表达式结构
--7 days

SQL 表达式字符串
interval '-7' days
Expression 表达式结构
-7 days

SQL 表达式字符串
-interval '-7' days
Expression 表达式结构
--7 days

SQL 表达式字符串
interval 21 days
Expression 表达式结构
21 days

SQL 表达式字符串
-interval 21 days
Expression 表达式结构
-21 days

SQL 表达式字符串
interval '21' days
Expression 表达式结构
21 days

SQL 表达式字符串
-interval '21' days
Expression 表达式结构
-21 days

SQL 表达式字符串
interval 0 hour
Expression 表达式结构
0 seconds

SQL 表达式字符串
-interval 0 hour
Expression 表达式结构
-0 seconds

SQL 表达式字符串
interval '0' hour
Expression 表达式结构
0 seconds

SQL 表达式字符串
-interval '0' hour
Expression 表达式结构
-0 seconds

SQL 表达式字符串
interval 10 hour
Expression 表达式结构
10 hours

SQL 表达式字符串
-interval 10 hour
Expression 表达式结构
-10 hours

SQL 表达式字符串
interval '10' hour
Expression 表达式结构
10 hours

SQL 表达式字符串
-interval '10' hour
Expression 表达式结构
-10 hours

SQL 表达式字符串
interval -7 hour
Expression 表达式结构
-7 hours

SQL 表达式字符串
-interval -7 hour
Expression 表达式结构
--7 hours

SQL 表达式字符串
interval '-7' hour
Expression 表达式结构
-7 hours

SQL 表达式字符串
-interval '-7' hour
Expression 表达式结构
--7 hours

SQL 表达式字符串
interval 21 hour
Expression 表达式结构
21 hours

SQL 表达式字符串
-interval 21 hour
Expression 表达式结构
-21 hours

SQL 表达式字符串
interval '21' hour
Expression 表达式结构
21 hours

SQL 表达式字符串
-interval '21' hour
Expression 表达式结构
-21 hours

SQL 表达式字符串
interval 0 hours
Expression 表达式结构
0 seconds

SQL 表达式字符串
-interval 0 hours
Expression 表达式结构
-0 seconds

SQL 表达式字符串
interval '0' hours
Expression 表达式结构
0 seconds

SQL 表达式字符串
-interval '0' hours
Expression 表达式结构
-0 seconds

SQL 表达式字符串
interval 10 hours
Expression 表达式结构
10 hours

SQL 表达式字符串
-interval 10 hours
Expression 表达式结构
-10 hours

SQL 表达式字符串
interval '10' hours
Expression 表达式结构
10 hours

SQL 表达式字符串
-interval '10' hours
Expression 表达式结构
-10 hours

SQL 表达式字符串
interval -7 hours
Expression 表达式结构
-7 hours

SQL 表达式字符串
-interval -7 hours
Expression 表达式结构
--7 hours

SQL 表达式字符串
interval '-7' hours
Expression 表达式结构
-7 hours

SQL 表达式字符串
-interval '-7' hours
Expression 表达式结构
--7 hours

SQL 表达式字符串
interval 21 hours
Expression 表达式结构
21 hours

SQL 表达式字符串
-interval 21 hours
Expression 表达式结构
-21 hours

SQL 表达式字符串
interval '21' hours
Expression 表达式结构
21 hours

SQL 表达式字符串
-interval '21' hours
Expression 表达式结构
-21 hours

SQL 表达式字符串
interval 0 minute
Expression 表达式结构
0 seconds

SQL 表达式字符串
-interval 0 minute
Expression 表达式结构
-0 seconds

SQL 表达式字符串
interval '0' minute
Expression 表达式结构
0 seconds

SQL 表达式字符串
-interval '0' minute
Expression 表达式结构
-0 seconds

SQL 表达式字符串
interval 10 minute
Expression 表达式结构
10 minutes

SQL 表达式字符串
-interval 10 minute
Expression 表达式结构
-10 minutes

SQL 表达式字符串
interval '10' minute
Expression 表达式结构
10 minutes

SQL 表达式字符串
-interval '10' minute
Expression 表达式结构
-10 minutes

SQL 表达式字符串
interval -7 minute
Expression 表达式结构
-7 minutes

SQL 表达式字符串
-interval -7 minute
Expression 表达式结构
--7 minutes

SQL 表达式字符串
interval '-7' minute
Expression 表达式结构
-7 minutes

SQL 表达式字符串
-interval '-7' minute
Expression 表达式结构
--7 minutes

SQL 表达式字符串
interval 21 minute
Expression 表达式结构
21 minutes

SQL 表达式字符串
-interval 21 minute
Expression 表达式结构
-21 minutes

SQL 表达式字符串
interval '21' minute
Expression 表达式结构
21 minutes

SQL 表达式字符串
-interval '21' minute
Expression 表达式结构
-21 minutes

SQL 表达式字符串
interval 0 minutes
Expression 表达式结构
0 seconds

SQL 表达式字符串
-interval 0 minutes
Expression 表达式结构
-0 seconds

SQL 表达式字符串
interval '0' minutes
Expression 表达式结构
0 seconds

SQL 表达式字符串
-interval '0' minutes
Expression 表达式结构
-0 seconds

SQL 表达式字符串
interval 10 minutes
Expression 表达式结构
10 minutes

SQL 表达式字符串
-interval 10 minutes
Expression 表达式结构
-10 minutes

SQL 表达式字符串
interval '10' minutes
Expression 表达式结构
10 minutes

SQL 表达式字符串
-interval '10' minutes
Expression 表达式结构
-10 minutes

SQL 表达式字符串
interval -7 minutes
Expression 表达式结构
-7 minutes

SQL 表达式字符串
-interval -7 minutes
Expression 表达式结构
--7 minutes

SQL 表达式字符串
interval '-7' minutes
Expression 表达式结构
-7 minutes

SQL 表达式字符串
-interval '-7' minutes
Expression 表达式结构
--7 minutes

SQL 表达式字符串
interval 21 minutes
Expression 表达式结构
21 minutes

SQL 表达式字符串
-interval 21 minutes
Expression 表达式结构
-21 minutes

SQL 表达式字符串
interval '21' minutes
Expression 表达式结构
21 minutes

SQL 表达式字符串
-interval '21' minutes
Expression 表达式结构
-21 minutes

SQL 表达式字符串
interval 0 second
Expression 表达式结构
0 seconds

SQL 表达式字符串
-interval 0 second
Expression 表达式结构
-0 seconds

SQL 表达式字符串
interval '0' second
Expression 表达式结构
0 seconds

SQL 表达式字符串
-interval '0' second
Expression 表达式结构
-0 seconds

SQL 表达式字符串
interval 10 second
Expression 表达式结构
10 seconds

SQL 表达式字符串
-interval 10 second
Expression 表达式结构
-10 seconds

SQL 表达式字符串
interval '10' second
Expression 表达式结构
10 seconds

SQL 表达式字符串
-interval '10' second
Expression 表达式结构
-10 seconds

SQL 表达式字符串
interval -7 second
Expression 表达式结构
-7 seconds

SQL 表达式字符串
-interval -7 second
Expression 表达式结构
--7 seconds

SQL 表达式字符串
interval '-7' second
Expression 表达式结构
-7 seconds

SQL 表达式字符串
-interval '-7' second
Expression 表达式结构
--7 seconds

SQL 表达式字符串
interval 21 second
Expression 表达式结构
21 seconds

SQL 表达式字符串
-interval 21 second
Expression 表达式结构
-21 seconds

SQL 表达式字符串
interval '21' second
Expression 表达式结构
21 seconds

SQL 表达式字符串
-interval '21' second
Expression 表达式结构
-21 seconds

SQL 表达式字符串
interval 0 seconds
Expression 表达式结构
0 seconds

SQL 表达式字符串
-interval 0 seconds
Expression 表达式结构
-0 seconds

SQL 表达式字符串
interval '0' seconds
Expression 表达式结构
0 seconds

SQL 表达式字符串
-interval '0' seconds
Expression 表达式结构
-0 seconds

SQL 表达式字符串
interval 10 seconds
Expression 表达式结构
10 seconds

SQL 表达式字符串
-interval 10 seconds
Expression 表达式结构
-10 seconds

SQL 表达式字符串
interval '10' seconds
Expression 表达式结构
10 seconds

SQL 表达式字符串
-interval '10' seconds
Expression 表达式结构
-10 seconds

SQL 表达式字符串
interval -7 seconds
Expression 表达式结构
-7 seconds

SQL 表达式字符串
-interval -7 seconds
Expression 表达式结构
--7 seconds

SQL 表达式字符串
interval '-7' seconds
Expression 表达式结构
-7 seconds

SQL 表达式字符串
-interval '-7' seconds
Expression 表达式结构
--7 seconds

SQL 表达式字符串
interval 21 seconds
Expression 表达式结构
21 seconds

SQL 表达式字符串
-interval 21 seconds
Expression 表达式结构
-21 seconds

SQL 表达式字符串
interval '21' seconds
Expression 表达式结构
21 seconds

SQL 表达式字符串
-interval '21' seconds
Expression 表达式结构
-21 seconds

SQL 表达式字符串
interval 0 millisecond
Expression 表达式结构
0 seconds

SQL 表达式字符串
-interval 0 millisecond
Expression 表达式结构
-0 seconds

SQL 表达式字符串
interval '0' millisecond
Expression 表达式结构
0 seconds

SQL 表达式字符串
-interval '0' millisecond
Expression 表达式结构
-0 seconds

SQL 表达式字符串
interval 10 millisecond
Expression 表达式结构
0.01 seconds

SQL 表达式字符串
-interval 10 millisecond
Expression 表达式结构
-0.01 seconds

SQL 表达式字符串
interval '10' millisecond
Expression 表达式结构
0.01 seconds

SQL 表达式字符串
-interval '10' millisecond
Expression 表达式结构
-0.01 seconds

SQL 表达式字符串
interval -7 millisecond
Expression 表达式结构
-0.007 seconds

SQL 表达式字符串
-interval -7 millisecond
Expression 表达式结构
--0.007 seconds

SQL 表达式字符串
interval '-7' millisecond
Expression 表达式结构
-0.007 seconds

SQL 表达式字符串
-interval '-7' millisecond
Expression 表达式结构
--0.007 seconds

SQL 表达式字符串
interval 21 millisecond
Expression 表达式结构
0.021 seconds

SQL 表达式字符串
-interval 21 millisecond
Expression 表达式结构
-0.021 seconds

SQL 表达式字符串
interval '21' millisecond
Expression 表达式结构
0.021 seconds

SQL 表达式字符串
-interval '21' millisecond
Expression 表达式结构
-0.021 seconds

SQL 表达式字符串
interval 0 milliseconds
Expression 表达式结构
0 seconds

SQL 表达式字符串
-interval 0 milliseconds
Expression 表达式结构
-0 seconds

SQL 表达式字符串
interval '0' milliseconds
Expression 表达式结构
0 seconds

SQL 表达式字符串
-interval '0' milliseconds
Expression 表达式结构
-0 seconds

SQL 表达式字符串
interval 10 milliseconds
Expression 表达式结构
0.01 seconds

SQL 表达式字符串
-interval 10 milliseconds
Expression 表达式结构
-0.01 seconds

SQL 表达式字符串
interval '10' milliseconds
Expression 表达式结构
0.01 seconds

SQL 表达式字符串
-interval '10' milliseconds
Expression 表达式结构
-0.01 seconds

SQL 表达式字符串
interval -7 milliseconds
Expression 表达式结构
-0.007 seconds

SQL 表达式字符串
-interval -7 milliseconds
Expression 表达式结构
--0.007 seconds

SQL 表达式字符串
interval '-7' milliseconds
Expression 表达式结构
-0.007 seconds

SQL 表达式字符串
-interval '-7' milliseconds
Expression 表达式结构
--0.007 seconds

SQL 表达式字符串
interval 21 milliseconds
Expression 表达式结构
0.021 seconds

SQL 表达式字符串
-interval 21 milliseconds
Expression 表达式结构
-0.021 seconds

SQL 表达式字符串
interval '21' milliseconds
Expression 表达式结构
0.021 seconds

SQL 表达式字符串
-interval '21' milliseconds
Expression 表达式结构
-0.021 seconds

SQL 表达式字符串
interval 0 microsecond
Expression 表达式结构
0 seconds

SQL 表达式字符串
-interval 0 microsecond
Expression 表达式结构
-0 seconds

SQL 表达式字符串
interval '0' microsecond
Expression 表达式结构
0 seconds

SQL 表达式字符串
-interval '0' microsecond
Expression 表达式结构
-0 seconds

SQL 表达式字符串
interval 10 microsecond
Expression 表达式结构
0.00001 seconds

SQL 表达式字符串
-interval 10 microsecond
Expression 表达式结构
-0.00001 seconds

SQL 表达式字符串
interval '10' microsecond
Expression 表达式结构
0.00001 seconds

SQL 表达式字符串
-interval '10' microsecond
Expression 表达式结构
-0.00001 seconds

SQL 表达式字符串
interval -7 microsecond
Expression 表达式结构
-0.000007 seconds

SQL 表达式字符串
-interval -7 microsecond
Expression 表达式结构
--0.000007 seconds

SQL 表达式字符串
interval '-7' microsecond
Expression 表达式结构
-0.000007 seconds

SQL 表达式字符串
-interval '-7' microsecond
Expression 表达式结构
--0.000007 seconds

SQL 表达式字符串
interval 21 microsecond
Expression 表达式结构
0.000021 seconds

SQL 表达式字符串
-interval 21 microsecond
Expression 表达式结构
-0.000021 seconds

SQL 表达式字符串
interval '21' microsecond
Expression 表达式结构
0.000021 seconds

SQL 表达式字符串
-interval '21' microsecond
Expression 表达式结构
-0.000021 seconds

SQL 表达式字符串
interval 0 microseconds
Expression 表达式结构
0 seconds

SQL 表达式字符串
-interval 0 microseconds
Expression 表达式结构
-0 seconds

SQL 表达式字符串
interval '0' microseconds
Expression 表达式结构
0 seconds

SQL 表达式字符串
-interval '0' microseconds
Expression 表达式结构
-0 seconds

SQL 表达式字符串
interval 10 microseconds
Expression 表达式结构
0.00001 seconds

SQL 表达式字符串
-interval 10 microseconds
Expression 表达式结构
-0.00001 seconds

SQL 表达式字符串
interval '10' microseconds
Expression 表达式结构
0.00001 seconds

SQL 表达式字符串
-interval '10' microseconds
Expression 表达式结构
-0.00001 seconds

SQL 表达式字符串
interval -7 microseconds
Expression 表达式结构
-0.000007 seconds

SQL 表达式字符串
-interval -7 microseconds
Expression 表达式结构
--0.000007 seconds

SQL 表达式字符串
interval '-7' microseconds
Expression 表达式结构
-0.000007 seconds

SQL 表达式字符串
-interval '-7' microseconds
Expression 表达式结构
--0.000007 seconds

SQL 表达式字符串
interval 21 microseconds
Expression 表达式结构
0.000021 seconds

SQL 表达式字符串
-interval 21 microseconds
Expression 表达式结构
-0.000021 seconds

SQL 表达式字符串
interval '21' microseconds
Expression 表达式结构
0.000021 seconds

SQL 表达式字符串
-interval '21' microseconds
Expression 表达式结构
-0.000021 seconds

SQL 表达式字符串
interval 13.123456789 seconds
Expression 表达式结构
13.123456 seconds

SQL 表达式字符串
-interval 13.123456789 seconds
Expression 表达式结构
-13.123456 seconds

SQL 表达式字符串
interval -13.123456789 second
Expression 表达式结构
-13.123456 seconds

SQL 表达式字符串
-interval -13.123456789 second
Expression 表达式结构
--13.123456 seconds

SQL 表达式字符串
interval 13.123456 second
Expression 表达式结构
13.123456 seconds

SQL 表达式字符串
-interval 13.123456 second
Expression 表达式结构
-13.123456 seconds

SQL 表达式字符串
interval 1.001 second
Expression 表达式结构
1.001 seconds

SQL 表达式字符串
-interval 1.001 second
Expression 表达式结构
-1.001 seconds

SQL 表达式字符串
interval '123-10' year to month
Expression 表达式结构
123 years 10 months

SQL 表达式字符串
-interval '123-10' year to month
Expression 表达式结构
-123 years 10 months

SQL 表达式字符串
interval '496-0' year to month
Expression 表达式结构
496 years

SQL 表达式字符串
-interval '496-0' year to month
Expression 表达式结构
-496 years

SQL 表达式字符串
interval '-2-3' year to month
Expression 表达式结构
-2 years -3 months

SQL 表达式字符串
-interval '-2-3' year to month
Expression 表达式结构
--2 years -3 months

SQL 表达式字符串
interval '-123-0' year to month
Expression 表达式结构
-123 years

SQL 表达式字符串
-interval '-123-0' year to month
Expression 表达式结构
--123 years

SQL 表达式字符串
interval '	 -1-2	' year to month
Expression 表达式结构
-1 years -2 months

SQL 表达式字符串
-interval '	 -1-2	' year to month
Expression 表达式结构
--1 years -2 months

SQL 表达式字符串
interval '99 11:22:33.123456789' day to second
Expression 表达式结构
99 days 11 hours 22 minutes 33.123456 seconds

SQL 表达式字符串
-interval '99 11:22:33.123456789' day to second
Expression 表达式结构
-99 days 11 hours 22 minutes 33.123456 seconds

SQL 表达式字符串
interval '-99 11:22:33.123456789' day to second
Expression 表达式结构
-99 days -11 hours -22 minutes -33.123456 seconds

SQL 表达式字符串
-interval '-99 11:22:33.123456789' day to second
Expression 表达式结构
--99 days -11 hours -22 minutes -33.123456 seconds

SQL 表达式字符串
interval '10 9:8:7.123456789' day to second
Expression 表达式结构
10 days 9 hours 8 minutes 7.123456 seconds

SQL 表达式字符串
-interval '10 9:8:7.123456789' day to second
Expression 表达式结构
-10 days 9 hours 8 minutes 7.123456 seconds

SQL 表达式字符串
interval '1 0:0:0' day to second
Expression 表达式结构
1 days

SQL 表达式字符串
-interval '1 0:0:0' day to second
Expression 表达式结构
-1 days

SQL 表达式字符串
interval '-1 0:0:0' day to second
Expression 表达式结构
-1 days

SQL 表达式字符串
-interval '-1 0:0:0' day to second
Expression 表达式结构
--1 days

SQL 表达式字符串
interval '1 0:0:1' day to second
Expression 表达式结构
1 days 1 seconds

SQL 表达式字符串
-interval '1 0:0:1' day to second
Expression 表达式结构
-1 days 1 seconds

SQL 表达式字符串
interval '	 1 0:0:1 ' day to second
Expression 表达式结构
1 days 1 seconds

SQL 表达式字符串
-interval '	 1 0:0:1 ' day to second
Expression 表达式结构
-1 days 1 seconds

SQL 表达式字符串
interval '11:22:33.123456789' hour to second
Expression 表达式结构
11 hours 22 minutes 33.123456 seconds

SQL 表达式字符串
-interval '11:22:33.123456789' hour to second
Expression 表达式结构
-11 hours 22 minutes 33.123456 seconds

SQL 表达式字符串
interval '9:8:7.123456789' hour to second
Expression 表达式结构
9 hours 8 minutes 7.123456 seconds

SQL 表达式字符串
-interval '9:8:7.123456789' hour to second
Expression 表达式结构
-9 hours 8 minutes 7.123456 seconds

SQL 表达式字符串
interval '-19:18:17.123456789' hour to second
Expression 表达式结构
-19 hours -18 minutes -17.123456 seconds

SQL 表达式字符串
-interval '-19:18:17.123456789' hour to second
Expression 表达式结构
--19 hours -18 minutes -17.123456 seconds

SQL 表达式字符串
interval '0:0:0' hour to second
Expression 表达式结构
0 seconds

SQL 表达式字符串
-interval '0:0:0' hour to second
Expression 表达式结构
-0 seconds

SQL 表达式字符串
interval '0:0:1' hour to second
Expression 表达式结构
1 seconds

SQL 表达式字符串
-interval '0:0:1' hour to second
Expression 表达式结构
-1 seconds

SQL 表达式字符串
interval 3 months 4 days 22 seconds 1 millisecond
Expression 表达式结构
3 months 4 days 22.001 seconds

SQL 表达式字符串
-interval 3 months 4 days 22 seconds 1 millisecond
Expression 表达式结构
-3 months 4 days 22.001 seconds



SQL 表达式字符串
1 + r.r As q
Expression 表达式结构
(1 + 'r.r) AS q#23

SQL 表达式字符串
1 - f('o', o(bar))
Expression 表达式结构
(1 - 'f(o, 'o('bar)))



SQL 表达式字符串
123_
Expression 表达式结构
'123_

SQL 表达式字符串
1a.123_
Expression 表达式结构
'1a.123_

SQL 表达式字符串
a.123A
Expression 表达式结构
'a.123A

SQL 表达式字符串
a.123E3_column
Expression 表达式结构
'a.123E3_column

SQL 表达式字符串
a.123D_column
Expression 表达式结构
'a.123D_column

SQL 表达式字符串
a.123BD_column
Expression 表达式结构
'a.123BD_column



SQL 表达式字符串
```fo``o`.```ba``r`
Expression 表达式结构
'`fo`o.`ba`r

SQL 表达式字符串
`fo````o`.`ba````r`
Expression 表达式结构
'fo``o.ba``r



SQL 表达式字符串
first(a ignore nulls)
Expression 表达式结构
first('a, true)

SQL 表达式字符串
first(a)
Expression 表达式结构
first('a, false)

SQL 表达式字符串
last(a ignore nulls)
Expression 表达式结构
last('a, true)

SQL 表达式字符串
last(a)
Expression 表达式结构
last('a, false)


TIMESTAMP '2019-01-14 20:54:00.000'
1547499240000000
Timestamp '2000-01-01T00:55:00'
946688100000000
TIMESTAMP '2019-01-16 20:50:00.567000+01:00'
1547668200567000
TIMESTAMP '2019-01-14 20:54:00.000'
1547528040000000
Timestamp '2000-01-01T00:55:00'
946716900000000
TIMESTAMP '2019-01-16 20:50:00.567000+01:00'
1547668200567000
TIMESTAMP '2019-01-14 20:54:00.000'
1547495640000000
Timestamp '2000-01-01T00:55:00'
946684500000000
TIMESTAMP '2019-01-16 20:50:00.567000+01:00'
1547668200567000
TIMESTAMP '2019-01-14 20:54:00.000'
1547499240000000
Timestamp '2000-01-01T00:55:00'
946688100000000
TIMESTAMP '2019-01-16 20:50:00.567000+01:00'
1547668200567000
TIMESTAMP '2019-01-14 20:54:00.000'
1547528040000000
Timestamp '2000-01-01T00:55:00'
946716900000000
TIMESTAMP '2019-01-16 20:50:00.567000+01:00'
1547668200567000
TIMESTAMP '2019-01-14 20:54:00.000'
1547477640000000
Timestamp '2000-01-01T00:55:00'
946666500000000
TIMESTAMP '2019-01-16 20:50:00.567000+01:00'
1547668200567000
TIMESTAMP '2019-01-14 20:54:00.000'
1547470440000000
Timestamp '2000-01-01T00:55:00'
946659300000000
TIMESTAMP '2019-01-16 20:50:00.567000+01:00'
1547668200567000
TIMESTAMP '2019-01-14 20:54:00.000'
1547495640000000
Timestamp '2000-01-01T00:55:00'
946684500000000
TIMESTAMP '2019-01-16 20:50:00.567000+01:00'
1547668200567000


DATE '2019-01-14'
17910
DATE '2019-01'
17897
DATE '2019'
17897
DATE '2019-01-14'
17910
DATE '2019-01'
17897
DATE '2019'
17897
DATE '2019-01-14'
17910
DATE '2019-01'
17897
DATE '2019'
17897
DATE '2019-01-14'
17910
DATE '2019-01'
17897
DATE '2019'
17897
DATE '2019-01-14'
17910
DATE '2019-01'
17897
DATE '2019'
17897
DATE '2019-01-14'
17910
DATE '2019-01'
17897
DATE '2019'
17897
DATE '2019-01-14'
17910
DATE '2019-01'
17897
DATE '2019'
17897
DATE '2019-01-14'
17910
DATE '2019-01'
17897
DATE '2019'
17897



SQL 表达式字符串
current_date
Expression 表达式结构
current_date(None)

SQL 表达式字符串
current_timestamp
Expression 表达式结构
current_timestamp()

SQL 表达式字符串
current_date
Expression 表达式结构
'current_date

SQL 表达式字符串
current_timestamp
Expression 表达式结构
'current_timestamp

```