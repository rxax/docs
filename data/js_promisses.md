## Promisses

Promisses (state machine) enables asynchronous processing: stateful object (pending, resolved/fulfilled, rejected)

```js
// 
// ---------------------------------------------------------
const t2 = document.getElementById("i2");
const b2 = document.getElementById("b2");
const o2 = document.getElementById("o2");


// add button event listener
b2.onclick = (event) => {
    // create promise with its executor function
    const p1 = new Promise((resolve, reject) => {

        setTimeout(() => {

            if (isNaN(i2.value)) {
                reject('Invalid number!');
            } else {
                resolve(i2.value)
            }

        }, 1000)

    })

    // define resolved handler
    const onResolved = (prop) => {
        o2.innerHTML = `You have entered ${prop}`
    }

    // define rejected handler
    const onfailed = (prop) => {
        o2.innerHTML = `Error: ${prop}`
    }

    // attach handlers to promise then(), catch(), finally()
    p1.then(onResolved, onfailed).finally(() => {
        console.log('The promise has been resolved')
    })


}

// resoved promise
const p = Promise.resolve(30).then(val => console.log(val));

// rejected promise
const p2 = Promise.reject(31).then(() => { /* this 'then' is not called due to the reject */ })
                .catch((val) => { 
                    /* this is called */
                    console.log(val)
                });
```