# Premise: Lucy deposited $62500 in an investment fund that provided 8 percent annual return compounded quarterly.
# Hypothesis: Lucy deposited $more than 22500 in an investment fund that provided 8 percent annual return compounded quarterly.
# Golden Label: entailment

deposit_premise = 62500
deposit_hypothesis = 22500
annual_return = 8  # this value is the same in both premise and hypothesis

# the hypothesis refers to the amount Lucy deposited in an investment fund mentioned in the premise
if deposit_premise <= deposit_hypothesis:
    # check if the value 'deposit_hypothesis' contradicts the amount deposited according to the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)

