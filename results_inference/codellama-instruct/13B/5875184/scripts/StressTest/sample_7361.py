premise_boys_age_14 = 80
premise_boys_age_15 = 70
premise_boys_age_13 = 50
premise_boys_age_12 = 60

hypothesis_boys_age_14 = 50
hypothesis_boys_age_15 = 70
hypothesis_boys_age_13 = 50
hypothesis_boys_age_12 = 60

# check if the hypothesis values contradict the premise values
if hypothesis_boys_age_14!= premise_boys_age_14:
    label = "contradiction"
elif hypothesis_boys_age_15!= premise_boys_age_15:
    label = "contradiction"
elif hypothesis_boys_age_13!= premise_boys_age_13:
    label = "contradiction"
elif hypothesis_boys_age_12!= premise_boys_age_12:
    label = "contradiction"
else:
    label = "entailment"

print(label)
