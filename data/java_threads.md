### Platform Threads

Managed by the OS.
Drawbacks: expensive to create, limited in number, block CPU resources (I/O or during Thread.sleep)

How to create platform Threads:

***Implementing the Runnable interface***

```java
class Task implements Runnable {
    @Override
    public void run() {
        System.out.println("Task is running");
    }
}

// Using the Thread
public class RunnableExample {
    public static void main(String[] args) {
        Thread thread = new Thread(new Task());
        thread.start();
    }
}
```

***Extending the Thread class***

```java
class Task extends Thread {
    @Override
    public void run() {
        System.out.println("Task is running");
    }
}


// Using the Thread
public class ThreadExample {
    public static void main(String[] args) {
        Task task = new Task();
        task.start();
    }
}
```

***Lambra expressions***

```java
public class LambdaExample {
    public static void main(String[] args) {
        Thread thread = new Thread(() -> System.out.println("Task is running"));
        thread.start();
    }
}
```

### Virtual Threads

Since Java21. Managed by the Virtual Machine. 
They provide massive scalability and simplified concurrency.


Basic sintax:
```java
Thread virtualThread = Thread.ofVirtual().start(() -> {
    // Code to be executed by the virtual thread
});
```


Example: Simple Web Server

```java
import java.net.ServerSocket;
import java.net.Socket;
public class VirtualThreadServer {
    public static void main(String[] args) throws Exception {
        try (ServerSocket server = new ServerSocket(8080)) {
            while (true) {
                Socket client = server.accept();
                Thread.ofVirtual().start(() -> handleClient(client));
            }
        }
    }
    private static void handleClient(Socket client) {
        try (client) {
            client.getOutputStream().write("Hello, Virtual Threads!".getBytes());
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```