# Premise: The total of the ages of Amar, Akbar and Anthony is 36 years.
# Hypothesis: The total of the ages of Amar, Akbar and Anthony is more than 36 years.
# Golden Label: contradiction

total_age_premise = 36
total_age_hypothesis = 36

# the hypothesis refers to the total age of Amar, Akbar and Anthony mentioned in the premise
if total_age_hypothesis != total_age_premise:
    # check if the hypothesis value contradicts the total age of Amar, Akbar and Anthony in the premise
    label = "contradiction"
elif total_age_premise < total_age_hypothesis:
    # check if the total age in the hypothesis contradicts the total age reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

