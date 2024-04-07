# Premise: There was 4 to 5 shops in the town which was build by a builder from Mumbai.
# Hypothesis: There was less than 5 to 5 shops in the town which was build by a builder from Mumbai.
# Golden Label: entailment

shops_premise_min = 4
shops_premise_max = 5
shops_hypothesis_min = 1  # assuming less than 5 means anything from 1 to 5
shops_hypothesis_max = 5

# the hypothesis talks about the number of shops in a town, referenced also in the premise
if shops_hypothesis_min < shops_premise_min or shops_hypothesis_max > shops_premise_max:
    # check if the range of shops in the hypothesis contradicts the range of shops reported in the premise
    label = "contradiction"
elif shops_hypothesis_min == shops_premise_min and shops_hypothesis_max == shops_premise_max:
    # check if the range of shops in the hypothesis is exactly the same as the range of shops in the premise
    label = "entailment"
else:
    # if the hypothesis values are within the range given in the premise, but not exactly the same, we can infer neutrality
    label = "neutral"

print(label)

