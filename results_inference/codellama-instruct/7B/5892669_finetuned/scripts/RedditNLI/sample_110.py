percentage_increase_premise = 1.5
percentage_increase_hypothesis = 1.5

# the hypothesis and premise mention the percentage increase in pending sales of homes in March
if percentage_increase_hypothesis!= percentage_increase_premise:
    # check if the percentage increase in the hypothesis contradicts the percentage increase in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
