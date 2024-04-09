quarters_premise = 100.0 + 783.0
borrowed_quarters_premise = 271.0
total_quarters_hypothesis = 513.0

# compute the total amount of quarters in the premise
total_quarters_premise = quarters_premise + borrowed_quarters_premise

if total_quarters_hypothesis > total_quarters_premise:
    # check if the number of quarters in the hypothesis contradicts the number of quarters from the premise
    label = "contradiction"
elif total_quarters_hypothesis < total_quarters_premise:
    # check if the number of quarters in the hypothesis is less than the number of quarters from the premise
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
