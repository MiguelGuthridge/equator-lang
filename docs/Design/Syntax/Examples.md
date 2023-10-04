# Syntax examples

## Caesar cipher

```equator
$ASCII_A := 65;

// Apply caesar cipher to a single letter
equation caesar_char ($input, $output, $shift) {
    // Get shift amount into a reasonable range
    $shift := $shift % 26;

    // Convert letter into a number (0 - 26)
    $in_num := char_to_int, char = $input | $$ & int - $ASCII_A;

    // Shift the number
    $out_num := ($in_num + $shift) % 26;

    // Convert it back to a letter
    $output := char_to_int, int = $out_num + $ASCII_A;
}

equation caesar ($input, $output, $shift) {
    $output := [];
    over $char in $input {
        when is_ascii_letter, char = $char {
            $caesar_char, input = $char, shift = $shift | output -> $shifted;
            $append, list = $output, value = $shifted | $output;
        } else {
            $append, list = $output, value = $char | $output;
        }
    }
}
```
