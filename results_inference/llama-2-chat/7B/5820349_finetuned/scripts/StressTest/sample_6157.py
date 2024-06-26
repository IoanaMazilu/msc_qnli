sameer_anand_ratio_premise = 3/4
sameer_anand_ratio_hypothesis = 5/4

# the hypothesis refers to the ratio of Sameer and Anand's ages mentioned in the premise
if sameer_anand_ratio_hypothesis <= sameer_anand_ratio_premise:
    # check if the ratio of'sameer_anand_ratio_hypothesis' contradicts the ratio of Sameer and Anand's ages in the premise
    label = "contradiction"
else:
    # the premise gives only a lower bound for the ratio of Sameer and Anand's ages
    # any ratio greater than'sameer_anand_ratio_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
