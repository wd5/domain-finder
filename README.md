# Finder

A quick and dirty tool for finding available single word .io domains

![](https://raw.github.com/owainlewis/domain-finder/master/preview.png)

## Use

When you run the script it will search every word in a word file larger than 4 letters. 

If the domain is available it will save the result to available.txt

Because the word file is so large the second argument is a letter (i.e words starting with "b" etc)

Arguments are:

finder.py <path_to_dict> <letter_to_search> <max_word_length>

```python

python finder.py "/usr/share/dict/words" "b" 10

```