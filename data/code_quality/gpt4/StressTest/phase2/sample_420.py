flavors_premise = 8
flavors_hypothesis = 2

# the hypothesis talks about the number of ice cream flavors in Guna's parlor, which is also referenced in the premise
if flavors_premise <= flavors_hypothesis:
    # check if the number of flavors in the premise contradicts the estimate of more than 'flavors_hypothesis'
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
