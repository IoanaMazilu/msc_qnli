weeks_premise = 1
weeks_hypothesis = 2
times_gym_premise = 3
times_gym_hypothesis = 3

# the hypothesis refers to the number of weeks and the average number of times Rikki goes to the gym, mentioned in the premise
if weeks_hypothesis <= weeks_premise:
    # check if the estimate of 'weeks_hypothesis' contradicts the number of weeks in the premise
    label = "contradiction"
elif times_gym_hypothesis!= times_gym_premise:
    # check if the average number of times Rikki goes to the gym in the hypothesis contradicts the average number of times reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
