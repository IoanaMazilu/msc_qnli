amar_age_premise = 45
amar_age_hypothesis = 75
akbar_age_premise = 45
akbar_age_hypothesis = 75
anthony_age_premise = 45
anthony_age_hypothesis = 75

# the hypothesis talks about the total of the ages of Amar, Akbar and Anthony
if amar_age_hypothesis <= amar_age_premise + akbar_age_premise + anthony_age_premise:
    # check if the hypothesis value contradicts the estimate of the total ages in the premise
    label = "contradiction"
elif akbar_age_hypothesis!= akbar_age_premise or anthony_age_hypothesis!= anthony_age_premise:
    # check if any of the individual ages in the hypothesis contradict the corresponding ages in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
