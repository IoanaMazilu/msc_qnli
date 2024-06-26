man_dollars_premise = 100
man_dollars_hypothesis = 100

# the premise and hypothesis refer to the same amount of dollars
if man_dollars_premise!= man_dollars_hypothesis:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # the premise and hypothesis refer to the same amount of dollars
    label = "entailment"

print(label)
