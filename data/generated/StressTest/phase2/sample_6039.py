# Premise: Xavier starts from P towards Q at a speed of 90 kmph and after every 12 mins increases his speed by 20 kmph.
# Hypothesis: Xavier starts from P towards Q at a speed of more than 10 kmph and after every 12 mins increases his speed by 20 kmph.
# Golden Label: entailment

initial_speed_premise = 90
initial_speed_hypothesis = 10
speed_increase_premise = 20
speed_increase_hypothesis = 20
time_interval_premise = 12
time_interval_hypothesis = 12

# the hypothesis refers to the initial speed, speed increase and time interval mentioned in the premise
if initial_speed_premise <= initial_speed_hypothesis:
    # check if the estimate of 'initial_speed_hypothesis' contradicts the initial speed in the premise
    label = "contradiction"
elif speed_increase_hypothesis != speed_increase_premise:
    # check if the speed increase in the hypothesis contradicts the speed increase reported in the premise
    label = "contradiction"
elif time_interval_hypothesis != time_interval_premise:
    # check if the time interval in the hypothesis contradicts the time interval reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

