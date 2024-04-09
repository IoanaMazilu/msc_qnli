age_14_boys_premise = 80
age_14_boys_hypothesis = 50
age_15_boys_premise = 70
age_15_boys_hypothesis = 70
age_13_boys_premise = 50
age_13_boys_hypothesis = 50
age_12_boys_premise = 60
age_12_boys_hypothesis = 60

# the hypothesis refers to the number of boys of different ages in John's School mentioned in the premise
if age_14_boys_hypothesis!= age_14_boys_premise:
    # check if the number of boys of age 14 in the hypothesis contradicts the number of boys of age 14 in the premise
    label = "contradiction"
elif age_15_boys_hypothesis!= age_15_boys_premise:
    # check if the number of boys of age 15 in the hypothesis contradicts the number of boys of age 15 in the premise
    label = "contradiction"
elif age_13_boys_hypothesis!= age_13_boys_premise:
    # check if the number of boys of age 13 in the hypothesis contradicts the number of boys of age 13 in the premise
    label = "contradiction"
elif age_12_boys_hypothesis!= age_12_boys_premise:
    # check if the number of boys of age 12 in the hypothesis contradicts the number of boys of age 12 in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
