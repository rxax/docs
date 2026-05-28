## Text search

Using fuzzy_match

```python
from fuzzy_match import algorithims
```

Input, search text, acceptance score

```python
source = [
    'Bus stop 10, Route number 45, Pears Station',
    'Bus route 25, Stop 1100, Connolly Station',
    'The Grand Hotel',
    'Dartmouth Terrace, Stop 123'
]

search_text = 'bus stop 123'

acceptance_score = 0.25
```

Search through the data
```python
results = []

for item in source:
    # Get str similarity
    x = algorithims.trigram(item, search_text)
    #print(item, x)

    # Save to result
    if x >= acceptance_score:
        results.append({
            "score": x,
            "item": item
        })

#print(len(results), results)
```

Sort the results by score

```python
results.sort(key=lambda a: a['score'], reverse=True)
print(results)
```

Flatten the results (to get the items back as a list)

```python
results = [el['item'] for el in results]
print(results)
```

Output:

> ['Dartmouth Terrace, Stop 123']