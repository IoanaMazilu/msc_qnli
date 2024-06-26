weeks_premise = 6
weeks_hypothesis = 3
gym_visits_premise = 2
gym_visits_hypothesis = 2

# the hypothesis talks about the number of weeks and the average number of gym visits, both also referenced in the premise
if weeks_hypothesis >= weeks_premise:
    # check if the number of weeks in the hypothesis contradicts the estimate of less than 'weeks_premise' in the premise
    label = "contradiction"
elif gym_visits_hypothesis!= gym_visits_premise:
    # check if the number of gym visits in the hypothesis contradicts the number of gym visits reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
