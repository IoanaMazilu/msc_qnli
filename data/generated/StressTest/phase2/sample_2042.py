# Premise: The pilot of a small aircraft with a 40-gallon fuel tank wants to fly to Cleveland, which is 480 miles away.
# Hypothesis: The pilot of a small aircraft with a 70-gallon fuel tank wants to fly to Cleveland, which is 480 miles away.
# Golden Label: contradiction

fuel_capacity_premise = 40
fuel_capacity_hypothesis = 70
distance_to_cleveland_premise = 480
distance_to_cleveland_hypothesis = 480

# the hypothesis talks about the fuel capacity of an aircraft and the distance to Cleveland, referenced also in the premise
if fuel_capacity_hypothesis != fuel_capacity_premise:
    # check if the fuel capacity in the hypothesis contradicts the fuel capacity reported in the premise
    label = "contradiction"
elif distance_to_cleveland_hypothesis != distance_to_cleveland_premise:
    # check if the distance to Cleveland in the hypothesis contradicts the distance reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

