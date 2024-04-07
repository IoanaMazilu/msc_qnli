# Premise: How many different possible committees of 3 people can be selected from these 7 people if at least one of either Jane or Thomas is to be selected?
# Hypothesis: How many different possible committees of less than 4 people can be selected from these 7 people if at least one of either Jane or Thomas is to be selected?
# Golden Label: entailment

people_premise = 7
committee_size_premise = 3

people_hypothesis = 7
committee_size_hypothesis = 4

# the hypothesis refers to the number of people and the size of the committee mentioned in the premise
if people_premise != people_hypothesis:
    # check if the number of people in the hypothesis contradicts the number of people in the premise
    label = "contradiction"
elif committee_size_hypothesis <= committee_size_premise:
    # check if the committee size in the hypothesis contradicts the committee size in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
