school_distance_premise = 850  # in meters
school_distance_hypothesis = 750  # in meters

# the hypothesis refers to the distance from Shreehari's house to his school mentioned in the premise
if school_distance_hypothesis > school_distance_premise:
    # check if the hypothesis contradicts the premise that the school is less than 'school_distance_premise' meters away
    label = "contradiction"
elif school_distance_hypothesis == school_distance_premise:
    # check if the hypothesis correctly entails the premise
    label = "entailment"
else:
    # the premise gives only an estimate for the distance to the school
    # any distance less than 'school_distance_premise' meters is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
