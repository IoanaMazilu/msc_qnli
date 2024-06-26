apples_premise = 48
apples_hypothesis = 88
given_to_mike_premise = 22
given_to_mike_hypothesis = 22

# the hypothesis refers to the number of apples Maddie has, and the number of apples she gives to Mike
if apples_premise!= apples_hypothesis:
    # check if the number of apples in the hypothesis contradicts the number of apples in the premise
    label = "contradiction"
elif given_to_mike_premise!= given_to_mike_hypothesis:
    # check if the number of apples given to Mike in the hypothesis contradicts the number of apples given to Mike in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
