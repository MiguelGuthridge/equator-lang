# Structure syntax

Syntax of complex structures

## Equation

### Equation definition syntax

All variables not declared as part of the interface are considered to be local,
and are not shared outside the scope of the function.

```equator
equation my_equation ($x, $y, $z) {
    $z := a / b,
    a = 10 * $y,
    b = $x - 10;
}
```

Note that all interface variables are marked with a `$`.

### Equation literal syntax

All unknowns are published for calling code.

```equator
$my_eq := some_value = 10 * other_value + 2
```

This is equivalent to

```equator
equation my_eq ($some_value, $other_value) {
    $some_value = 10 * $other_value + 2
}
```

## Function

Functions are like equations, but unknowns are categorised as parameters and
returns. Like equations, values are published for calling code if they are
specified in the function interface.

```equator
// div_mod must be a function as the modulus is not reversible
function div_mod ($a, $b) -> ($div, $mod) {
    $div = $a / $b;
    $mod = $a % $b;
}
```

### Function calls

Function calls are similar to equation substitutions:

```equator
>>> $div_mod, a = 14, b = 3;
div => 4
mod => 2
```

## Expression

Examples of expressions are:

```equator
x + 2
sin(x)
```

### Condition

Conditions are a subset of expressions which can be evaluated to a value of
`Boolean` type.

Examples of conditions are:

```equator
x + 2 == 10
y > 6
```
