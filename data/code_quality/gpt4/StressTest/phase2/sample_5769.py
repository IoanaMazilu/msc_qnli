notes_premise = 39
notes_hypothesis = 89

# the hypothesis refers to the number of notes mentioned in the premise
if notes_premise >= notes_hypothesis:
    # check if the estimate of 'notes_hypothesis' contradicts the number of notes in the premise
    label = "contradiction"
elif notes_premise < notes_hypothesis:
    # check if the number of notes in the hypothesis is greater than the number of notes reported in the premise
    label = "entailment"

print(label)
