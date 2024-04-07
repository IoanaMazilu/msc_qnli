# Premise: If Michael earned $363 last week, how many hours did he work?
# Hypothesis: If Michael earned $less than 463 last week, how many hours did he work?
# Golden Label: entailment

earnings_premise = 363
earnings_hypothesis = 463

# the hypothesis refers to Michael's earnings last week mentioned in the premise
if earnings_hypothesis <= earnings_premise:
    # check if the estimate of 'earnings_hypothesis' contradicts the exact earnings in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)

