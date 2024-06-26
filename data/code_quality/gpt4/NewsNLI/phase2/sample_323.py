lost_sight_age_premise = 16
lost_sight_age_hypothesis = 16

# The hypothesis mentions the age when Smith lost her sight and registered as blind,
# which is also mentioned in the premise
if lost_sight_age_hypothesis != lost_sight_age_premise:
    # if the age when she lost her sight in the hypothesis contradicts the age reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
