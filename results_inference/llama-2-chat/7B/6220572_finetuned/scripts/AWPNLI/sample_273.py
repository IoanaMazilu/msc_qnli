students_start_year_premise = 10.0
students_left_premise = 4.0
students_new_premise = 42.0
students_end_hypothesis = 50.0

# the hypothesis talks about the number of students at the end of the year, which is also referenced in the premise
# compute the total number of students at the end of the year from the premise
total_students_end_year_premise = students_start_year_premise + students_left_premise - students_new_premise
if total_students_end_year_hypothesis!= total_students_end_year_premise:
    # check if the number of students at the end of the year in the hypothesis contradicts the number of students from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
