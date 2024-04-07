# Premise: If Donald carries a total of 39 notes (of either $10 or € 10,) then what is the total number of notes (of either $10 or € 10,) they take?
# Hypothesis: If Donald carries a total of less than 89 notes (of either $10 or € 10,) then what is the total number of notes (of either $10 or € 10,) they take?
# Golden Label: entailment

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

