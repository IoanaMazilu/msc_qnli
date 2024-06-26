boys_age_14_premise = 80
boys_age_14_hypothesis = 50
boys_age_15_premise = 70
boys_age_15_hypothesis = 70
boys_age_13_premise = 50
boys_age_13_hypothesis = 50
boys_age_12_premise = 60
boys_age_12_hypothesis = 60

# the hypothesis refers to the number of boys in each age group mentioned in the premise
if boys_age_14_premise < boys_age_14_hypothesis:
    # check if the number of boys aged 14 in the hypothesis contradicts the number given in the premise
    label = "contradiction"
elif boys_age_15_premise != boys_age_15_hypothesis or boys_age_13_premise != boys_age_13_hypothesis or boys_age_12_premise != boys_age_12_hypothesis:
    # check if the number of boys in any other age group contradicts the numbers given in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
