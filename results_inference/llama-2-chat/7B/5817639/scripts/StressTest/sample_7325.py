average_gym_visits_premise = 1
average_gym_visits_hypothesis = 3

# the hypothesis refers to the number of times Rikki goes to the gym in the future, which is also mentioned in the premise
if average_gym_visits_premise <= average_gym_visits_hypothesis:
    # check if the estimate of 'average_gym_visits_hypothesis' contradicts the number of times Rikki goes to the gym in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of times Rikki goes to the gym in the future
    # any number of times greater than 'average_gym_visits_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
