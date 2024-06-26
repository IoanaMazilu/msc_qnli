john_rake_time_premise = 30
todd_rake_time_premise = 60
john_rake_time_hypothesis = 60
todd_rake_time_hypothesis = 60

# the hypothesis talks about the time John and Todd take to rake a lawn, referenced also in the premise
if john_rake_time_hypothesis >= john_rake_time_premise:
    # check if the hypothesis value contradicts the estimate of less than 'john_rake_time_hypothesis'
    label = "contradiction"
elif todd_rake_time_hypothesis!= todd_rake_time_premise:
    # check if the time Todd takes to rake the lawn in the hypothesis contradicts the time reported in the premise
    label = "contradiction"
else:
    # the premise gives exact time for John and Todd to rake the lawn
    # any time less than 'john_rake_time_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
