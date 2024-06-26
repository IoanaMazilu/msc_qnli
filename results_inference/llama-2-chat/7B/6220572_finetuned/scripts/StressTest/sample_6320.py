apples_premise = 4
apples_hypothesis = 6
apples_given_hypothesis = 2

# the hypothesis talks about the number of apples Maddie has and the number of apples she gives to Mike
if apples_hypothesis <= apples_premise:
    # check if the hypothesis value contradicts the estimate of more than 'apples_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of apples
    # any number of apples greater than 'apples_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
