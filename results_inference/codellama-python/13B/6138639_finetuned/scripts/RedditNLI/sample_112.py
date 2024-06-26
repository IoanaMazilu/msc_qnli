percentage_premise = 14
percentage_hypothesis = 14

# the hypothesis and premise mention the percentage of bankruptcy filings
if percentage_hypothesis!= percentage_premise:
    # check if the percentage in the hypothesis contradicts the percentage in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
