rake_time_john_premise = 60
rake_time_john_hypothesis = 30
rake_time_todd_premise = 60
rake_time_todd_hypothesis = 60

# the hypothesis talks about the time John and Todd take to rake the lawn, referenced also in the premise
if rake_time_john_hypothesis >= rake_time_john_premise:
    # check if the hypothesis value contradicts the estimate of less than 'rake_time_john_premise'
    label = "contradiction"
elif rake_time_todd_hypothesis!= rake_time_todd_premise:
    # check if the time Todd takes to rake the lawn in the hypothesis contradicts the time reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the time John takes to rake the lawn
    # any time less than 'rake_time_john_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
