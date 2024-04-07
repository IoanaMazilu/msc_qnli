# Premise: If Donald carries a total of 30 notes (of either $10 or € 10,) then what is the total number of notes (of either $10 or € 10,) they take?
# Hypothesis: If Donald carries a total of 20 notes (of either $10 or € 10,) then what is the total number of notes (of either $10 or € 10,) they take?
# Golden Label: contradiction

notes_carried_premise = 30
notes_carried_hypothesis = 20

# the hypothesis refers to the number of notes carried by Donald mentioned in the premise
if notes_carried_hypothesis != notes_carried_premise:
    # check if the number of notes in the hypothesis contradicts the number of notes reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

