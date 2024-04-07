# Premise: Jancy had 100 currency notes in all, some of which are of Rs 70 denomination and the remaining of Rs 50 denomination.
# Hypothesis: Jancy had less than 200 currency notes in all, some of which are of Rs 70 denomination and the remaining of Rs 50 denomination.
# Golden Label: entailment

total_notes_premise = 100
total_notes_hypothesis = 200

# the hypothesis refers to the total number of currency notes mentioned in the premise
if total_notes_hypothesis <= total_notes_premise:
    # check if the estimate of 'total_notes_hypothesis' contradicts the number of total currency notes in the premise
    label = "contradiction"
elif total_notes_hypothesis > total_notes_premise:
    # check if the number of total currency notes in the hypothesis contradicts the number of total currency notes reported in the premise
    label = "neutral"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
