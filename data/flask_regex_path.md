## Flask RegEx path converter

Convenience function to use RegEx expressions in app.route paths.

```python
class RegexConverter(BaseConverter):
    def __init__(self, url_map, *items):
        super(RegexConverter, self).__init__(url_map)
        self.regex = items[0]

# Register converter
app.url_map.converters['regex'] = RegexConverter
```

Usage:

```python
@app.route('/api/<regex("[a-zA-Z0-9]*"):appid>/test')
def test(appid):
    return Response(response="All Good", status=200)
```
