# Premise: Lucy deposited $62500 in an investment fund that provided 12 percent annual return compounded quarterly.
# Hypothesis: Lucy deposited $more than 42500 in an investment fund that provided 12 percent annual return compounded quarterly.
# Golden Label: entailment

deposit_premise = 62500
deposit_hypothesis = 42500
annual_return_premise = 12
annual_return_hypothesis = 12

# the hypothesis refers to the amount deposited and the annual return rate mentioned in the premise
if deposit_premise <= deposit_hypothesis:
    # check if the deposit amount in the hypothesis contradicts the deposit amount in the premise
    label = "contradiction"
elif annual_return_premise != annual_return_hypothesis:
    # check if the annual return rate in the hypothesis contradicts the return rate in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

