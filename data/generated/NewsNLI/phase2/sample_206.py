# Premise: Chautauqua Airlines flight 3071 came within 800 vertical feet and.82 nautical miles after take-off of an arriving aircraft, identified as Republic Airlines flight 3329, authorities said.
# Hypothesis: A plane came within 800 vertical feet and less than one nautical mile of another aircraft.
# Golden Label: entailment

vertical_distance_premise = 800
vertical_distance_hypothesis = 800
nautical_miles_premise = 0.82
nautical_miles_hypothesis = 1

# the hypothesis mentions the vertical distance and the nautical miles which are also mentioned in the premise
if vertical_distance_hypothesis != vertical_distance_premise:
    # check if the vertical distance in the hypothesis contradicts the vertical distance reported in the premise
    label = "contradiction"
elif nautical_miles_hypothesis < nautical_miles_premise:
    # check if the nautical miles from the hypothesis contradicts the nautical miles in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

