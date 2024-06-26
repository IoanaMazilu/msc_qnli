pennies_premise = 100.0
quarters_premise = 783.0
quarters_borrowed_premise = 271.0
quarters_now_hypothesis = 513.0

# the hypothesis talks about the number of quarters, which is also referenced in the premise
# compute the total number of quarters from the premise
total_quarters_premise = pennies_premise + quarters_premise - quarters_borrowed_premise
if total_quarters_hypothesis!= total_quarters_premise:
    # check if the number of quarters in the hypothesis contradicts the number of quarters from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
