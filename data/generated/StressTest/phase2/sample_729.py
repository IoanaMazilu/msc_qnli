# Premise: Jeff has 252 ounces of peanut butter in 16, 28.
# Hypothesis: Jeff has more than 152 ounces of peanut butter in 16, 28.
# Golden Label: entailment

pb_quantity_premise = 252
pb_quantity_hypothesis = 152

# the hypothesis refers to the quantity of peanut butter possessed by Jeff, also mentioned in the premise
if pb_quantity_premise <= pb_quantity_hypothesis:
    # check if the estimate 'pb_quantity_hypothesis' contradicts the quantity of peanut butter in the premise
    label = "contradiction"
else:
    # if the quantity of peanut butter in the hypothesis does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)

