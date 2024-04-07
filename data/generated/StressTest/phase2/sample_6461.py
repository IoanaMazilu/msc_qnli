# Premise: Lucy deposited $62500 in an investment fund that provided 20 percent annual return compounded quarterly.
# Hypothesis: Lucy deposited $52500 in an investment fund that provided 20 percent annual return compounded quarterly.
# Golden Label: contradiction

deposit_premise = 62500
deposit_hypothesis = 52500
return_percent_premise = 20
return_percent_hypothesis = 20

# the hypothesis refers to the amount deposited by Lucy and the annual return percent, both mentioned in the premise
if deposit_premise != deposit_hypothesis:
    # check if the deposit amount in the hypothesis contradicts the deposit amount in the premise
    label = "contradiction"
elif return_percent_premise != return_percent_hypothesis:
    # check if the return percent in the hypothesis contradicts the return percent in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

