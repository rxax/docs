# Builder pattern

Builder Pattern is a unique design pattern which helps in building complex object using simple objects and uses an algorithmic approach. This design pattern comes under the category of creational pattern.

```python
class HtmlBuilder:
    _html = ''

    def with_paragrah(self, text: str):
        self._html += f"<p>{text}</p>"
        return self

    def with_image(self, url: str):
        self._html += f"<img src='{url}'/>"
        return self

    def build(self):
        return self._html
```

Example usage:

```python
builder = HtmlBuilder()
html = builder.with_image("Image_created_with_a_mobile_phone.png") \
    .with_paragrah("This is an example") \
    .build()
print(html)
```
Output:

> `<img src='Image_created_with_a_mobile_phone.png'/><p>This is an example</p>`