apples_maddie_premise = 25
apples_maddie_hypothesis = 15
apples_given_to_mike = 8

# the hypothesis mentions the number of apples Maddie has which is also referred in the premise
if apples_maddie_hypothesis >= apples_maddie_premise:
    # check if the hypothesis value contradicts the premise estimate of less than 'apples_maddie_premise'
    label = "contradiction"
elif apples_maddie_hypothesis - apples_given_to_mike != apples_maddie_premise - apples_given_to_mike:
    # check if the number of apples left after Maddie gives some to Mike in the hypothesis contradicts the number left in the premise
    label = "contradiction"
else:
    # the premise provides an estimate for the number of apples Maddie has
    # any number of apples less than 'apples_maddie_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
