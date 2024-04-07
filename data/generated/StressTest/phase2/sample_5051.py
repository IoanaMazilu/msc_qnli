# Premise: Anitha had 80 currency notes in all, some of which are of Rs 95 denomination and the remaining of Rs 45 denomination.
# Hypothesis: Anitha had more than 80 currency notes in all, some of which are of Rs 95 denomination and the remaining of Rs 45 denomination.
# Golden Label: contradiction

total_notes_premise = 80
total_notes_hypothesis = 80

# the hypothesis refers to the total number of currency notes Anitha had, also mentioned in the premise
if total_notes_hypothesis > total_notes_premise:
    # check if the number of notes in the hypothesis contradicts the number of notes reported in the premise
    label = "contradiction"
else:
    # if the hypothesis does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)

