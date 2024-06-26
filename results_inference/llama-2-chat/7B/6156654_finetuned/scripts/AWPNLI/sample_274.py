roses_premise = 37.0
sold_premise = 16.0
picked_premise = 19.0
roses_hypothesis = 40.0

# the hypothesis refers to the number of roses, which is also mentioned in the premise
# compute the difference between the number of roses in the premise and the hypothesis
difference = roses_hypothesis - roses_premise

# check if the difference is greater than or equal to zero
if difference <= 0:
    # if the difference is zero or less, we can infer entailment
    label = "entailment"
else:
    # if the difference is greater than zero, we can infer contradiction
    label = "contradiction"

print(label)
