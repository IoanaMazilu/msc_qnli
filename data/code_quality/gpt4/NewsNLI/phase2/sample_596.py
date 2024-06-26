wreckage_depth_feet_premise = 15000
wreckage_depth_meters_premise = 4500
wreckage_depth_meters_hypothesis = 4500

# the hypothesis mentions the wreckage depth in meters, which is also mentioned in the premise
if wreckage_depth_meters_hypothesis != wreckage_depth_meters_premise:
    # check if the wreckage depth in the hypothesis contradicts the wreckage depth reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
