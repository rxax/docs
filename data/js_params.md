## QueryParams helper class

Used to get the query parameters:

```javascript
const QueryParams = (url) => {

    const params = []
    // init params
    const queryParams = new URLSearchParams(url || window.location.search)
    for (const [key, value] of queryParams) {
        params.push({[key]: value})
    }

    const getParamUniqueKeys = () => {
        // get the unique keys from param
        const obj = {}
        try {
            const keys = getParamKeys()
            keys.map(item => obj[item] = item)
        } catch (ex) {
        }
        return Object.keys(obj)
    }

    const getParamKeys = () => {
        // get the keys from param (can contain duplicates)
        const obj = []
        try {
            params.map(item => Object.entries(item)[0][0]).forEach(item => obj.push(item))
        } catch (ex) {
        }
        return obj
    }

    const values = () => {
        try {
            return params.map(item => Object.entries(item)[0][1])
        } catch (ex) {
        }
        return []
    }

    const getParamValuesByKey = (key) => {
        // get the values from params by key
        try {
            return params.filter(item => key in item).map(item => Object.entries(item)[0][1])
        } catch (ex) {
            return []
        }
    }

    const getParamValueByKey = (key) => {
        // get the first value from params by key
        try {
            return getParamValuesByKey(key)[0]
        } catch (ex) {
            return null
        }
    }

    const get = (id) => {
        // get param value by id
        return getParamValueByKey(id)
    }

    const getAll = (id) => {
        //get all param values by id
        return getParamValuesByKey(id)
    }

    const contains = (id) => {
        // check if param in params
        return getParamUniqueKeys().filter(item => item === id)
    }

    const keys = () => {
        //  get all keys
        return getParamUniqueKeys()
    }

    const items = () => {
        // transform the params in to key=value pairs ([ {key:key, value:value}, ...])
        return params.map(item=>{
            const [key,value] = Object.entries(item)[0]
            return {key: key, value: value}
        })
    }

    // attach functions
    return {
        getParamValueByKey,
        getParamValuesByKey,
        getParamKeys,
        getParamUniqueKeys,
        get,
        getAll,
        contains,
        keys,
        values,
        items
    }
}


export default QueryParams
```

Usage example:

```javascript
const params = QueryParams()

'all params '+params.items().map((item) => item.key + '=' + item.value+' ')

'all values for a key id: '+JSON.stringify(params.getAll('id'))

'one value for a key id: '+JSON.stringify(params.get('id'))

'all keys: '+JSON.stringify(params.getParamKeys())
        
'all unique keys: '+JSON.stringify(params.keys())
```