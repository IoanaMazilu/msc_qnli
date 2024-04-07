# Premise: Xavier starts from P towards Q at a speed of 90 kmph and after every 12 mins increases his speed by 10 kmph.
# Hypothesis: Xavier starts from P towards Q at a speed of 10 kmph and after every 12 mins increases his speed by 10 kmph.
# Golden Label: contradiction

start_speed_premise = 90
start_speed_hypothesis = 10
increase_rate_premise = 10
increase_rate_hypothesis = 10
increase_interval_premise = 12
increase_interval_hypothesis = 12

# the hypothesis refers to Xavier's starting speed, speed increase rate, and the interval for speed increase, all mentioned in the premise
if start_speed_premise != start_speed_hypothesis:
    # checking if the starting speed in the hypothesis contradicts the starting speed reported in the premise
    label = "contradiction"
elif increase_rate_premise != increase_rate_hypothesis:
    # checking if the speed increase rate in the hypothesis contradicts the speed increase rate reported in the premise
    label = "contradiction"
elif increase_interval_premise != increase_interval_hypothesis:
    # checking if the speed increase interval in the hypothesis contradicts the speed increase interval reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

