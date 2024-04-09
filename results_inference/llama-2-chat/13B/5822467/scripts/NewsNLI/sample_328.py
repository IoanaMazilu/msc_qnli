premise_name = "iPhone_name"
hypothesis_name = "iPhone_name_rumor"

# define variables with representative names for the numerical entities in both inputs
iPhone_5_premise = 0.5
iPhone_4S_premise = 0.4
rumor_hypothesis = 0.5

# extract all quantities as valid numbers (integers or floats)
iPhone_5_premise = float(iPhone_5_premise)
iPhone_4S_premise = float(iPhone_4S_premise)
rumor_hypothesis = float(rumor_hypothesis)

# use brief comments to explain what comparison you do between the defined variables
# do not use their values in the comments

# compare the premise and hypothesis values
if iPhone_5_premise == rumor_hypothesis:
    # if the premise and hypothesis values are the same, we can infer entailment
    label = "entailment"
elif iPhone_4S_premise == rumor_hypothesis:
    # if the premise and hypothesis values are the same, we can infer entailment
    label = "entailment"
else:
    # if the premise and hypothesis values are different, we cannot infer entailment or contradiction
    label = "neutral"

print(label)
