# Premise: It takes Jack and Lee respectively 6 and 10 minutes to finish each lap.
# Hypothesis: It takes Jack and Lee respectively 5 and 10 minutes to finish each lap.
# Golden Label: contradiction

jack_lap_time_premise = 6
lee_lap_time_premise = 10
jack_lap_time_hypothesis = 5
lee_lap_time_hypothesis = 10

# the hypothesis refers to the lap times of Jack and Lee mentioned in the premise
if jack_lap_time_hypothesis != jack_lap_time_premise:
    # check if the lap time of Jack in the hypothesis contradicts the lap time of Jack in the premise
    label = "contradiction"
elif lee_lap_time_hypothesis != lee_lap_time_premise:
    # check if the lap time of Lee in the hypothesis contradicts the lap time of Lee in the premise
    label = "contradiction"
else:
    # if the lap times in the hypothesis do not contradict the lap times in the premise, we can infer entailment
    label = "entailment"

print(label)

