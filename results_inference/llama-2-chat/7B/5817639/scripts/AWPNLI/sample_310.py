quarter_premise = 21.0
quarter_hypothesis = 70.0

# compare the number of quarters in the premise and hypothesis
if quarter_hypothesis >= quarter_premise:
    # check if the total number of quarters in the hypothesis contradicts the estimate from the premise
    label = "contradiction"
elif quarter_hypothesis - quarter_premise!= 0:
    # check if the difference between the hypothesis and premise values contradicts the estimate from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
