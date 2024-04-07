# Premise: When m divided by less than 588, the remainder is 47.
# Hypothesis: When m divided by 288, the remainder is 47.
# Golden Label: neutral

divisor_premise = 588
divisor_hypothesis = 288
remainder_premise = 47
remainder_hypothesis = 47

# the hypothesis talks about 'm' being divided by a certain number and the resulting remainder, same as the premise
if divisor_hypothesis >= divisor_premise:
    # check if the divisor in the hypothesis contradicts the premise's estimate of less than 'divisor_premise'
    label = "contradiction"
elif remainder_hypothesis != remainder_premise:
    # check if the remainder in the hypothesis contradicts the remainder in the premise
    label = "contradiction"
else:
    # the premise only gives an upper limit for the divisor and the same remainder as the hypothesis
    # any divisor less than 'divisor_premise' and the same remainder is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

