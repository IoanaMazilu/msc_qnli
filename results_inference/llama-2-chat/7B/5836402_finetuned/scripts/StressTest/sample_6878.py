amar_age_premise = 25
akbar_age_premise = 30
anthony_age_premise = 35
total_ages_premise = 66

# the hypothesis refers to the total of the ages mentioned in the premise
if total_ages_premise >= hypothesis:
    # check if the total of ages in the hypothesis contradicts the total of ages in the premise
    label = "contradiction"
elif amar_age_premise + akbar_age_premise + anthony_age_premise < total_ages_premise:
    # check if the total of ages in the hypothesis contradicts the total of ages in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
