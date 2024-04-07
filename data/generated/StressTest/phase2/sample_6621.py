# Premise: How many different possible committees of 4 people can be selected from these 7 people if at least one of either Jane or Thomas is to be selected?
# Hypothesis: How many different possible committees of less than 5 people can be selected from these 7 people if at least one of either Jane or Thomas is to be selected?
# Golden Label: entailment

committee_size_premise = 4
committee_size_hypothesis = 5
people_premise = 7
people_hypothesis = 7

# the hypothesis talks about the size of the committee and the number of people, both referenced in the premise
if committee_size_hypothesis <= committee_size_premise:
    # check if the size of the committee in the hypothesis contradicts the size of the committee in the premise
    label = "contradiction"
elif people_hypothesis != people_premise:
    # check if the number of people in the hypothesis contradicts the number of people in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

