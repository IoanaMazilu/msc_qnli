shirts_premise = 1
shirts_hypothesis = 5
jeans_premise = 1
jeans_hypothesis = 1
sneakers_premise = 1
sneakers_hypothesis = 1

# the hypothesis talks about the number of shirts, jeans, and sneakers in an outfit
if shirts_premise <= shirts_hypothesis:
    # check if the number of shirts in the premise contradicts the hypothesis
    label = "contradiction"
elif jeans_premise!= jeans_hypothesis or sneakers_premise!= sneakers_hypothesis:
    # check if the number of jeans or sneakers in the premise contradicts the hypothesis
    label = "contradiction"
else:
    # if the number of shirts, jeans, and sneakers in the premise matches the hypothesis, we can infer entailment
    label = "entailment"

print(label)
