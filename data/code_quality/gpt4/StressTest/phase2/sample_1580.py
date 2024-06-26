students_premise = 100
grades_higher_angela_premise = 19
students_hypothesis = 800
grades_higher_angela_hypothesis = 19

# the hypothesis refers to the same number of grades higher than Angela’s mentioned in the premise, but in a different class size
if students_premise != students_hypothesis:
    # check if the number of students in the hypothesis contradicts the number of students in the premise
    label = "contradiction"
elif grades_higher_angela_hypothesis != grades_higher_angela_premise:
    # check if the number of grades higher than Angela’s in the hypothesis contradicts the number in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
