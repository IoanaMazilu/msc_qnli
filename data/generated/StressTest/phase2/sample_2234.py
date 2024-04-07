# Premise: Jancy had 100 currency notes in all, some of which are of Rs 70 denomination and the remaining of Rs 50 denomination.
# Hypothesis: Jancy had less than 100 currency notes in all, some of which are of Rs 70 denomination and the remaining of Rs 50 denomination.
# Golden Label: contradiction

total_notes_premise = 100
total_notes_hypothesis = 100

# the hypothesis refers to the total number of notes that Jancy had, which is also mentioned in the premise
if total_notes_hypothesis >= total_notes_premise:
    # check if the hypothesis that Jancy had less than 'total_notes_hypothesis' contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
