rocket_range_km_premise = 60
rocket_range_miles_premise = 37
rocket_range_miles_hypothesis = 37

# the hypothesis mentions the range of the rockets in miles, which is also mentioned in the premise
if rocket_range_miles_hypothesis != rocket_range_miles_premise:
    # check if the rocket range in the hypothesis contradicts the rocket range stated in the premise
    label = "contradiction"
else:
    # if the rocket range from the hypothesis does not contradict the range in the premise, we can infer entailment
    label = "entailment"

print(label)
