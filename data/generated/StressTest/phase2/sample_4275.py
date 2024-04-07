# Premise: If Michael earned $352 last week, how many hours did he work?
# Hypothesis: If Michael earned $less than 652 last week, how many hours did he work?
# Golden Label: entailment

earnings_premise = 352
earnings_hypothesis = 652

# the hypothesis refers to the earnings of Michael mentioned in the premise
if earnings_hypothesis <= earnings_premise:
    # check if the estimate of 'earnings_hypothesis' contradicts the earnings in the premise
    label = "contradiction"
elif earnings_hypothesis > earnings_premise:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

