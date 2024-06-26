average_mark_premise = 46 + 75 + 72 + 63 + 65
average_mark_hypothesis = 86 + 75 + 72 + 63 + 65

# the hypothesis refers to the same scores as in the premise
if average_mark_hypothesis!= average_mark_premise:
    # check if the average mark in the hypothesis contradicts the average mark in the premise
    label = "contradiction"
else:
    # if the average marks in the hypothesis and premise are the same, it is entailment
    label = "entailment"

print(label)
