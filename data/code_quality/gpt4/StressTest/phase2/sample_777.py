apples_maddie_premise = 15
apples_maddie_hypothesis = 25
apples_given_to_mike = 8

# the hypothesis refers to the number of apples Maddie has and the number of apples she gives to Mike, both mentioned in the premise
if apples_given_to_mike != 8:
    # check if the number of apples given to Mike in the hypothesis contradicts the number of apples given to Mike in the premise
    label = "contradiction"
elif apples_maddie_premise >= apples_maddie_hypothesis:
    # check if the number of apples Maddie has in the premise contradicts the estimate of less than 'apples_maddie_hypothesis'
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
