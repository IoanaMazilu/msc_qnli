 time_john_premise = 30
time_john_hypothesis = 30
time_todd_premise = 60
time_todd_hypothesis = 60

# the hypothesis refers to the time John and Todd take to rake a lawn, which is also mentioned in the premise
if time_john_premise >= time_john_hypothesis:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif time_todd_hypothesis!= time_todd_premise:
    # check if the time for Todd in the hypothesis contradicts the time in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
