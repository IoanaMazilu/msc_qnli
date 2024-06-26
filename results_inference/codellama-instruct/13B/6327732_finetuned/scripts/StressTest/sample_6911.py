# define variables for the numerical entities in the premise
roshan_age_premise = 5
raj_age_premise = 5 + roshan_age_premise
age_ratio_premise = 3/4

# define variables for the numerical entities in the hypothesis
roshan_age_hypothesis = 2
raj_age_hypothesis = 2 + roshan_age_hypothesis
age_ratio_hypothesis = 3/4

# check if the hypothesis values contradict the premise values
if roshan_age_hypothesis!= roshan_age_premise:
    # the hypothesis value for Roshan's age contradicts the premise value
    label = "contradiction"
elif raj_age_hypothesis!= raj_age_premise:
    # the hypothesis value for Raj's age contradicts the premise value
    label = "contradiction"
elif age_ratio_hypothesis!= age_ratio_premise:
    # the hypothesis value for the age ratio contradicts the premise value
    label = "contradiction"
else:
    # the hypothesis values do not contradict the premise values
    label = "neutral"

print(label)
