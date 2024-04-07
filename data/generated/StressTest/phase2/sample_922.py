# Premise: While Kiran playing all but less than 8 got destroyed.
# Hypothesis: While Kiran playing all but 3 got destroyed.
# Golden Label: neutral

destroyed_items_premise = 8
destroyed_items_hypothesis = 3

# the hypothesis refers to the number of items not destroyed while Kiran was playing, also mentioned in the premise
if destroyed_items_hypothesis >= destroyed_items_premise:
    # check if the number of undestroyed items in the hypothesis contradicts the estimate of less than 'destroyed_items_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of undestroyed items
    # any number less than 'destroyed_items_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

