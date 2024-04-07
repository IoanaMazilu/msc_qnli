# Premise: How many different possible committees of 3 people can be selected from these 7 people if at least one of either Jane or Thomas is to be selected?
# Hypothesis: How many different possible committees of more than 3 people can be selected from these 7 people if at least one of either Jane or Thomas is to be selected?
# Golden Label: contradiction

committee_size_premise = 3
committee_size_hypothesis = 3
people_count = 7

# the hypothesis refers to the number of people in a committee, also mentioned in the premise
if committee_size_hypothesis > committee_size_premise:
    # check if the number of people in the hypothesis contradicts the number of people in the premise
    label = "contradiction"
elif committee_size_hypothesis < committee_size_premise:
    # check if the number of people in the hypothesis is lower than the number of people in the premise
    label = "contradiction"
else:
    # if the number of people in the hypothesis equals the number of people in the premise, we can infer entailment
    label = "entailment"

print(label)
