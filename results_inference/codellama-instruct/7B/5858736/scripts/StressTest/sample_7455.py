apples_maddie_premise = 48
apples_mike_premise = 22
apples_maddie_hypothesis = 18

# the hypothesis talks about the number of apples Maddie has, referenced also in the premise
if apples_maddie_hypothesis <= apples_maddie_premise:
    # check if the hypothesis value contradicts the estimate of more than 'apples_maddie_premise'
    label = "contradiction"
elif apples_maddie_premise - apples_mike_premise <= apples_maddie_hypothesis:
    # check if the number of apples Maddie has left after giving 22 to Mike is consistent with the hypothesis
    label = "entailment"
else:
    # the premise gives only an estimate for the number of apples Maddie has
    # any number of apples greater than 'apples_maddie_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
