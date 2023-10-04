# Syntax examples

## Caesar cipher

```equator
$ASCII_UPPER_A := 65;
$ASCII_LOWER_A := 97;



// Apply caesar cipher to a single letter
equation caesar_char ($input, $output, $shift) {
    when is_ascii_letter, char = $input {
        // Get shift amount into a reasonable range
        $shift := $shift % 26;

        // Convert the char to an int
        char_to_int, char = $input | $int;

        // Uppercase and lowercase letters have a different base value
        when ($int > $ASCII_LOWER_A) {
            $char_base := $ASCII_LOWER_A;
        } else {
            $char_base := $ASCII_UPPER_A;
        }

        // Convert letter into a number (0 - 26)
        $in_num := $int - $char_base;

        // Shift the number
        $out_num := ($in_num + $shift) % 26;

        // Convert it back to a letter
        $output := char_to_int, int = $out_num + $char_base;
    } else {
        $output := input;
    }
}

// Apply a caesar cipher
equation caesar ($input, $output, $shift) {
    $output := [];
    // FIXME: How is this reversed? Do we need a `map` function?
    // That would require higher-order functions, which is yucky with the
    // current syntax
    over $char in $input {
        $caesar_char, input = $char, shift = $shift | output -> $shifted;
        $append, list = $output, value = $shifted | $output;
    }
}
```
