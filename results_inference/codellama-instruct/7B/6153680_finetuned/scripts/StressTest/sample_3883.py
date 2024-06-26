miles_jogging_premise = 4
hours_jogging_walking_premise = 3
miles_jogging_hypothesis = 3
hours_jogging_walking_hypothesis = 3

# the hypothesis talks about the same jogging and walking distance as the premise
if miles_jogging_hypothesis!= miles_jogging_premise:
    # check if the jogging distance in the hypothesis contradicts the jogging distance in the premise
    label = "contradiction"
elif hours_jogging_walking_hypothesis!= hours_jogging_walking_premise:
    # check if the total time spent jogging and walking in the hypothesis contradicts the total time spent jogging and walking in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
