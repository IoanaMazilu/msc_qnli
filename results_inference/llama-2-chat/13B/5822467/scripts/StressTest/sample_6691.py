premise_air_travel = 8800 # less than 8800 km by air
hypothesis_air_travel = 1800 # 1800 km by air
total_journey_premise = 3/5 * premise_air_travel # 3/5 of the total journey
total_journey_hypothesis = 3/5 * hypothesis_air_travel # 3/5 of the total journey

# Check if the hypothesis value contradicts the premise value
if hypothesis_air_travel > premise_air_travel:
    label = "contradiction"
elif total_journey_hypothesis!= total_journey_premise:
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
