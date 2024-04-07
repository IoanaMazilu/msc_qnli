# Premise: If Michael earned $210 last week, how many hours did he work?
# Hypothesis: If Michael earned $less than 810 last week, how many hours did he work?
# Golden Label: entailment

earnings_premise = 210
earnings_hypothesis = 810

# the hypothesis refers to the money earned by Michael mentioned in the premise
if earnings_premise >= earnings_hypothesis:
    # check if the estimate of 'earnings_hypothesis' contradicts the amount of earnings in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

