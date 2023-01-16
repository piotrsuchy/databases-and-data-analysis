# LABORATORIUM NR 13:

Piotr Suchy 407332

# Pierwszy test - hello:

### **Faza RED:**
![Pierwszy test - fail](images/Fail_1.png)

### **FAZA GREEN:**
Treść testu:
![Pierwszy test](images/hello_test.png)

Wynik testu po napisaniu funkcji hello():
![Pierwszy test - green](images/hello_test_green.png)

### **FAZA REFACTOR:**
Ponieważ funkcja hello() jest bardzo prymitywna, faza refactor była zbędna w tym przypadku.


# Drugi test - Extract Sentiment:
### **Faza RED:**
![Drugi fail](images/Fail_2.png)

### **FAZA GREEN:**
Treść testu:
![Drugi test-1](images/sentiment_function.png)

Treść funkcji:
![Drugi test](images/sentiment_1.png)


Wynik testu po napisaniu funkcji extract_sentiment():
![Pierwszy test - green](images/sentiment_green.png)

### **FAZA REFACTOR:**
Refactoring:
Zmieniona treść testu:
![](images/sentiment_2.png)

Zmieniona treść funkcji:
![](images/sentiment_function2.png)

Wyniki po refactoringu:
![](images/sentiment_green2.png)


# Trzeci test - text function:

### **Faza RED:**
![](images/Fail_4.png)
![](images/Fail_5.png)

### **FAZA GREEN:**
Treść funkcji:
![](images/text_function.png)

Treść testu:
![](images/text_test.png)

Wynik testu po napisaniu funkcji:
![](images/text_green.png)

### **FAZA REFACTOR:**
Ponieważ funkcja text_contain_word() jest jednolinijkowa, nie ma przestrzeni do ulepszeń. Ale można dodać jeszcze jeden przypadek testu, aby mieć więcej pewności.

Treść funkcji testującej po refactorze:
![](images/text_refactor1.png)

Wynik testów po refactorze:

![](images/text_refactor2.png)


# Czwarty test - Przykład dla bubblesort'u:

### **Faza RED:**
Treść testu:

![](images/bubblesort_test.png)

Treść funkcji - póki co nie robi nic, oprócz zwrócenia parametru:

![](images/bubblesort_function.png)

I wynik testu dla funkcji, która nic nie robi (póki co) - jak widać test niezaliczony:
![](images/bubblesort_test_red.png)


### **Faza Green:**

Treść funkcji, która przechodzi test:

![](images/function_bubblesort.png)

Treść testu, przed refactoringiem:

![](images/test_bubblesort.png)

Wynik testu dla funkcji powyżej:

![](images/bubble_test_green.png)


### **Faza Refactor:**

Po dodaniu dodatkowych testów - edge casów:

![](images/refactor_b1.png)

I zmodyfikowaniu funkcji do rozpatrywania edge case'a + usunięcia zbędnego kodu:

![](images/refactor_b2.png)

Dostajemy wyniki:

![](images/refactor_b3.png)


## WNIOSKI:

TDD jest przydatnym sposobem tworzenia kodu, szczególnie w większych projektach. TDD sprawia, że kod, który stworzymy od razu spełnia wszystkie wymogi. Podejście to jest jednak dosyć powolne i w indywidualnych projektach nie jest wymagane.