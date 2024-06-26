students_premise = 100
students_hypothesis = 600
grades_higher_than_angela_premise = 19
grades_higher_than_angela_hypothesis = 19

# the hypothesis talks about the number of students in a class and the number of grades higher than Angela's, both referenced in the premise
if students_hypothesis < students_premise:
    # check if the hypothesis value contradicts the number of students in the premise
    label = "contradiction"
elif grades_higher_than_angela_hypothesis != grades_higher_than_angela_premise:
    # check if the number of grades higher than Angela's in the hypothesis contradicts the number of such grades reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
