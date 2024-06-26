friends_premise = 6
friends_hypothesis = 5

# The hypothesis talks about the number of friends John has, referenced also in the premise
if friends_hypothesis > friends_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
elif friends_hypothesis == friends_premise:
    # check if the hypothesis value is the same as the premise
    label = "entailment"
else:
    # any number of friends less than 'friends_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
