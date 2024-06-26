gallons_added_premise = 7
gallons_added_hypothesis = 5

# the hypothesis talks about the amount of water that Henry adds to the tank, as mentioned in the premise
if gallons_added_hypothesis >= gallons_added_premise:
    # check if the amount of water Henry adds in the hypothesis contradicts the estimate of less than 'gallons_added_premise'
    label = "contradiction"
elif gallons_added_hypothesis == gallons_added_premise - 1:
    # check if the amount of water Henry adds in the hypothesis is exactly one less than 'gallons_added_premise'
    # in this case, the hypothesis can be fully and explicitly entailed from the premise
    label = "entailment"
else:
    # any amount of water less than 'gallons_added_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
