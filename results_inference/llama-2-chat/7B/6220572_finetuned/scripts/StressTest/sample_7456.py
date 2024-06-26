apples_premise = 18
apples_hypothesis = 48
apples_given_premise = 22
apples_given_hypothesis = 22

# the hypothesis refers to the number of apples Maddie has, the number of apples given to Mike and the number of apples left
if apples_hypothesis <= apples_premise:
    # check if the hypothesis value contradicts the number of apples in the premise
    label = "contradiction"
elif apples_given_hypothesis!= apples_given_premise:
    # check if the number of apples given in the hypothesis contradicts the number of apples given in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of apples
    # any number of apples greater than 'apples_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
