# Premise: In John's School, there are more than 20 boys of age 14 each, 70 boys of age 15 each & 50 boys of age 13 each and another 60 boys of age 12 each.
# Hypothesis: In John's School, there are 80 boys of age 14 each, 70 boys of age 15 each & 50 boys of age 13 each and another 60 boys of age 12 each.
# Golden Label: neutral

boys_age_14_premise = 20
boys_age_14_hypothesis = 80
boys_age_15_premise = 70
boys_age_15_hypothesis = 70
boys_age_13_premise = 50
boys_age_13_hypothesis = 50
boys_age_12_premise = 60
boys_age_12_hypothesis = 60

# the hypothesis talks about the number of boys of different ages in John's School, referenced also in the premise
if boys_age_14_hypothesis <= boys_age_14_premise:
    # check if the hypothesis value for boys aged 14 contradicts the estimate of more than 'boys_age_14_premise'
    label = "contradiction"
elif boys_age_15_hypothesis != boys_age_15_premise:
    # check if the number of boys aged 15 in the hypothesis contradicts the number of boys aged 15 reported in the premise
    label = "contradiction"
elif boys_age_13_hypothesis != boys_age_13_premise:
    # check if the number of boys aged 13 in the hypothesis contradicts the number of boys aged 13 reported in the premise
    label = "contradiction"
elif boys_age_12_hypothesis != boys_age_12_premise:
    # check if the number of boys aged 12 in the hypothesis contradicts the number of boys aged 12 reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of boys aged 14
    # any number of boys aged 14 greater than 'boys_age_14_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
    
print(label)

