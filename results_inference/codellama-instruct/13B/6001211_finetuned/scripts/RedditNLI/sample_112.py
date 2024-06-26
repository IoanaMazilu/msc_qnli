percentage_increase_premise = 14
percentage_increase_hypothesis = 14

# the hypothesis and premise mention the percentage increase in bankruptcy filings
if percentage_increase_hypothesis!= percentage_increase_premise:
    # check if the percentage increase in the hypothesis contradicts the percentage increase in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
