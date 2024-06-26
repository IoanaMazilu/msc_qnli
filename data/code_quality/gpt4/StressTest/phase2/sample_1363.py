apples_maddie_premise = 8
apples_maddie_hypothesis = 6
apples_given_mike_premise = 3
apples_given_mike_hypothesis = 3

# the hypothesis refers to the number of apples Maddie has and the number she gives to Mike
if apples_maddie_hypothesis >= apples_maddie_premise:
    # check if the number of apples Maddie has in the hypothesis contradicts the estimate of less than 'apples_maddie_premise'
    label = "contradiction"
elif apples_given_mike_hypothesis != apples_given_mike_premise:
    # check if the number of apples given to Mike in the hypothesis contradicts the number of apples given in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of apples Maddie has
    # any number of apples less than 'apples_maddie_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
