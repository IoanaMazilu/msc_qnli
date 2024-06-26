apples_premise = 18
apples_hypothesis = 48
given_to_mike_premise = 22
given_to_mike_hypothesis = 22

# the hypothesis refers to the number of apples Maddie has, which is also mentioned in the premise
if apples_hypothesis <= apples_premise:
    # check if the number of apples in the hypothesis contradicts the number of apples in the premise
    label = "contradiction"
elif apples_hypothesis - given_to_mike_hypothesis!= apples_premise - given_to_mike_premise:
    # check if the number of apples left after giving some to Mike in the hypothesis contradicts the number of apples left after giving some to Mike in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
