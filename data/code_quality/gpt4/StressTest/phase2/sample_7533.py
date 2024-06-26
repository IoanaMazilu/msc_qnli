leo_gain_premise = 10
leo_gain_hypothesis = 50
weight_difference = 0.50

# the hypothesis refers to the amount of weight Leo gains and its relation to Kendra's weight, which is also mentioned in the premise
if leo_gain_hypothesis <= leo_gain_premise:
    # check if the hypothesis contradicts the premise by stating Leo gains less weight than specified in the premise
    label = "contradiction"
elif leo_gain_hypothesis > leo_gain_premise:
    # the premise specifies a particular weight gain for Leo, any weight gain greater than 'leo_gain_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
