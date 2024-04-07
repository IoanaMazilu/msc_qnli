# Premise: Anup was asked to find the value of 7/12 of a sum of money R.
# Hypothesis: Anup was asked to find the value of more than 6/12 of a sum of money R.
# Golden Label: entailment

value_premise = 7/12
value_hypothesis = 6/12

# the hypothesis refers to the fraction of money Anup is asked to find, also mentioned in the premise
if value_premise <= value_hypothesis:
    # check if the value in the premise contradicts the hypothesis of more than 'value_hypothesis'
    label = "contradiction"
else:
    # if the value in the premise is greater than the 'value_hypothesis', it implies that the statement is entailed
    label = "entailment"

print(label)

