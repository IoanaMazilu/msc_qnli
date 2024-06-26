total_notes_premise = 90
total_notes_hypothesis = 40

# the hypothesis refers to the total number of notes Julie had, which is also mentioned in the premise
if total_notes_hypothesis >= total_notes_premise:
    # check if the estimate of 'total_notes_hypothesis' contradicts the total number of notes in the premise
    label = "contradiction"
elif total_notes_hypothesis < total_notes_premise:
    # if the hypothesis value is less than the total number of notes in the premise, it is entailed by the premise
    label = "entailment"

print(label)
