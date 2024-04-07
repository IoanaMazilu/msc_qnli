# Premise: Maddie has less than 7 apples, if she give 2 to mike, how many does she have left?
# Hypothesis: Maddie has 4 apples, if she give 2 to mike, how many does she have left?
# Golden Label: neutral

apples_maddie_premise = 7
apples_maddie_hypothesis = 4
apples_given_to_mike = 2

# the hypothesis talks about the number of apples Maddie has, which is also referenced in the premise
if apples_maddie_hypothesis >= apples_maddie_premise:
    # check if the hypothesis value contradicts the estimate of less than 'apples_maddie_premise'
    label = "contradiction"
elif apples_maddie_hypothesis - apples_given_to_mike != apples_maddie_premise - apples_given_to_mike:
    # check if the number of apples left after Maddie gives some to Mike in the hypothesis contradicts the number left in the premise
    label = "contradiction"
else:
    # any number of apples less than 'apples_maddie_premise' is consistent with the premise, 
    # as well as the remaining after giving 'apples_given_to_mike' to Mike, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

