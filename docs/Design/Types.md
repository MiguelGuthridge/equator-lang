# Data types

## `Type`

A meta-type.

## `Number`

Equator does not distinguish between floats and integers. All numbers are
treated the same.

## `Boolean`

True of false. Similar to boolean types in other languages.

## `String`

Strings are similar to other high-level languages, but aren't the primary
focus of the language. I doubt I'll do much with them aside from printing
content.

## `Equation`

Equations are the core of Equator's logic. They are like a function with a
clearly-defined inverse, meaning that they can be reversed.

An equation needs to have at least one input and one output, as it is
impossible to get the inverse of an equation that doesn't accept this.

Note that functions cannot be used in an equation definition, as they cannot
be inversed, and therefore would prevent the equation from being solvable,
except in one direction.

## `Function`

Functions are similar to functions in other languages. Unlike equations, they
do not have an inverse, and therefore cannot be used as part of an equation.
This is because rather than specifying unknowns, their unknowns are sorted into
parameters and returns.

### Converting functions to equations

A collection of functions can be converted to an equation, provided that if the
equation has $n$ unknowns, each function accepts $n - 1$ parameters and returns
the one remaining unknown.

## `Expression`

Expressions don't define equality, and therefore can only be evaluated. They
can still be stored as variables, but when evaluated with equations, they will
only get the values derived from the equations substituted.

## `Condition`

Conditions measure properties of expressions and equations.
