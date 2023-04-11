# transgreek

Translate a greek-lettered wordlist to greeklish. May have some dups as some greek words that are written with different greek letters can produce the same greeklish output.

## usage

```bash
python3 transgreek.py input.txt output.txt
```

You can then remove the dups and sort it

```bash
sort -u output.txt > sorted.txt
```

You can then combine the generated lists with
[wordlister](https://github.com/servomekanism/wordlister) to create male and female
combined lists

Based on [this](https://stackoverflow.com/questions/59552782/how-to-convert-characters-from-greek-to-english-python) answer.
