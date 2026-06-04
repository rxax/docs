## Stream API

The DataSet for the examples

```java
    private List<Footballer> getFootballers() {
        return List.of(
                new Footballer("Messi", 32, Gender.MALE, List.of("CF","CAM", "RF")),
                new Footballer("Griezmann", 28, Gender.MALE, List.of("CF", "CAM", "LF")),
                new Footballer("Arthur", 23, Gender.MALE, List.of("CM", "CAM")),
                new Footballer("Ter Stegen", 27, Gender.MALE, List.of("GK")),
                new Footballer("Puig", 20, Gender.MALE, List.of("CM", "CDM")),
                new Footballer("Jennifer", 29, Gender.FEMALE, List.of("CF", "CAM")),
                new Footballer("Jana", 17, Gender.FEMALE, List.of("CB")),
                new Footballer("Alexia", 25, Gender.FEMALE, List.of("CAM", "RF", "LF"))
        );
    }

```

Filter dataset

```java
List<Footballer> collect = footballerList.stream()
                .filter(footballer -> footballer.getGender().equals(Gender.FEMALE))
                .filter(footballer -> footballer.getAge() > 23)
                .collect(Collectors.toList());
```

Map dataset

```java
long femalesMoreThan24y= footballerList.stream()
                .filter(footballer -> footballer.getGender().equals(Gender.FEMALE))
                .map(Footballer::getAge)
                .filter(age -> age > 24)
                .count();
```

Sort dataset

```java
        List<Footballer>  sortByGenderAndName= footballerList.stream()
                .sorted(Comparator.comparing(Footballer::getGender).thenComparing(Footballer::getName))
                .collect(Collectors.toList());
```

Take while

```java
        List<Integer> takeAWhile = Stream.of(2, 4, 6, 8, 9, 10, 11, 12)
                .takeWhile(n -> n % 2 == 0)
                .collect(Collectors.toList());

        System.out.println("takeAWhile = " + takeAWhile);
        //prints takeAWhile = [2, 4, 6, 8]
```

Drop while

```java
  List<Integer> dropWhile = Stream.of(2, 4, 6, 8, 9, 10, 11, 12)
                .dropWhile(n -> n % 2 == 0)
                .collect(Collectors.toList());

        System.out.println("dropWhile = " + dropWhile);
        //prints dropWhile = [9, 10, 11, 12]
```