builder_premise = 1
builder_hypothesis = 2
build_days_premise = 15
build_days_hypothesis = 15
homes_premise = 100
homes_hypothesis = 100

# the hypothesis refers to the number of builders, build days and homes mentioned in the premise
if builder_hypothesis <= builder_premise:
    # check if the builder number in the hypothesis contradicts the builder number in the premise
    label = "contradiction"
elif build_days_hypothesis!= build_days_premise:
    # check if the build days in the hypothesis contradicts the build days reported in the premise
    label = "contradiction"
elif homes_hypothesis!= homes_premise:
    # check if the number of homes in the hypothesis contradicts the number of homes reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of builders
    # any builder number greater than 'builder_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
