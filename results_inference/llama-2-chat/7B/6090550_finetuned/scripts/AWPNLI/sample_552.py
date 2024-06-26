initial_noodles_premise = 54.0
given_noodles_premise = 12.0
left_noodles_hypothesis = 42.0

# the hypothesis refers to the number of noodles left, which is also mentioned in the premise
# compute the remaining noodles in the premise
remaining_noodles_premise = initial_noodles_premise - given_noodles_premise
if remaining_noodles_premise!= left_noodles_hypothesis:
    # check if the number of noodles left in the hypothesis contradicts the number of noodles left in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
