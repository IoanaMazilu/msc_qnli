land_side_premise = 720
land_side_hypothesis = 120

# the hypothesis talks about the size of a square land, referenced also in the premise
if land_side_hypothesis >= land_side_premise:
    # check if the size of the land in the hypothesis contradicts the premise of less than 'land_side_premise'
    label = "contradiction"
elif land_side_hypothesis < land_side_premise:
    # if the size of the land in the hypothesis is less than 'land_side_premise', it can be entailed from the premise
    label = "entailment"
else:
    # any other situation would be neutral
    label = "neutral"

print(label)
