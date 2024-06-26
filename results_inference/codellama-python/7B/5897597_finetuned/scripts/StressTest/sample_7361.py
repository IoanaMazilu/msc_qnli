age14_boys_premise = 80
age14_boys_hypothesis = 50
age15_boys_premise = 70
age15_boys_hypothesis = 70
age13_boys_premise = 50
age13_boys_hypothesis = 50
age12_boys_premise = 60
age12_boys_hypothesis = 60

# the hypothesis refers to the number of boys of each age mentioned in the premise
if age14_boys_hypothesis!= age14_boys_premise:
    # check if the number of age 14 boys in the hypothesis contradicts the number of age 14 boys reported in the premise
    label = "contradiction"
elif age15_boys_hypothesis!= age15_boys_premise:
    # check if the number of age 15 boys in the hypothesis contradicts the number of age 15 boys reported in the premise
    label = "contradiction"
elif age13_boys_hypothesis!= age13_boys_premise:
    # check if the number of age 13 boys in the hypothesis contradicts the number of age 13 boys reported in the premise
    label = "contradiction"
elif age12_boys_hypothesis!= age12_boys_premise:
    # check if the number of age 12 boys in the hypothesis contradicts the number of age 12 boys reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
