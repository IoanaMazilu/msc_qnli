kennedy_airport_premise = 37.3 * 1000000
kennedy_airport_hypothesis = 2979 * 1000000

# the hypothesis refers to the number of airline passengers using Kennedy Airport in a year
if kennedy_airport_hypothesis <= kennedy_airport_premise:
    # check if the estimate of 'kennedy_airport_hypothesis' contradicts the number of airline passengers reported in the premise
    label = "contradiction"
elif kennedy_airport_premise < kennedy_airport_hypothesis:
    # check if the number of airline passengers in the hypothesis contradicts the estimate of 'kennedy_airport_premise'
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
