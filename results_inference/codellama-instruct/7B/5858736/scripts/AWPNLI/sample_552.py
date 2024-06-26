noodles_premise = 54.0
noodles_given_premise = 12.0
noodles_hypothesis = 42.0

# the hypothesis refers to the number of noodles, which are also mentioned in the premise
# compute the total number of noodles in the premise
total_noodles_premise = noodles_premise - noodles_given_premise
if total_noodles_hypothesis!= total_noodles_premise:
    # check if the number of noodles in the hypothesis contradicts the number of noodles from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
