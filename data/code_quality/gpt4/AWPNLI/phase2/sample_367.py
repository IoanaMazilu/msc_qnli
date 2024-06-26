grew_carrots_premise = 6.0
took_carrots_premise = 3.0
left_carrots_hypothesis = 5.0

# the hypothesis refers to the number of carrots left, which is also mentioned indirectly in the premise
# compute the number of carrots left in the premise
left_carrots_premise = grew_carrots_premise - took_carrots_premise
if left_carrots_hypothesis != left_carrots_premise:
    # check if the number of carrots left in the hypothesis contradicts the number of carrots left from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
