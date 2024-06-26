krish_vaibhav_age_ratio_premise = 8/5
krish_vaibhav_age_ratio_hypothesis = 3/5

# the hypothesis refers to the proportion of Krish and Vaibhav's ages mentioned in the premise
if krish_vaibhav_age_ratio_hypothesis >= krish_vaibhav_age_ratio_premise:
    # check if the proportion in the hypothesis contradicts the premise that the proportion is less than 'krish_vaibhav_age_ratio_premise'
    label = "contradiction"
else:
    # since the premise only gives an upper limit for the ratio
    # any ratio less than 'krish_vaibhav_age_ratio_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
