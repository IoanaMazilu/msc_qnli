# define variables for the numerical entities in the premise
roshan_age_premise = 5
raj_age_premise = 5 + roshan_age_premise
age_ratio_premise = 3/4

# define variables for the numerical entities in the hypothesis
roshan_age_hypothesis = 6
raj_age_hypothesis = roshan_age_hypothesis + roshan_age_premise
age_ratio_hypothesis = 3/4

# check if the hypothesis values contradict the premise values
if roshan_age_hypothesis < roshan_age_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif raj_age_hypothesis!= raj_age_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif age_ratio_hypothesis!= age_ratio_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
