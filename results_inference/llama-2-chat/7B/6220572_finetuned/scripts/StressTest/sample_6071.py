builder_build_time_premise = 15
builder_build_time_hypothesis = 15

# the hypothesis refers to the build time of the builder mentioned in the premise
if builder_build_time_hypothesis!= builder_build_time_premise:
    # check if the build time in the hypothesis contradicts the build time reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the build time
    # any build time greater than 'builder_build_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
