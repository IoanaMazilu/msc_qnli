marks_premise = [56, 60, 72, 85, 80]
marks_hypothesis = 26

# the hypothesis refers to the marks obtained by a student in various subjects, mentioned in the premise
if marks_premise[0] <= marks_hypothesis:
    # check if the 'marks_hypothesis' contradicts the first mark in the list of marks in the premise
    label = "contradiction"
else:
    # if the 'marks_hypothesis' is less than the first mark in the list of marks in the premise, we can infer entailment
    label = "entailment"

print(label)
