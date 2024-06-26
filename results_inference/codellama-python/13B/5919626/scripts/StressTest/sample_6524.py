average_premise = 70
average_hypothesis = 70

# the premise and hypothesis are the same
if average_premise!= average_hypothesis:
    # check if the hypothesis value contradicts the estimate of 'average_premise'
    label = "contradiction"
else:
    # the premise and hypothesis are the same
    label = "entailment"

print(label)
