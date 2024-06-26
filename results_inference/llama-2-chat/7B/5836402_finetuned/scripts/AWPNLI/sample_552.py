noodles_total_premise = 54.0
noodles_given_premise = 12.0
noodles_left_hypothesis = 42.0

# the hypothesis refers to the number of noodles left, which are also mentioned in the premise
# compute the number of noodles left in the premise
noodles_left_premise = noodles_total_premise - noodles_given_premise
if noodles_left_hypothesis!= noodles_left_premise:
    # check if the number of noodles left in the hypothesis contradicts the number of noodies left from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
