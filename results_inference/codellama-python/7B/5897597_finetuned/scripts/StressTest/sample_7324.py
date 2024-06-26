weeks_premise = 2
weeks_hypothesis = 1
average_gym_times_premise = 3
average_gym_times_hypothesis = 3

# the hypothesis talks about the number of weeks and average gym times, referenced also in the premise
if weeks_hypothesis >= weeks_premise:
    # check if the hypothesis value contradicts the estimate of less than 'weeks_premise'
    label = "contradiction"
elif average_gym_times_hypothesis!= average_gym_times_premise:
    # check if the average gym times in the hypothesis contradicts the average gym times reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of weeks
    # any number of weeks less than 'weeks_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
