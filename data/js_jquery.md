## JQuery

Get a Dom object

```js
$variable = $('selector')
```

Access the current elements native api

```js
$('selector').each(function(key, el) { 
   /* `this`, or jquery api with $(el)/$(this) */ 
});
```


DOM ready v3:

```js
jQuery(function($) {
	// code
});
```

Attach named listeners

```js
$(document).on("click.mymodule", function() {
    console.log("Document Clicked 1")
});
```

Detach named listeners

```js
$(document).off("click.mymodule");
```