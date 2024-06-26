payment_premise = 128
payment_hypothesis = 328

# the hypothesis refers to the amount John needs to pay, which is also mentioned in the premise
if payment_hypothesis == payment_premise:
    # check if the amount John needs to pay in the hypothesis contradicts the amount in the premise
    label = "entailment"
else:
    # the amount John needs to pay in the hypothesis is different from the premise
    # without knowing the denomination of the bills, we cannot infer how many bills John will need to use
    label = "contradiction"

print(label)
