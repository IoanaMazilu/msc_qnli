gang_premise = 8
gang_hypothesis = 8

# the hypothesis refers to the number of gang members Andrew has, which is also mentioned in the premise
if gang_hypothesis >= gang_premise:
    # check if the estimate of 'gang_hypothesis' contradicts the number of gang members in the premise
    label = "contradiction"
else:
    # if the hypothesis value is less than the premise value, we can infer entailment
    label = "entailment"

print(label)
