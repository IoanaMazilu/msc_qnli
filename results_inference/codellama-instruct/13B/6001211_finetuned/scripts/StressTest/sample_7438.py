horses_premise = 25
horses_hypothesis = 25
fastest_horses_premise = 4
fastest_horses_hypothesis = 3

# the hypothesis refers to the number of horses and the fastest horses mentioned in the premise
if horses_hypothesis!= horses_premise:
    # check if the number of horses in the hypothesis contradicts the number of horses reported in the premise
    label = "contradiction"
elif fastest_horses_hypothesis >= fastest_horses_premise:
    # check if the number of fastest horses in the hypothesis contradicts the number of fastest horses in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of fastest horses
    # any number of fastest horses less than 'fastest_horses_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
