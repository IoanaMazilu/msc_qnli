# Premise: How many different possible committees of 4 people can be selected from these 9 people if at least one of either Jane or Thomas is to be selected?
# Hypothesis: How many different possible committees of 1 people can be selected from these 9 people if at least one of either Jane or Thomas is to be selected?
# Golden Label: contradiction

committee_size_premise = 4
committee_size_hypothesis = 1
people_count = 9

# The hypothesis talks about the possible committees from the same group of people mentioned in the premise
if committee_size_hypothesis > committee_size_premise:
    # check if the committee size in the hypothesis contradicts the committee size given in the premise
    label = "contradiction"
elif committee_size_hypothesis < committee_size_premise:
    # the premise gives the size of the committee as 'committee_size_premise'
    # any committee size less than 'committee_size_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the committee size in the hypothesis does not contradict the one in the premise, we can infer entailment
    label = "entailment"

print(label)

