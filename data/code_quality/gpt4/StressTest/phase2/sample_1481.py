total_notes_premise = 90
total_notes_hypothesis = 90

# the hypothesis refers to the total number of currency notes that Julie had, also mentioned in the premise
if total_notes_hypothesis > total_notes_premise:
    # check if the hypothesis value contradicts the exact number of total notes in the premise
    label = "contradiction"
else:
    # since the hypothesis and the premise mention the same number of total notes, we can infer entailment
    label = "entailment"

print(label)
