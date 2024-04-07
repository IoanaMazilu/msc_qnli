# Premise: Rakesh travelled less than 8800 kilometre by air which formed 3/5 of the total journey.
# Hypothesis: Rakesh travelled 1800 kilometre by air which formed 3/5 of the total journey.
# Golden Label: neutral

air_travel_premise = 8800
air_travel_hypothesis = 1800
journey_fraction_premise = 3/5
journey_fraction_hypothesis = 3/5

# the hypothesis refers to the air travel distance and its proportion of the total journey, as given in the premise
if air_travel_hypothesis >= air_travel_premise:
    # check if the hypothesis value contradicts the estimate of less than 'air_travel_premise'
    label = "contradiction"
elif journey_fraction_hypothesis != journey_fraction_premise:
    # check if the fraction of the journey travelled by air in the hypothesis contradicts the same fraction given in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

