years_premise = 3
years_hypothesis = 2
age_premise = 26
age_hypothesis = 26

# the hypothesis refers to the future age of Arun and the years after which it will be reached, mentioned also in the premise
if years_hypothesis >= years_premise:
    # check if the hypothesis value contradicts the estimate of less than 'years_premise'
    label = "contradiction"
elif age_hypothesis != age_premise:
    # check if the future age in the hypothesis contradicts the future age reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
