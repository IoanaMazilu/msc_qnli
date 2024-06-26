apples_maddie_premise = 6
apples_maddie_hypothesis = 8
apples_given_to_mike = 3

# the hypothesis talks about the number of apples Maddie has, referenced also in the premise
if apples_maddie_hypothesis <= apples_maddie_premise:
    # check if the hypothesis value contradicts the exact number of apples Maddie has in the premise
    label = "contradiction"
else:
    # the premise gives the exact number of apples Maddie has, any number of apples less than 'apples_maddie_hypothesis' is consistent with the premise
    # but cannot be explicitly entailed from the premise as it's a range
    label = "neutral"

print(label)
