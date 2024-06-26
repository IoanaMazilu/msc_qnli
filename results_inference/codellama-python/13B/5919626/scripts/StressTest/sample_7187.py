apples_man_premise = 3
apples_man_hypothesis = 3

# the hypothesis talks about the number of apples owned by the man, referenced also in the premise
if apples_man_hypothesis!= apples_man_premise:
    # check if the number of apples in the hypothesis contradicts the number of apples reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of apples
    # any number of apples equal to 'apples_man_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
