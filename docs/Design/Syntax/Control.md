# Control flow syntax

## If-else

If-else statements require a condition. This condition is evaluated, and if it
is `true`, the if block is entered, and if it is `false`, the `else`
block is entered.

```equator
if x == 2 {
    print, value = "x is 2";
} else {
    print, value = "x is not 2";
}
```

### Interaction with `,` comma operator

When a comma operator is used in an if statement, the first element is
required to be a conditional, and all others are required to be an equation.
The conditional is evaluated simultaneously with the equations.

```equator
if x == 100, x = 10^2 {
    print, value = "x^2 is 100";
}
```

## When-else

One limitation of if-else statements is that they require the condition to be
fully evaluated, making them not work nicely with equations, as an inverse
cannot be created. To resolve this, Equator introduces when-else statements.

In the forwards direction, this works like an if statement. But in the reverse
direction, it creates two variations on the output.

```equator
// Implementation of an abs equation, which produces the absolute value of
// x
// This would be used as:
// abs, a = 2
// And would produce a list of results
// x = [ -2, 2 ]
equation abs (x, a) {
    when x > 0 {
        a = $x;
    } else {
        a = -x;
    }
}
```

## While loop

Behaves similarly to a while loop in conventional languages.

```equator
$x := 0;
while x < 10 {
    print, value = $x;
}
```

## Where loop?

`where` is to `while` as `when` is to `if`. My poor feeble brain cannot
comprehend how this would work currently, so it probably won't be included in
the language.

## For loop

Behaves like a Python for loop, iterating over an iterable.

```equator
abs, a = 3 | x;

for result in x {
    if result > 0 {
        print, value=["found the positive result", x];
    }
}
```
