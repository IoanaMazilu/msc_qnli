john_rake_time_premise = 30
john_rake_time_hypothesis = 30
todd_rake_time_premise = 60
todd_rake_time_hypothesis = 60

# the hypothesis talks about the time John and Todd take to rake a lawn
if john_rake_time_premise > john_rake_time_hypothesis:
    # check if the time John takes to rake the lawn in the hypothesis contradicts the premise
    label = "contradiction"
elif todd_rake_time_premise!= todd_rake_time_hypothesis:
    # check if the time Todd takes to rake the lawn in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
