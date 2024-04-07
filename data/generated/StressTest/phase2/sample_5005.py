# Premise: Christine selects an item at a less than 85% off ticket price sale.
# Hypothesis: Christine selects an item at a 25% off ticket price sale.
# Golden Label: neutral

discount_premise = 85
discount_hypothesis = 25

# the hypothesis talks about the discount percentage of an item selected by Christine, referenced also in the premise
if discount_hypothesis >= discount_premise:
    # check if the hypothesis value contradicts the estimate of less than 'discount_premise' percentage
    label = "contradiction"
elif discount_hypothesis < discount_premise:
    # the premise gives only an estimate for the discount percentage
    # any discount percentage less than 'discount_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

