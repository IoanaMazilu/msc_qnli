# define the ratios as integers
ratio_premise = 4/3
ratio_hypothesis = 4/3

# the hypothesis refers to the age ratio mentioned in the premise
if ratio_hypothesis <= ratio_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)