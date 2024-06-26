pennies_premise = 100.0
quarters_premise = 783.0
borrowed_quarters = 271.0
quarters_now_hypothesis = 513.0

# the hypothesis refers to the number of quarters, which is also mentioned in the premise
# compute the total number of quarters in the premise
quarters_total_premise = quarters_premise + borrowed_quarters

# compare the number of quarters in the hypothesis with the total number of quarters in the premise
if quarters_now_hypothesis!= quarters_total_premise:
    # if the number of quarters in the hypothesis does not match the total number of quarters in the premise, then it's a contradiction
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
