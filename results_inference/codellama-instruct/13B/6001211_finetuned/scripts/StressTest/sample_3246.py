students_premise = 90
students_hypothesis = 50

# the hypothesis refers to the number of students representing 'x percent' of the boys at the same school mentioned in the premise
if students_premise <= students_hypothesis:
    # check if the number of students in the hypothesis contradicts the number of students reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
