amar_age_premise = 20
akbar_age_premise = 20
anthony_age_premise = 15

amar_age_hypothesis = 20
akbar_age_hypothesis = 20
anthony_age_hypothesis = 15

total_age_premise = 45
total_age_hypothesis = 75

# the hypothesis refers to the total age of Amar, Akbar, and Anthony mentioned in the premise
if total_age_hypothesis!= total_age_premise:
    # check if the total age in the hypothesis contradicts the total age reported in the premise
    label = "contradiction"
elif amar_age_hypothesis!= amar_age_premise or akbar_age_hypothesis!= akbar_age_premise or anthony_age_hypothesis!= anthony_age_premise:
    # check if any of the ages in the hypothesis contradicts the ages reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
