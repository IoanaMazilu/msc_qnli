apples_premise = 127.0
apples_given_premise = 88.0
apples_hypothesis = 39.0

# compute the difference between the premise and hypothesis values
difference = apples_premise - apples_hypothesis

# check if the difference is greater than zero
if difference > 0:
    # the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the difference is zero or negative, the hypothesis is consistent with the premise
    label = "entailment"

print(label)
