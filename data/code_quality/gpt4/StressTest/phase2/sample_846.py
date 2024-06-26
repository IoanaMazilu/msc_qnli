distance_to_school_premise = 750  # in meters
distance_to_school_hypothesis = 850  # in meters

# the hypothesis refers to the same distance as the premise
if distance_to_school_hypothesis < distance_to_school_premise:
    # check if the hypothesis value contradicts the premise distance
    label = "contradiction"
elif distance_to_school_hypothesis > distance_to_school_premise:
    # check if the hypothesis value can be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis value does not contradict the premise and can be explicitly entailed from the premise
    label = "entailment"

print(label)
