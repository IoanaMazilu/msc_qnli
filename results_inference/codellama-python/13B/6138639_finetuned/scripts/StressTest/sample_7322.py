gym_visits_premise = 2
gym_visits_hypothesis = 2
weeks_premise = 3
weeks_hypothesis = 1

# the hypothesis talks about the number of gym visits in a given number of weeks, referenced also in the premise
if gym_visits_hypothesis!= gym_visits_premise:
    # check if the number of gym visits in the hypothesis contradicts the number of gym visits reported in the premise
    label = "contradiction"
elif weeks_hypothesis > weeks_premise:
    # the premise gives only an estimate for the number of weeks
    # any number of weeks greater than 'weeks_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
