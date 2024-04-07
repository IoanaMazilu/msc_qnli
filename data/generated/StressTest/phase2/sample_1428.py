# Premise: When m divided by 288, the remainder is 47.
# Hypothesis: When m divided by less than 588, the remainder is 47.
# Golden Label: entailment

divisor_premise = 288
remainder_premise = 47
divisor_hypothesis = 588
remainder_hypothesis = 47

# the hypothesis refers to the divisor and remainder figure for 'm' mentioned in the premise
if divisor_hypothesis <= divisor_premise:
    # check if the divisor in the hypothesis contradicts the divisor in the premise
    label = "contradiction"
elif remainder_hypothesis != remainder_premise:
    # check if the remainder in the hypothesis contradicts the remainder in the premise
    label = "contradiction"
else:
    # the premise gives only a specific divisor and remainder for 'm'
    # any divisor less than 'divisor_hypothesis' with same remainder is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

