builder_premise = 2
builder_hypothesis = 2
building_days_premise = 15
building_days_hypothesis = 15
homes_premise = 100
homes_hypothesis = 100

# the hypothesis refers to the number of days the builder takes to build homes and the number of homes, both mentioned in the premise
if builder_hypothesis >= builder_premise:
    # check if the hypothesis value contradicts the estimate of 'builder_premise'
    label = "contradiction"
elif building_days_hypothesis!= building_days_premise:
    # check if the number of building days in the hypothesis contradicts the number of building days reported in the premise
    label = "contradiction"
elif homes_hypothesis!= homes_premise:
    # check if the number of homes in the hypothesis contradicts the number of homes reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
