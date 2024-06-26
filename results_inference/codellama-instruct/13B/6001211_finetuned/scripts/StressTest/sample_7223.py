students_premise = 200
students_hypothesis = 300
grades_higher_than_lena_premise = 24
grades_higher_than_lena_hypothesis = 24

# the hypothesis refers to the number of students and grades mentioned in the premise
if students_premise!= students_hypothesis:
    # check if the number of students in the hypothesis contradicts the number of students reported in the premise
    label = "contradiction"
elif grades_higher_than_lena_hypothesis!= grades_higher_than_lena_premise:
    # check if the number of grades higher than Lena's in the hypothesis contradicts the number of such grades reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
