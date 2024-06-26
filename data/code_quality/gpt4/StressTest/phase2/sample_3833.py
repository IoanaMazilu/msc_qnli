peanuts_in_box_premise = 10
peanuts_added = 8
peanuts_in_box_hypothesis = 10

# The hypothesis refers to the initial number of peanuts in the box, which is also mentioned in the premise
if peanuts_in_box_hypothesis >= peanuts_in_box_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # the premise gives a specific number of peanuts in the box,
    # any lesser number of peanuts in the box is consistent with the premise, but cannot be explicitly entailed
    label = "neutral"

print(label)
