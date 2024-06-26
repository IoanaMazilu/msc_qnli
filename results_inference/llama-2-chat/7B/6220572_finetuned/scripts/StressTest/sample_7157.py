age_ratio_premise = 4/3
age_ratio_hypothesis = 4/3

# the hypothesis talks about the age ratio between Sandy and Molly, referenced also in the premise
if age_ratio_hypothesis <= age_ratio_premise:
    # check if the hypothesis value contradicts the ratio of 'age_ratio_premise'
    label = "contradiction"
else:
    # any ratio greater than 'age_ratio_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
