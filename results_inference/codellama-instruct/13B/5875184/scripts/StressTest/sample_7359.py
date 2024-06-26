premise_boys_age_14 = 80
premise_boys_age_15 = 70
premise_boys_age_13 = 50
premise_boys_age_12 = 60

hypothesis_boys_age_14 = 20
hypothesis_boys_age_15 = 70
hypothesis_boys_age_13 = 50
hypothesis_boys_age_12 = 60

# the hypothesis refers to the number of boys of each age mentioned in the premise
if hypothesis_boys_age_14 > premise_boys_age_14:
    # check if the estimate of 'hypothesis_boys_age_14' contradicts the number of boys of age 14 in the premise
    label = "contradiction"
elif hypothesis_boys_age_15!= premise_boys_age_15:
    # check if the number of boys of age 15 in the hypothesis contradicts the number of boys of age 15 reported in the premise
    label = "contradiction"
elif hypothesis_boys_age_13!= premise_boys_age_13:
    # check if the number of boys of age 13 in the hypothesis contradicts the number of boys of age 13 reported in the premise
    label = "contradiction"
elif hypothesis_boys_age_12!= premise_boys_age_12:
    # check if the number of boys of age 12 in the hypothesis contradicts the number of boys of age 12 reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
