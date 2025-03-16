## Task 1. Comparison of randomized and deterministic QuickSort

>   Implement the randomized and deterministic QuickSort algorithms. Perform a comparative analysis of their performance by measuring the average execution time on arrays of different sizes.

#### Specifications:

1. To implement the randomized QuickSort algorithm, implement the randomized_quick_sort(arr) function, where the pivot is randomly selected.

2. To implement the deterministic QuickSort algorithm, implement the deterministic_quick_sort(arr) function, where the pivot is selected according to a fixed rule: the first, last, or middle element.

3. Create a set of test arrays of different sizes: 10_000, 50_000, 100_000, and 500_000 elements. Fill the arrays with random integers.

4. Measure the execution time of both algorithms on each array. For a more accurate estimate, repeat the sorting of each array 5 times and calculate the average execution time.

## Task 2. Creating a class schedule using a greedy algorithm

>   Implement a program to schedule classes at a university using a greedy algorithm for the set covering problem. The goal is to assign teachers to subjects in a way that minimizes the number of teachers and covers all subjects.

#### Specifications:

1.  Implement the Teacher class with the following attributes:
        
        first_name    
        last_name (last name)
        age (age)
        email (email)
        can_teach_subjects (set of subjects that can be taught)
2.  Implement the create_schedule(subjects, teachers) function that uses a greedy algorithm to assign teachers to subjects. The function should return a list of teachers and the subjects they are assigned to.
3.  When selecting a teacher at each stage, give preference to the one who can teach the largest number of subjects that are not yet covered. If there are several such candidates, choose the youngest in terms of age.