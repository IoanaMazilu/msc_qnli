expert_premise = 10
shots_premise = 6

# define variables with representative names for the numerical entities in both inputs
expert_hypothesis = 10
shots_hypothesis = 4

# extract all quantities as valid numbers (integers or floats)
expert_premise = int(expert_premise)
shots_premise = int(shots_premise)
expert_hypothesis = int(expert_hypothesis)
shots_hypothesis = int(shots_hypothesis)

# use brief comments to explain what comparison you do between the defined variables
# do not use their values in the comments

# compare the number of shots in the premise and hypothesis
if shots_premise!= shots_hypothesis:
    # check if the number of shots in the hypothesis contradicts the number of shots in the premise
    label = "contradiction"
elif expert_premise!= expert_hypothesis:
    # check if the number of shots in the hypothesis is not explicitly entailed by the premise
    label = "neutral"
else:
    # if the number of shots in the hypothesis is explicitly entailed by the premise, we can infer entailment
    label = "entailment"

print(label)
