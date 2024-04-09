john_raking_time_premise = 30
john_raking_time_hypothesis = 60
todd_raking_time_premise = 60
todd_raking_time_hypothesis = 60

# the hypothesis refers to the time John and Todd take to rake a lawn, which is also mentioned in the premise
if john_raking_time_premise > john_raking_time_hypothesis:
    # check if the time John takes to rake a lawn contradicts the hypothesis that it takes him less than 60 minutes
    label = "contradiction"
elif todd_raking_time_premise!= todd_raking_time_hypothesis:
    # check if the time Todd takes to rake a lawn contradicts the hypothesis that it takes him exactly 60 minutes
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
