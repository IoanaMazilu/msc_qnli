friends_premise = 6
friends_hypothesis = 5

# The hypothesis refers to the number of friends that go out to dinner, which is also mentioned in the premise
if friends_premise <= friends_hypothesis:
    # check if the number of friends in the premise contradicts the estimate of more than 'friends_hypothesis'
    label = "contradiction"
else:
    # the premise gives an exact number of friends, which is more than 'friends_hypothesis'
    # so the premise entails the hypothesis
    label = "entailment"

print(label)
