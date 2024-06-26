premise_air_travel = 1800
hypothesis_air_travel = 8800
total_journey_premise = 3/5 * premise_air_travel
total_journey_hypothesis = 3/5 * hypothesis_air_travel

# Check if the hypothesis value contradicts the estimate of the premise
if hypothesis_air_travel <= total_journey_premise:
    label = "contradiction"
elif hypothesis_air_travel > total_journey_hypothesis:
    # Check if the hypothesis value contradicts the estimate of the total journey in the premise
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
