years_premise = 6
years_hypothesis = 4
age_premise = 38
age_hypothesis = 38

# the hypothesis talks about the age of Sandy after a certain number of years, referenced also in the premise
if years_hypothesis > years_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
elif age_hypothesis!= age_premise:
    # check if the age in the hypothesis contradicts the age reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
