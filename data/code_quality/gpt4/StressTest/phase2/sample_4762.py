gallons_water_add_premise = 7
gallons_water_add_hypothesis = 8

# the hypothesis talks about the amount of water, in gallons, Henry would add to a tank, referenced also in the premise
if gallons_water_add_hypothesis <= gallons_water_add_premise:
    # check if the hypothesis value contradicts the estimate of more than 'gallons_water_add_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount of water Henry would add
    # any amount of water greater than 'gallons_water_add_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
