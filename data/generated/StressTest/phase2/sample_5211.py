# Premise: 90 students represent x percent of the boys at Jones Elementary School.
# Hypothesis: more than 30 students represent x percent of the boys at Jones Elementary School.
# Golden Label: entailment

students_premise = 90
students_hypothesis = 30

# the hypothesis refers to the number of students representing x percent of the boys at the school, also mentioned in the premise
if students_premise <= students_hypothesis:
    # check if the 'students_premise' contradicts the estimate of more than 'students_hypothesis'
    label = "contradiction"
else:
    # if the hypothesis number of students does not contradict the premise number of students, we can infer entailment
    label = "entailment"

print(label)

