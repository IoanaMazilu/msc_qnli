weeks_premise = 6
weeks_hypothesis = 3
average_gym_visits_premise = 2
average_gym_visits_hypothesis = 2

# the hypothesis talks about the number of weeks and average gym visits, referenced also in the premise
if weeks_hypothesis > weeks_premise:
    # check if the hypothesis value contradicts the estimate of less than 'weeks_premise'
    label = "contradiction"
elif average_gym_visits_hypothesis!= average_gym_visits_premise:
    # check if the average gym visits in the hypothesis contradicts the average gym visits reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of weeks
    # any number of weeks less than 'weeks_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
