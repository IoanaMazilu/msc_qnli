# define variables with representative names for the numerical entities in both inputs
flare_premise = 40
futuristic_hypothesis = 40

# extract all quantities as valid numbers (integers or floats)
flare_premise_int = int(flare_premise)
futuristic_hypothesis_int = int(futuristic_hypothesis)

# use brief comments to explain what comparison we do between the defined variables
# do not use their values in the comments

# compare the two values to determine the label
if flare_premise_int == futuristic_hypothesis_int:
    # if the values are the same, the hypothesis does not contradict the premise
    label = "neutral"
elif flare_premise_int < futuristic_hypothesis_int:
    # if the premise value is less than the hypothesis value, the hypothesis entails the premise
    label = "entailment"
else:
    # if the premise value is greater than the hypothesis value, the hypothesis contradicts the premise
    label = "contradiction"

print(label)
