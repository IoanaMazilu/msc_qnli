lap_time_jack_premise = 6
lap_time_jack_hypothesis = 5
lap_time_lee_premise = 10
lap_time_lee_hypothesis = 10

# the hypothesis refers to the lap times of Jack and Lee, mentioned in the premise
if lap_time_jack_hypothesis <= lap_time_jack_premise:
    # check if the estimate of 'lap_time_jack_hypothesis' contradicts the time of Jack in the premise
    label = "contradiction"
elif lap_time_lee_hypothesis!= lap_time_lee_premise:
    # check if the time of Lee in the hypothesis contradicts the time of Lee reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
