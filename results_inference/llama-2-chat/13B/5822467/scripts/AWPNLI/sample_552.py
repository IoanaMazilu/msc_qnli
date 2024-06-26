noodles_premise = 54.0
noodles_given_premise = 12.0
left_noodles_hypothesis = 42.0

# compute the number of noodles left after giving some to William
left_noodles_premise = noodles_premise - noodles_given_premise

if left_noodles_hypothesis > left_noodles_premise:
    # check if the number of noodles left in the hypothesis contradicts the number of noodles left in the premise
    label = "contradiction"
elif left_noodles_hypothesis!= left_noodles_premise:
    # check if the number of noodles left in the hypothesis contradicts the number of noodles left in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
