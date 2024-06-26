sameer_anand_ratio_premise = 6/4
sameer_anand_ratio_hypothesis = 5/4

# the hypothesis gives a more specific ratio of Sameer and Anand's ages, which also was mentioned in the premise
if sameer_anand_ratio_hypothesis >= sameer_anand_ratio_premise:
    # check if the hypothesis ratio contradicts the estimate of less than 'sameer_anand_ratio_premise'
    label = "contradiction"
else:
    # any ratio of Sameer and Anand's ages less than 'sameer_anand_ratio_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
