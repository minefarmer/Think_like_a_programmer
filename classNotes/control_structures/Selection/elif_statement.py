'''     Elif Statement
Elif statement is used to chose one block of statement from many blocks of statements.

It is used when there are many options and only one block of statements

    Test score | Grade
    >= 90       A
    >= 80       B
    >= 70       C
    >= 60       D
    Selow 60    R
    
                                   
                                                                Main
                                                                 |
                                                        False    |   True
                                                ____________test_score > 90________________
                                                |                                          |
                                   __False__Test score > 80_____True__          Output"grade A"
                                  |                                   |                   |
                         _False____Test score > 70_____True__         |                   |
                        |                                    |        |                   |    
         __False__Test score > 60 ___True__                  |     Output "Grade B"       |
        |                                  |                 |        |                   |
  Output"Grade F"                          |       Output "grade C"   |                   |
        |                             Output "Grade D        |        |                   |
        |                                  |                 |        |                   |
        |____________0_____________________|                 |        |                   |        
                     |________________0______________________|        |                   |
                                      |______________0________________|                   |
                                                     |                                    |
                                                     |__________________0_________________|
                                                                        |
                                                                       End


                                      
'''


test_score = int(input("Please enter the test score: "))
