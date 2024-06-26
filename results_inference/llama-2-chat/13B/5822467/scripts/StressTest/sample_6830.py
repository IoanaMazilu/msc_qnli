arun_age_premise = 26
arun_age_hypothesis = 26
years_elapsed_premise = 6
years_elapsed_hypothesis = 3

# the hypothesis refers to Arun's age after 3 years, which is also mentioned in the premise
if arun_age_hypothesis <= arun_age_premise:
    # check if the estimate of 'arun_age_hypothesis' contradicts the age of Arun reported in the premise
    label = "contradiction"
elif years_elapsed_hypothesis!= years_elapsed_premise:
    # check if the number of years elapsed in the hypothesis contradicts the number of years elapsed reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
