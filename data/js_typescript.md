##Typescript

Basic Types

```ts
let name: string = "Alice";
let age: number = 30;
let active: boolean = true;
let data: any = "anything";

let id: string | number = 123; // Union type
```

Arrays

```ts
let nums: number[] = [1, 2, 3];

let names: Array<string> = ["Alice", "Bob"];
```

Tuples

```ts
let person: [string, number] = ["Alice", 30];
```

Enums

```ts
enum Status {
  Pending,
  Active,
  Completed
}

let current: Status = Status.Active;
```

Objects

```ts
let user: {
  name: string;
  age: number;
} = {
  name: "Alice",
  age: 30
};
```

Type Aliases

```ts
type User = {
  id: number;
  name: string;
};

const user: User = {
  id: 1,
  name: "Alice"
};
```

Interfaces

```ts
interface User {
  id: number;
  name: string;
}

const user: User = {
  id: 1,
  name: "Alice"
};
```

Interface extension

```ts
interface Person {
  name: string;
}

interface Employee extends Person {
  employeeId: number;
}
```

Function

```ts
function add(a: number, b: number): number {
  return a + b;
}

const multiply = (a: number, b: number): number => a * b;
```

Optional parameters

```ts
function greet(name: string, title?: string) {
  return title ? `${title} ${name}` : name;
}
```

Default paramters

```ts
function greet(name: string, title = "Mr.") {
  return `${title} ${name}`;
}
```

Classes

```ts
class User {
  constructor(
    public name: string,
    private password: string
  ) {}

  login() {
    console.log(`${this.name} logged in`);
  }
}
```

Access modifiers

```ts
class Example {
  public a = 1;
  protected b = 2;
  private c = 3;
}
```

Generics

```ts
function identity<T>(value: T): T {
  return value;
}

const result = identity<string>("hello");
```

Generic Interfaces

```ts
interface ApiResponse<T> {
  data: T;
  success: boolean;
}
```

Type Assertions

```ts
const input = document.getElementById("name") as HTMLInputElement;

const value = (<HTMLInputElement>input).value;
```

Literal types

```ts
type Direction = "up" | "down" | "left" | "right";

let move: Direction = "up";
```

Optional properties

```ts
interface User {
  id: number;
  name?: string;
}
```

Readonly properties

```ts
interface User {
  readonly id: number;
  name: string;
}
```

###Utility types

***Partial***

```ts
interface User {
  id: number;
  name: string;
}

type UserUpdate = Partial<User>;
```

***Pick***

```ts
type UserPreview = Pick<User, "id" | "name">;
```

***Omit***

```ts
type UserWithoutId = Omit<User, "id">;
```

***Record***

```ts
type Scores = Record<string, number>;

const scores: Scores = {
  alice: 95,
  bob: 88
};
```

***Async/Await***

```ts
async function fetchUser(id: number): Promise<User> {
  const response = await fetch(`/users/${id}`);
  return response.json();
}
```

***Type Guards***

```ts
function printId(id: string | number) {
  if (typeof id === "string") {
    console.log(id.toUpperCase());
  } else {
    console.log(id.toFixed());
  }
}
```

***Null safety***

```ts
let value: string | null = null;

value?.toUpperCase(); // Optional chaining

const result = value ?? "default"; // Nullish coalescing
```

###Modules

Export

```ts
export function add(a: number, b: number) {
  return a + b;
}

export default class User {}
```

Import

```ts
import User from "./User";
import { add } from "./math";
```

###Common Patterns

Discriminated Union

```ts
type Success = {
  status: "success";
  data: string;
};

type Error = {
  status: "error";
  message: string;
};

type Result = Success | Error;

function handle(result: Result) {
  if (result.status === "success") {
    console.log(result.data);
  } else {
    console.log(result.message);
  }
}
```

Generic API Response

```ts
type ApiResponse<T> = {
  success: boolean;
  data: T;
  error?: string;
};
```

Useful Compiler Flags

```json
{
  "compilerOptions": {
    "strict": true,
    "noImplicitAny": true,
    "strictNullChecks": true,
    "target": "ES2022",
    "module": "NodeNext"
  }
}
```

Most Common Syntax

```ts
type User = {
  id: number;
  name: string;
};

async function getUser(id: number): Promise<User> {
  return { id, name: "Alice" };
}

const user = await getUser(1);
console.log(user.name);
```