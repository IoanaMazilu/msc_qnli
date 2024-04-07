# Premise: Maddie has more than 18 apples, if she give 22 to mike, how many does she have left?
# Hypothesis: Maddie has 48 apples, if she give 22 to mike, how many does she have left?
# Golden Label: neutral

apples_maddie_premise = 18
apples_maddie_hypothesis = 48
apples_given_to_mike = 22

# the hypothesis talks about the number of apples Maddie has, referenced also in the premise
if apples_maddie_hypothesis <= apples_maddie_premise:
    # check if the hypothesis value contradicts the estimate of more than 'apples_maddie_premise'
    label = "contradiction"
elif apples_given_to_mike != apples_given_to_mike:
    # check if the number of apples given to Mike in the hypothesis contradicts the number of apples given to Mike in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of apples Maddie has
    # any number of apples greater than 'apples_maddie_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

