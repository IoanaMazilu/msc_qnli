years_premise = 25
years_hypothesis = 25

# the hypothesis and premise mention the number of years since China's last slowest economic growth
if years_hypothesis != years_premise:
    # check if the number of years in the hypothesis contradicts the number of years in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
