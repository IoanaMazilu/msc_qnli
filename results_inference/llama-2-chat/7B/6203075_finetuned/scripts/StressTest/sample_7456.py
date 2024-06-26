apples_premise = 18
apples_hypothesis = 48
given_apples_premise = 22
given_apples_hypothesis = 22

# the hypothesis talks about the number of apples Maddie has, which is also referenced in the premise
if apples_hypothesis <= apples_premise:
    # check if the hypothesis value contradicts the estimate of more than 'apples_premise'
    label = "contradiction"
elif given_apples_hypothesis!= given_apples_premise:
    # check if the given number of apples in the hypothesis contradicts the given number of apples in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of apples
    # any number of apples greater than 'apples_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
