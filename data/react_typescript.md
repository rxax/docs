### TypeScript best practices for React

#### Define basic props

Define the shape of `props` object to ensure type safety.

```js
type BookProps = {
  name: string;
  author?: string; // Optional prop
};

function BookInfo({ name, author }: BookProps) {
  return (
    <div>
      <h2>{name}</h2>
      {author && <p>Author: {author}</p>}
    </div>
  );
}
```

#### Handling `children` props

React allows you to pass content to components via `children`.

```js
import { PropsWithChildren } from 'react';

type CourseProps = {
  courseName: string;
};

function CourseInfo({ courseName, children }: PropsWithChildren<CourseProps>) {
  return (
    <div>
      <h1>{courseName}</h1>
      {children}
    </div>
  );
}
```

[source](https://medium.com/@mkare/best-practices-for-using-typescript-with-react-bad13d851143)