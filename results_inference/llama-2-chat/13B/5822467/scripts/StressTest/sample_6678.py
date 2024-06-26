# define variables with representative names for the numerical entities in both inputs
aswin_age = 25
sachin_age = 30
sumesh_age = 40

# extract all quantities as valid numbers (integers or floats)
premise_age_sum = aswin_age + sachin_age + sumesh_age
hypothesis_age_sum = premise_age_sum + 43

# use brief comments to explain what comparison we do between the defined variables
# do not use their values in the comments

# compare the premise and hypothesis age sums
if hypothesis_age_sum > premise_age_sum:
    # the hypothesis age sum is greater than the premise age sum, so we can infer entailment
    label = "entailment"
elif premise_age_sum > hypothesis_age_sum:
    # the premise age sum is greater than the hypothesis age sum, so we can infer contradiction
    label = "contradiction"
else:
    # if the premise and hypothesis age sums are equal, we can infer neutrality
    label = "neutral"

print(label)
