age_14_premise = 20
age_14_hypothesis = 80
age_15_premise = 70
age_15_hypothesis = 70
age_13_premise = 50
age_13_hypothesis = 50
age_12_premise = 60
age_12_hypothesis = 60

# the hypothesis talks about the number of boys of each age in John's School, referenced also in the premise
if age_14_hypothesis!= age_14_premise:
    # check if the number of boys of age 14 in the hypothesis contradicts the number of boys of age 14 reported in the premise
    label = "contradiction"
elif age_15_hypothesis!= age_15_premise:
    # check if the number of boys of age 15 in the hypothesis contradicts the number of boys of age 15 reported in the premise
    label = "contradiction"
elif age_13_hypothesis!= age_13_premise:
    # check if the number of boys of age 13 in the hypothesis contradicts the number of boys of age 13 reported in the premise
    label = "contradiction"
elif age_12_hypothesis!= age_12_premise:
    # check if the number of boys of age 12 in the hypothesis contradicts the number of boys of age 12 reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
