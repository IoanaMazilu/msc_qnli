passenger_premise = 100000
passenger_hypothesis = 100000

# the hypothesis mentions the amount paid by one passenger, which is also mentioned in the premise
if passenger_hypothesis!= passenger_premise:
    # check if the amount paid by the passenger in the hypothesis contradicts the amount paid in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
