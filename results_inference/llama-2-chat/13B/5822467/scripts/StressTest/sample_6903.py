rahul_paid_premise = 160
rahul_paid_hypothesis = 360

# the hypothesis refers to the amount paid to rent the tool, mentioned in the premise
if rahul_paid_premise <= rahul_paid_hypothesis:
    # check if the hypothesis value contradicts the estimate of 'rahul_paid_premise'
    label = "contradiction"
elif rahul_paid_hypothesis!= rahul_paid_premise:
    # check if the hypothesis value contradicts the amount paid in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
