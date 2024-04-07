# Premise: 9000 which he and Dave earned at the end of 1 years.
# Hypothesis: 1000 which he and Dave earned at the end of 1 years.
# Golden Label: contradiction

earning_premise = 9000
earning_hypothesis = 1000

# the hypothesis talks about the earnings of 'he' and 'Dave' at the end of 1 year, which is also referenced in the premise
if earning_hypothesis != earning_premise:
    # check if the earnings in the hypothesis contradicts the earnings reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

