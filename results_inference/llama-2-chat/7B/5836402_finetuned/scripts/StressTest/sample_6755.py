goes_before_premise = 8
goes_before_hypothesis = 8

# the hypothesis refers to the number of P Ana goes before, which is also mentioned in the premise
if goes_before_hypothesis >= goes_before_premise:
    # check if the hypothesis value contradicts the premise of Ana going before less than 'goes_before_premise'
    label = "contradiction"
else:
    # if the hypothesis value is less than the premise, it can be entailed from the premise
    label = "entailment"

print(label)
