payment_premise = 133
payment_hypothesis = 233

# the hypothesis refers to the amount Jadeja paid in the premise
if payment_premise != payment_hypothesis:
    # check if the amount in the hypothesis contradicts the amount in the premise
    label = "contradiction"
else:
    # the premise and hypothesis amounts are equal
    label = "entailment"

print(label)
