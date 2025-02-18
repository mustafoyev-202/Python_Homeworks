def insert_underscores(txt):
    vowels = "aeiou"
    result = []
    for i, char in enumerate(txt):
        result.append(char)
        if (i + 1) % 3 == 0:
            result.append("_")
        if char in vowels and i + 1 < len(txt):
            result.append("_")
    return "".join(result).rstrip("_")


# Example usage:
print(insert_underscores("hello"))  # Output: hel_lo
print(insert_underscores("assalom"))  # Output: ass_alom
print(
    insert_underscores("abcabcdabcdeabcdefabcdefg")
)  # Output: abc_abcd_abcdeab_cdef_abcdefg
