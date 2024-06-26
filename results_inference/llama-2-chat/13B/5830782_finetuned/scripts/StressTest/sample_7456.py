apples_maddie_premise = 18
apples_maddie_hypothesis = 48
apples_given_premise = 22
apples_given_hypothesis = 22

# the hypothesis refers to the number of apples Maddie has and gives to Mike, mentioned in the premise
if apples_given_hypothesis!= apples_given_premise:
    # check if the number of apples given in the hypothesis contradicts the number of apples given in the premise
    label = "contradiction"
elif apples_maddie_hypothesis <= apples_maddie_premise:
    # check if the number of apples Maddie has in the hypothesis contradicts the estimate of more than 'apples_maddie_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of apples Maddie has
    # any number of apples greater than 'apples_maddie_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
