students_start_premise = 10.0
students_left_premise = 4.0
students_new_premise = 42.0
students_end_hypothesis = 50.0

# the hypothesis talks about the number of students at the end of the year, which is also referenced in the premise
# find the total number of students in the premise 
total_students_premise = students_start_premise + students_left_premise + students_new_premise
if students_end_hypothesis!= total_students_premise:
    # check if the total students from the hypothesis contradict the estimate of more than'students_left_premise'
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"
    
print(label)
