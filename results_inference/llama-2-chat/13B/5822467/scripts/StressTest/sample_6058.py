anita_days_premise = 38
anita_days_hypothesis = 18
indu_days_premise = 27
indu_days_hypothesis = 27
geeta_days_premise = 36
geeta_days_hypothesis = 36

# the hypothesis refers to the number of days taken by each person to complete the work
if anita_days_premise <= anita_days_hypothesis and indu_days_premise <= indu_days_hypothesis and geeta_days_premise <= geeta_days_hypothesis:
    # check if the estimate of each person's work days in the hypothesis contradicts the premise
    label = "contradiction"
elif any([premise_value!= hypothesis_value for premise_value, hypothesis_value in zip(
        [anita_days_premise, indu_days_premise, geeta_days_premise],
        [anita_days_hypothesis, indu_days_hypothesis, geeta_days_hypothesis]
    )]):
    # check if any of the hypothesis values contradict the premise values
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
