students_premise = 90
students_hypothesis = 70

# the hypothesis talks about the representation of x percent of boys at Jones Elementary School, referenced also in the premise
if students_premise != students_hypothesis:
    # check if the number of students in the hypothesis contradicts the number of students reported in the premise
    label = "contradiction"
else:
    # if the number of students in the hypothesis does not contradict the number of students reported in the premise, we can infer entailment
    label = "entailment"

print(label)
