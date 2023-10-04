# Operator syntax

## `:=` assignment operator

Bind an expression, condition or equation to a variable.

```equator
a := 1
```

## `,` join operator

Connect expressions and equations so that they are evaluated simultaneously.

```equator
>>> x + 2 * y = 10, 2 * x = y
x = 2
y = 4
```

## `|` pipe operator

Capture outputs from a statement to variables.

```equator
>>> // Capture values of x and y
>>> x + 2 * y = 10, 2 * x = y | x, y
>>> x
x = 2
```

## `->` map operator

Used alongside the pipe operator to rename variables when capturing them as
variables or unknowns.

```equator
>>> // Capture values of x and y
>>> x + 5 = 7 | x -> a
>>> a
a = 2
```

## `&` Join operator

Join captured outputs from a statement to unknowns in the next statement. Used
in conjunction with the pipe operator

```equator
>>> // Use x and y in next function call, but rename y to a
>>> x + 2 * y = 10, 2 * x = y | x, y -> a & x + a
6
```

## `=` equality operator

The equality operator is used to signify that two sides of an equation are
equal.

```equator
>>> x + 3 = 5
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

## `+` addition operator

## `-` subtraction operator

## `*` multiplication operator

## `/` division operator

## `%` modulus operator

## `^` power operator

## `==` equality conditional

## ``
