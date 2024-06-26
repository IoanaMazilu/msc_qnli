weeks_premise = 2
weeks_hypothesis = 1
times_gym_premise = 3
times_gym_hypothesis = 3

# the hypothesis refers to the number of weeks and the average number of times Rikki goes to the gym per week, mentioned in the premise
if weeks_hypothesis >= weeks_premise:
    # check if the number of weeks in the hypothesis contradicts the estimate of less than 'weeks_premise'
    label = "contradiction"
elif times_gym_hypothesis!= times_gym_premise:
    # check if the average number of times Rikki goes to the gym per week in the hypothesis contradicts the number of times reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of weeks
    # any number of weeks less than 'weeks_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)