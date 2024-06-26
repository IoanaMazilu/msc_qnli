father_age_premise = 2 * Shankar_age_premise + 10
father_age_hypothesis = 2 * Shankar_age_hypothesis + 30

# check if the hypothesis value contradicts the estimate of father's age in the premise
if father_age_hypothesis <= father_age_premise:
    label = "contradiction"
elif Shankar_age_hypothesis!= Shankar_age_premise:
    # check if the number of Shankar's age in the hypothesis contradicts the number of Shankar's age reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
