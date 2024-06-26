students_premise = 90
students_hypothesis = 50

# the hypothesis refers to the number of students representing x percent of the boys at Jones Elementary School, mentioned in the premise
if students_premise <= students_hypothesis:
    # check if the estimate of'students_hypothesis' contradicts the number of students in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
