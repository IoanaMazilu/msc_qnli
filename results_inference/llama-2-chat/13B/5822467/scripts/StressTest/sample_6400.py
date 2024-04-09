passenger_miami_premise = 8/2 * passenger_kennedy_premise
passenger_miami_hypothesis = 1/2 * passenger_kennedy_hypothesis
passenger_logan_premise = 4 * passenger_miami_premise

# the hypothesis refers to the number of passengers that used Miami Airport and Logan Airport
if passenger_miami_hypothesis <= passenger_miami_premise:
    # check if the estimate of 'passenger_miami_hypothesis' contradicts the number of passengers that used Miami Airport in the premise
    label = "contradiction"
elif passenger_logan_premise!= passenger_logan_hypothesis:
    # check if the number of passengers that used Logan Airport in the hypothesis contradicts the number of passengers that used Logan Airport in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
