average_marks_premise = 88
average_marks_hypothesis = 18

# the hypothesis refers to the difference in average marks mentioned in the premise
if average_marks_hypothesis >= average_marks_premise:
    # check if the 'average_marks_hypothesis' contradicts the premise of less than 'average_marks_premise'
    label = "contradiction"
else:
    # if the hypothesis does not contradict the premise, it can be inferred as an entailment
    label = "entailment"

print(label)
