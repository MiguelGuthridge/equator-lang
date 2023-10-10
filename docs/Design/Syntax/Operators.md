# Operator syntax

## `$` variable marker

Placed before an identifier to mark it as a variable, rather than an unknown,
meaning it is defined within the local scope, rather than the scope of the
given statement.

## `:=` assignment operator

Bind an expression, condition or equation to a variable.

### Binding a simple expression

```equator
>>> $a := 1;
>>> $a;
$a => 1
```

### Binding an expression

```equator
>>> $b := x + 3;
>>> // Evaluate the expression where x = 4
>>> $b, x = 4;
$b => 7
```

### Binding an equation

```equator
>>> $c := x + 1 = y;
>>> // Solve the equation where x = 2
>>> $c, x = 2;
x = 2
y = 3
```

### Binding a condition

```equator
>>> $d := x == 5;
>>> // Evaluate the condition where x = 4
>>> $d, x = 4;
$d => false
```

## `,` comma operator

Connect expressions and equations so that they are evaluated simultaneously.

```equator
>>> x + 2 * y = 10, 2 * x = y;
x = 2
y = 4
```

## `|` pipe operator

Capture outputs from a statement to variables.

```equator
>>> // Capture values of x and y
>>> x + 2 * y = 10, 2 * x = y | $x, $y;
>>> $x;
$x => 2
```

## `->` map operator

Used alongside the pipe operator to rename variables when capturing them as
variables or unknowns.

```equator
>>> // Capture values of x and y
>>> x + 5 = 7 | x -> $a;
>>> $a;
$a => 2
```

## `&` Join operator

Join captured outputs from a statement to unknowns in the next statement. Used
in conjunction with the pipe operator

```equator
>>> // Use x and y in next function call, but rename y to a within the joined
>>> // expression
>>> x + 2 * y = 10, 2 * x = y | x, y -> a & x + a;
x + a => 6
```

## `$$` capture all operator

Capture all variables involved with a statement.

```equator
>>> // Capture both x and y, and pass them to the expression `x + y`
>>> x + 2 * y = 10, 2 * x = y | $$ & x + y;
x + y => 6
```

## `=` equality operator

The equality operator is used to signify that two sides of an equation are
equal.

```equator
>>> x + 3 = 5;
x = 2
```

If two equality operators are used in the one expression, it is evaluated as
follows:

```equator
a = b = c
```

```equator
a = b, b = c
```

Compare to [equality conditional](#equality-conditional)

## `!=` inequality operator

The inequality operator is used to signify that the two sides of an equation
are not equal.

```equator
>>> a = sqrt(9), a != 3;
a = 3
```

## `+` addition operator

## `-` subtraction operator

## `*` multiplication operator

## `/` division operator

## `%` modulus operator

Defined in the same way as Python's modulus (negative values behave
differently)

```equator
>>> -4 % 5
-4 % 5 => 1
>>> -3 % 5
-3 % 5 => 2
>>> -2 % 5
-2 % 5 => 3
>>> -1 % 5
-1 % 5 => 4
>>> 0 % 5
0 % 5 => 0
```

## `^` power operator

## `!` not operator

An operator to convert truthy values to falsy values and vice-versa.

```equator
>>> !true;
!true => false
>>> !false;
!false => true
```

## `||` boolean or operator

## `&&` boolean and operator

## `==` equality conditional

A conditional operator that checks whether two expressions are equal.

Expressions are considered to be equal if one can be simplified to the other.

## `!==` inequality conditional

A conditional operator that checks whether two expressions are unequal.

## `>` greater than conditional

## `>=` greater than or equal to conditional

## `<` less than conditional

## `<=` less than or equal to conditional
