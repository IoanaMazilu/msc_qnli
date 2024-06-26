gang_size_premise = 8
gang_size_hypothesis = 3

# the hypothesis refers to the number of gang members Andrew has, which is also mentioned in the premise
if gang_size_premise >= gang_size_hypothesis:
    # check if the estimate of 'gang_size_hypothesis' contradicts the number of gang members in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
