apples_maddie_premise = 18
apples_given_to_mike_premise = 12
apples_maddie_hypothesis = 58
apples_given_to_mike_hypothesis = 12

# the hypothesis talks about the number of apples Maddie has and the number she gives to Mike, both of which are also mentioned in the premise
if apples_maddie_hypothesis != apples_maddie_premise or apples_given_to_mike_hypothesis != apples_given_to_mike_premise:
    # check if the number of apples Maddie has or the number she gives to Mike in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
