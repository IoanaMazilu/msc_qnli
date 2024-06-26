boys_age_14_premise = 80
boys_age_14_hypothesis = 50
boys_age_15_premise = 70
boys_age_15_hypothesis = 70
boys_age_13_premise = 50
boys_age_13_hypothesis = 50
boys_age_12_premise = 60
boys_age_12_hypothesis = 60

# the hypothesis refers to the number of boys in each age group in John's School, as mentioned in the premise
if boys_age_14_hypothesis!= boys_age_14_premise:
    # check if the number of boys of age 14 in the hypothesis contradicts the number of boys of age 14 in the premise
    label = "contradiction"
elif boys_age_15_hypothesis!= boys_age_15_premise:
    # check if the number of boys of age 15 in the hypothesis contradicts the number of boys of age 15 in the premise
    label = "contradiction"
elif boys_age_13_hypothesis!= boys_age_13_premise:
    # check if the number of boys of age 13 in the hypothesis contradicts the number of boys of age 13 in the premise
    label = "contradiction"
elif boys_age_12_hypothesis!= boys_age_12_premise:
    # check if the number of boys of age 12 in the hypothesis contradicts the number of boys of age 12 in the premise
    label = "contradiction"
else:
    # if the number of boys in each age group in the hypothesis does not contradict the number of boys in each age group in the premise, we can infer entailment
    label = "entailment"

print(label)
