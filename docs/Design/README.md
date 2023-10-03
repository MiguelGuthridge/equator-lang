# Design

Equator takes a new approach to programming, structured around the idea of
equations. Like a function, equations can be given various inputs, and produce
outputs. However, unlike functions, there is no clearly-defined input -
instead, the interpreter is given a number of inputs, and uses those values to
solve for the remaining unknowns.

For example, here is a simple equation of a line.

```equator
>>> line := y = m * x + b
```

To some extent, this is similar to the following Python function.

```py
>>> def line(m, x, b):
...    return m * x + b
```

The real difference arises when using equations, compared to functions.

```equator
>>> line, m = 10, x = 4, b = 2
y = 42
m = 10
x = 4
b = 2
```

```py
>>> line(10, 4, 2)
42
```

Unlike Python, any (or none) of the variables can be specified - the
interpreter will solve for the remaining variables as required.

```equator
>>> line, y = 42, x = 4, b = 2
m = 10
y = 4
x = 4
b = 2
```

```equator
>>> line, m = 2, b = 4
y = 2 * x + 4
x = (y - 4) / 2
m = 2
b = 4
```

Observe that if not all required variables are given, the equation is still
solved to the greatest extent possible. It is possible to bind the resulting
simultaneous equations to a variable to use them in future expressions.

```equator
>>> my_line := line, m = 2, b = 4
>>> my_line, x = 3
y = 10
x = 3
m = 2
b = 4
```
