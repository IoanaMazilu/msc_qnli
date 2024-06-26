boys_age14_premise = 80
boys_age14_hypothesis = 50
boys_age15_premise = 70
boys_age15_hypothesis = 70
boys_age13_premise = 50
boys_age13_hypothesis = 50
boys_age12_premise = 60
boys_age12_hypothesis = 60

# the hypothesis refers to the number of boys of each age group in John's School, mentioned in the premise
if boys_age14_premise!= boys_age14_hypothesis:
    # check if the number of boys of age 14 in the hypothesis contradicts the number of boys of age 14 in the premise
    label = "contradiction"
elif boys_age15_premise!= boys_age15_hypothesis:
    # check if the number of boys of age 15 in the hypothesis contradicts the number of boys of age 15 in the premise
    label = "contradiction"
elif boys_age13_premise!= boys_age13_hypothesis:
    # check if the number of boys of age 13 in the hypothesis contradicts the number of boys of age 13 in the premise
    label = "contradiction"
elif boys_age12_premise!= boys_age12_hypothesis:
    # check if the number of boys of age 12 in the hypothesis contradicts the number of boys of age 12 in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
