shirt_premise = 1
shirt_hypothesis = 3

# the hypothesis refers to the number of shirts in an outfit mentioned in the premise
if shirt_premise >= shirt_hypothesis:
    # check if the hypothesis contradicts the premise
    label = "contradiction"
elif shirt_premise < shirt_hypothesis:
    # the premise does not provide enough information to explicitly entail the hypothesis
    label = "neutral"

print(label)
