# Premise: Swedish Financial Supervisory Authority (FI) investigation concludes "high frequency trading no threat" two days after contradictory study.
# Hypothesis: Swedish Financial Supervisory Authority study reports "no risk with high frequency trading" two days after contradictory study.
# Golden Label: entailment

days_premise = 2
days_hypothesis = 2

# the hypothesis and premise mention the number of days between a contradictory study and the response of the Swedish Financial Supervisory Authority (FI)
if days_hypothesis != days_premise:
    # check if the number of days in the hypothesis contradicts the number of days in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

