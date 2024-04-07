# Premise: How many different possible committees of 3 people can be selected from these 6 people if at least one of either Jane or Thomas is to be selected?
# Hypothesis: How many different possible committees of more than 3 people can be selected from these 6 people if at least one of either Jane or Thomas is to be selected?
# Golden Label: contradiction

committee_size_premise = 3
committee_size_hypothesis = 3

# the hypothesis refers to the size of a committee, which is also mentioned in the premise
if committee_size_hypothesis > committee_size_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif committee_size_hypothesis < committee_size_premise:
    # check if the hypothesis value is less than the premise value
    label = "contradiction"
else:
    # if the hypothesis value and premise value are the same, we can infer entailment
    label = "entailment"

print(label)

