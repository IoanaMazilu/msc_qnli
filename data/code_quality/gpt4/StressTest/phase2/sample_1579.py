students_premise = 600
students_hypothesis = 100
grades_higher_than_angela_premise = 19
grades_higher_than_angela_hypothesis = 19

# the hypothesis refers to the number of students and grades higher than Angela's mentioned in the premise
if students_hypothesis > students_premise:
    # check if the number of students in the hypothesis contradicts the estimated number of students in the premise
    label = "contradiction"
elif grades_higher_than_angela_hypothesis != grades_higher_than_angela_premise:
    # check if the number of grades higher than Angela's in the hypothesis contradicts the number of grades higher than Angela's reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
