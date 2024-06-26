shops_premise = 5
shops_hypothesis = 5

# the hypothesis talks about the number of shops in a town, referenced also in the premise
if shops_hypothesis > shops_premise:
    # check if the hypothesis value contradicts the estimate of less than'shops_premise'
    label = "contradiction"
elif shops_hypothesis < shops_premise:
    # check if the hypothesis value is less than the premise estimate
    label = "entailment"
else:
    # if the hypothesis value is equal to the premise estimate, it is neutral
    label = "neutral"

print(label)
