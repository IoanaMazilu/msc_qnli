# Premise: Rakesh travelled 1800 kilometre by air which formed 3/5 of the total journey.
# Hypothesis: Rakesh travelled less than 8800 kilometre by air which formed 3/5 of the total journey.
# Golden Label: entailment

journey_by_air_premise = 1800
journey_by_air_hypothesis = 8800
journey_fraction_premise = 3/5
journey_fraction_hypothesis = 3/5

# the hypothesis refers to the distance travelled by air and the fraction of the total journey it represents, both mentioned in the premise
if journey_by_air_hypothesis >= journey_by_air_premise:
    # check if the 'journey_by_air_hypothesis' contradicts the distance travelled by air in the premise
    label = "contradiction"
elif journey_fraction_hypothesis != journey_fraction_premise:
    # check if the fraction of the total journey in the hypothesis contradicts the fraction in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

