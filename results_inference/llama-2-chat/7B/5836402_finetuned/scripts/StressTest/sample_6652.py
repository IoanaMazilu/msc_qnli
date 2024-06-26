apples_maddie_premise = 88
apples_given_premise = 12
apples_maddie_hypothesis = 18
apples_given_hypothesis = 12

# the hypothesis talks about the number of apples Maddie has after giving some to Mike, referenced also in the premise
if apples_maddie_hypothesis <= apples_maddie_premise:
    # check if the hypothesis value contradicts the estimate of more than 'apples_maddie_premise'
    label = "contradiction"
elif apples_given_hypothesis!= apples_given_premise:
    # check if the number of apples given in the hypothesis contradicts the number of apples given in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of apples Maddie has
    # any number of apples less than 'apples_maddie_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
