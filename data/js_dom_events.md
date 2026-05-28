## DOM Events

A) Level 0 event

```js
let btn1 = document.getElementById("button1");
let count1 = 0;

// define event handler
let handler1 = (event) => {
    document.getElementById('span1').innerHTML = (++count1);
    //show event object
    console.log(event);
}

// bind event handler with btn1
btn1.onclick = handler1;
```

B) Level 2 event

```js
let btn2 = document.getElementById("button2");
let count2 = 0;

// event handler
let handler2 = (event) => {
    document.getElementById('span2').innerHTML = (++count2);
    //show event object
    console.log(event);
}

// register event handler with btn2
btn2.addEventListener("click", handler2, false);
```

Programmatically dispatch an event

```js
let btn4 = document.getElementById("button4");
let btn5 = document.getElementById("button5");
let count4 = 0

// register event handler with btn4
btn4.addEventListener('click', () => { 
    // button 4 sends a click event to button 5
    const event = new Event('click')
    btn5.dispatchEvent(event)
    console.log('event dispatched')
})

// btn5 event handler
btn5.onclick = (event) => {
    document.getElementById('span4').innerHTML = (++count4);
}
```

C) Level 3 event

```js
let btn3 = document.getElementById("button3");
let span3 = document.getElementById("span3");
let count3 = 0;

// btn3 event handler
btn3.onclick = () => {
    // create a custom event
    let event = new CustomEvent('send', { detail: { message: 'custom event message'}} );
    // send event to span3
    span3.dispatchEvent(event);
}

// define event handler
let handler3 = (event) => {
    if(event.type == 'send') {
        count3++;
        event.target.innerHTML = count3;
        console.log(event.detail.message);
    }
}

// register span3 event handler
span3.addEventListener('send', handler3);
```