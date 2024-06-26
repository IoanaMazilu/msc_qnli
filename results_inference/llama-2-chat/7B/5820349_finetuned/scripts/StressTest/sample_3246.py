students_premise = 90
students_hypothesis = 50

# the hypothesis refers to the number of students representing x percent of the boys at Jones Elementary School mentioned in the premise
if students_hypothesis >= students_premise:
    # check if the hypothesis value contradicts the exact number of students in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
