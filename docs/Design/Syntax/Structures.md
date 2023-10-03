# Structure syntax

Syntax of complex structures

## Equation

### Equation definition syntax

All variables not declared as part of the interface are considered to be local,
and are not shared outside the scope of the function.

```equator
equation my_equation (x, y, z) {
    a = 10 * y
    b = x - 10
    z = a / b
}
```

### Equation literal syntax

All unknowns are published for calling code.

```equator
some_value = 10 * other_value + 2
```

## Function

Functions are like equations, but unknowns are categorised as parameters and
returns. Like equations, values are published for calling code if they are
specified in the function interface.

```equator
function div_mod (a, b) -> (div, mod) {
    div = a / b
    mod = a % b
}
```

## Expression

Examples of expressions are:

```equator
x + 2
sin(x)
```

## Condition

Examples of conditions are:

```equator
x + 2 == 10
y > 6
```
