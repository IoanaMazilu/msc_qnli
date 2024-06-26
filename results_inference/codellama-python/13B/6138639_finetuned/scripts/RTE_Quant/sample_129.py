parties_premise = 3
parties_hypothesis = 3

# the hypothesis talks about the number of parties in a Dutch coalition government, which is also mentioned in the premise
if parties_hypothesis!= parties_premise:
    # check if the number of parties in the hypothesis contradicts the number of parties from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
