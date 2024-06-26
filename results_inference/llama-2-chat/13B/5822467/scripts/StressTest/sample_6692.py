premise_air_travel = 1800
total_journey_premise = 3/5 * premise_air_travel
hypothesis_air_travel = 7800
total_journey_hypothesis = 3/5 * hypothesis_air_travel

# Check if the hypothesis value contradicts the premise estimate
if hypothesis_air_travel > premise_air_travel:
    label = "contradiction"
elif total_journey_hypothesis!= total_journey_premise:
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
