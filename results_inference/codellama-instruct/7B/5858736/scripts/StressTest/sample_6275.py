jack_lap_time_premise = 6
lee_lap_time_premise = 10
jack_lap_time_hypothesis = 5
lee_lap_time_hypothesis = 10

if jack_lap_time_hypothesis <= jack_lap_time_premise:
    label = "contradiction"
elif lee_lap_time_hypothesis!= lee_lap_time_premise:
    label = "contradiction"
else:
    label = "entailment"

print(label)
