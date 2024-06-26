john_time_premise = 30
john_time_hypothesis = 60
todd_time_premise = 60
todd_time_hypothesis = 60

# the hypothesis talks about the time taken by John and Todd to rake a lawn, which is also mentioned in the premise
if john_time_hypothesis <= john_time_premise:
    # check if the hypothesis time for John contradicts the premise time for John
    label = "contradiction"
elif todd_time_hypothesis!= todd_time_premise:
    # check if the hypothesis time for Todd contradicts the premise time for Todd
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
