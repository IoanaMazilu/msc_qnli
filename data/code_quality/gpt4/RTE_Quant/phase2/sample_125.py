revenue_premise = 42.78 # in million US dollars
revenue_hypothesis = 42.78 # in million US dollars

# the hypothesis talks about the earnings of Tom Online in three months, which is also mentioned in the premise
if revenue_premise == revenue_hypothesis:
    # if the revenue in the hypothesis does not contradict the revenue in the premise, we can infer entailment
    label = "entailment"

print(label)
