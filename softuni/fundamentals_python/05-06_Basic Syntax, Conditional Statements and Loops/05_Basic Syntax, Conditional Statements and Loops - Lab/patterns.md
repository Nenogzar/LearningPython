# Star Pattern Programs In Python
1. Write a python program to print following star pattern: 

        *      *      *      *      *

        *      *      *      *      *

        *      *      *      *      *

        *      *      *      *      *

        *      *      *      *      *
Code:

    n=5
    for i in range(n):
        for j in range(n):
            print('*', end=' ')
        print()

2. Write a python program to print following pattern: 
        
        *
        *      *      
        *      *      *   
        *      *      *      *    
        *      *      *      *      *

Code:

    n = 5 
    for i in range(n): 
       for j in range(i+1): 
          print('*', end=' ')
       print()

3. Write a python code to print following star pattern: 

        *      *      *      *      *
        *      *      *      *
        *      *      *   
        *      *  
        *

Code:    

    n = 5 
    for i in range(n): 
       for j in range(i, n): 
          print('*', end=' ')
       print()

4. Write a python code to print following pattern: 

                        *
                    *   *
                *   *   *
            *   *   *   *
        *   *   *   *   *

Code:

    n = 5 
    for i in range(n): 
      for j in range(i, n): 
         print(' ', end=' ') 
      for j in range(i+1):
         print('*', end=' ')
      print()

5. Write a python program to print following star pattern: 

        *   *   *   *   *
            *   *   *   *
                *   *   *
                    *   *
                        *
Code:

        n = 5 
        for i in range(n): 
           for j in range(i+1): 
              print(' ', end=' ') 
           for j in range(i, n):
              print('*', end=' ')
           print()



6. Write a python program to print following hill star pattern: 


                    *
                *   *   *
            *   *   *   *   *
        *   *   *   *   *   *   *
    *   *   *   *   *   *   *   *   *

Code:

        n = 5 
        for i in range(n): 
           for j in range(i, n): 
              print(' ', end=' ') 
           for j in range(i):
              print('*', end=' ')
           for j in range(i+1):
              print('*', end=' ')
           print()


7. Write a python program to print revers hill star pattern: 


    *   *   *   *   *   *   *   *   *
        *   *   *   *   *   *   *   
            *   *   *   *   * 
                *   *   *
                    *
Code:

        n = 5 
        for i in range(n): 
           for j in range(i+1): 
              print(' ', end=' ') 
           for j in range(i, n-1):
              print('*', end=' ')
           for j in range(i, n):
              print('*', end=' ')
           print()

8. Write a python code to print Dimond pattern with star: 


                    *
                *   *   *
            *   *   *   *   *
        *   *   *   *   *   *   *
    *   *   *   *   *   *   *   *   *
        *   *   *   *   *   *   *   
            *   *   *   *   * 
                *   *   *
                    *



Code:

    n = 5 
    for i in range(n-1): 
       for j in range(i, n): 
          print(' ', end=' ') 
       for j in range(i):
          print('*', end=' ')
       for j in range(i+1): 
          print('*', end=' ')
       print() 
    for i in range(n): 
       for j in range(i+1): 
          print(' ', end=' ') 
       for j in range(i, n-1):
          print('*', end=' ')
       for j in range(i, n):
          print('*', end=' ')
       print()

9. 


