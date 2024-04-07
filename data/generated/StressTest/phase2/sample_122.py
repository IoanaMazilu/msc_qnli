# Premise: The total of the ages of Amar, Akbar and Anthony is 40 years.
# Hypothesis: The total of the ages of Amar, Akbar and Anthony is 80 years.
# Golden Label: contradiction

total_ages_premise = 40
total_ages_hypothesis = 80

# the hypothesis refers to the total ages of Amar, Akbar and Anthony mentioned in the premise
if total_ages_hypothesis != total_ages_premise:
    # check if the total ages in the hypothesis contradicts the total ages reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

