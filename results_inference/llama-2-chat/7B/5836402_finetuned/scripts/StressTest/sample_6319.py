apples_premise = 7
apples_hypothesis = 4
given_apples_premise = 2
given_apples_hypothesis = 2

# the hypothesis refers to the number of apples Maddie has after giving 2 to Mike, which is also mentioned in the premise
# compute the number of apples Maddie has left in the premise
left_apples_premise = apples_premise - given_apples_premise

# compute the number of apples Maddie has left in the hypothesis
left_apples_hypothesis = apples_hypothesis - given_apples_hypothesis

# check if the number of apples Maddie has left in the hypothesis contradicts the number of apples left in the premise
if left_apples_hypothesis!= left_apples_premise:
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
