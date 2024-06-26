# define variables for the numerical entities in the premise
boys_age_14_premise = 80
boys_age_15_premise = 70
boys_age_13_premise = 50
boys_age_12_premise = 60

# define variables for the numerical entities in the hypothesis
boys_age_14_hypothesis = 50
boys_age_15_hypothesis = 70
boys_age_13_hypothesis = 50
boys_age_12_hypothesis = 60

# check if the hypothesis values contradict the premise values
if boys_age_14_hypothesis!= boys_age_14_premise or boys_age_15_hypothesis!= boys_age_15_premise or boys_age_13_hypothesis!= boys_age_13_premise or boys_age_12_hypothesis!= boys_age_12_premise:
    # if the hypothesis values contradict the premise values, we can infer contradiction
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
