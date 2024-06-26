years_premise = 6
years_hypothesis = 2
age_sandy_premise = 30
age_sandy_hypothesis = 30

# the hypothesis refers to Sandy's age after a certain number of years, also mentioned in the premise
if years_hypothesis >= years_premise:
    # check if the hypothesis contradicts the premise
    label = "contradiction"
elif age_sandy_hypothesis!= age_sandy_premise:
    # check if Sandy's age in the hypothesis contradicts the age in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
