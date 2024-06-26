boys_age14_premise = 80
boys_age14_hypothesis = 20
boys_age15_premise = 70
boys_age15_hypothesis = 70
boys_age13_premise = 50
boys_age13_hypothesis = 50
boys_age12_premise = 60
boys_age12_hypothesis = 60

# the hypothesis refers to the number of boys of each age group mentioned in the premise
if boys_age14_premise <= boys_age14_hypothesis:
    # check if the estimate of 'boys_age14_hypothesis' contradicts the number of boys of age 14 in the premise
    label = "contradiction"
elif boys_age15_hypothesis!= boys_age15_premise or boys_age13_hypothesis!= boys_age13_premise or boys_age12_hypothesis!= boys_age12_premise:
    # check if the number of boys of age 15, 13 or 12 in the hypothesis contradicts the number of boys of age 15, 13 or 12 reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
