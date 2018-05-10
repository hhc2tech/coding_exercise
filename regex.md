Regular expression 
|           |                                                    |                                                          |
|-----------|----------------------------------------------------|----------------------------------------------------------|
| `.`       | any                                                |                                                          |
| `^`       | start                                              |                                                          |
| `$`       | end                                                |                                                          |
| `*`       | 0 or more                                          |                                                          |
| `+`       | 1 or more                                          |                                                          |
| `?`       | 0 or 1                                             | 'ab?' will match 'a' or 'ab'                             |
| `{m}`     | `m` copies of the previous RE                      |                                                          |
| `{m, n}`  | from `m` to `n`                                    | 'a{4,}b' will match at least for `a` followed by one `b` |
| `{m, n}?` | minimum possible                                   |                                                          |
| `\`       | escapes                                            |                                                          |
|           | special char or signals special                    |                                                          |
| `[]`      | a set of chars                                     |                                                          |
| `[a-z]`   | any from `a` to `z`                                |                                                          |
|           | `[0-5][0-9]` any two-char number from `00` to `59` |                                                          |
|           | `[0-9A-Fa-f]` any hexadecimal digit                |                                                          |
|           | `[a\-z]` match `a`, `-`, or `z`                    |                                                          |
|           | special chars lose their meanings inside sets      |                                                          |
|           | `[^...]` NOT in the set                            |                                                          |
| `(...)`   |                                                    |                                                          |