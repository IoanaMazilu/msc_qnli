old_premise = 6 * 5 / 3 = 18
old_hypothesis = 20

# the hypothesis talks about the age of a person, referenced also in the premise
if old_hypothesis >= old_premise:
    # check if the hypothesis age contradicts the estimated age in the premise
    label = "contradiction"
else:
    # the premise gives an estimate for the age, and the hypothesis age is consistent with it
    label = "entailment"

print(label)
