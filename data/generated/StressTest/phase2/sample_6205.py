# Premise: less than 60 each, are purchased from Ram by Mohan at a price of Rs.
# Hypothesis: 20 each, are purchased from Ram by Mohan at a price of Rs.
# Golden Label: neutral

items_purchased_premise = 60
items_purchased_hypothesis = 20

# the hypothesis refers to the number of items purchased, also mentioned in the premise
if items_purchased_hypothesis >= items_purchased_premise:
    # check if the hypothesis value contradicts the estimate of less than 'items_purchased_premise'
    label = "contradiction"
elif items_purchased_hypothesis < items_purchased_premise:
    # the premise gives only an estimate for the number of items
    # any number of items less than 'items_purchased_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

