anita_days_premise = 18
indu_days_premise = 27
geeta_days_premise = 36

anita_days_hypothesis = 38
indu_days_hypothesis = 27
geeta_days_hypothesis = 36

# the hypothesis talks about the number of days required to complete the work
if anita_days_hypothesis <= anita_days_premise and indu_days_hypothesis <= indu_days_premise and geeta_days_hypothesis <= geeta_days_premise:
    # check if the hypothesis values contradict the premise ones
    label = "contradiction"
elif any([hypothesis > premise for hypothesis, premise in zip(anita_days_hypothesis, anita_days_premise), (indu_days_hypothesis, indu_days_premise), (geeta_days_hypothesis, geeta_days_premise)]):
    # check if any of the hypothesis values contradict the premise ones
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
