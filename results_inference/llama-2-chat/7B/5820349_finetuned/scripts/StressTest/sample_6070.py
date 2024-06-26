builder_premise = 1
builder_hypothesis = 2
building_days_premise = 15
building_days_hypothesis = 15
homes_premise = 100
homes_hypothesis = 100

# the hypothesis talks about the builder, building days and number of homes, all referenced in the premise
if builder_hypothesis <= builder_premise:
    # check if the hypothesis value contradicts the estimate of more than 'builder_premise'
    label = "contradiction"
elif building_days_hypothesis!= building_days_premise:
    # check if the building days in the hypothesis contradicts the building days reported in the premise
    label = "contradiction"
elif homes_hypothesis!= homes_premise:
    # check if the number of homes in the hypothesis contradicts the number of homes reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of builders
    # any number of builders greater than 'builder_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
