apples_maddie_premise = 18
apples_maddie_hypothesis = 48
apples_given = 22

# the hypothesis talks about the number of apples Maddie has, referenced also in the premise
if apples_maddie_hypothesis <= apples_maddie_premise:
    # check if the hypothesis value contradicts the estimate of more than 'apples_maddie_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of apples Maddie has
    # any number of apples greater than 'apples_maddie_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
