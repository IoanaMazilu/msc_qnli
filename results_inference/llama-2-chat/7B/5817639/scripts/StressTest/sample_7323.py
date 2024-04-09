average_gym_visits_premise = 1
average_gym_visits_hypothesis = 3

# the hypothesis talks about the number of times Rikki goes to the gym, referenced also in the premise
if average_gym_visits_hypothesis <= average_gym_visits_premise:
    # check if the hypothesis value contradicts the estimate of more than 'average_gym_visits_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of times Rikki goes to the gym
    # any number of times greater than 'average_gym_visits_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
