boys_age14_premise = 20
boys_age14_hypothesis = 80
boys_age15_premise = 70
boys_age15_hypothesis = 70
boys_age13_premise = 50
boys_age13_hypothesis = 50
boys_age12_premise = 60
boys_age12_hypothesis = 60

# the hypothesis refers to the number of boys of each age mentioned in the premise
if boys_age14_hypothesis <= boys_age14_premise:
    # check if the number of boys of age 14 in the hypothesis contradicts the estimate of more than 'boys_age14_premise'
    label = "contradiction"
elif boys_age15_hypothesis!= boys_age15_premise or boys_age13_hypothesis!= boys_age13_premise or boys_age12_hypothesis!= boys_age12_premise:
    # check if the number of boys of other ages in the hypothesis contradicts the number of boys of the same ages reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of boys of age 14
    # any number of boys of age 14 greater than 'boys_age14_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)