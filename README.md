# Artistic-Gymnastics
 Python program that manages the scores of an artistic gymnastics competition.
Make the following assumptions:

The number of lines in the file is not known a priori
The Name and Surname fields do not contain spaces
The athlete's sex is encoded by an M or F character.
The country abbreviation is always coded on 3 capital letters
5 votes are always assigned for each athlete, separated by a space and the value may vary from a minimum of 0 to a maximum of 10.
The program must print:

The name of the female winner. When calculating the total points, the maximum and the maximum score must always be DISCARDED minimum among the 5 assigned. The final score is therefore given by the sum of the three remaining scores.
The ranking of the top 3 nations, including both female and male athletes. For each nation the total score is calculated by adding the scores of all its athletes (M and F, and always discarding the highest and lowest scores of each athlete).