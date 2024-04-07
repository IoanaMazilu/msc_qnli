# Premise: Rakesh travelled 1800 kilometre by air which formed 3/5 of the total journey.
# Hypothesis: Rakesh travelled 7800 kilometre by air which formed 3/5 of the total journey.
# Golden Label: contradiction

travel_by_air_premise = 1800
travel_by_air_hypothesis = 7800
fraction_of_journey_premise = 3/5
fraction_of_journey_hypothesis = 3/5

# the hypothesis talks about the distance travelled by air and the fraction it represents of the total journey, both mentioned in the premise
if travel_by_air_hypothesis != travel_by_air_premise:
    # check if the distance travelled by air in the hypothesis contradicts the distance travelled by air reported in the premise
    label = "contradiction"
elif fraction_of_journey_hypothesis != fraction_of_journey_premise:
    # check if the fraction of the journey travelled by air in the hypothesis contradicts the fraction reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

