grapes_premise = 4
grapes_hypothesis = 8
grape_rate_premise = 70
grape_rate_hypothesis = 70
mangoes_premise = 9
mangoes_hypothesis = 9
mango_rate_premise = 55
mango_rate_hypothesis = 55

# the hypothesis talks about the number of kgs and rate of grapes and mangoes that Harkamal purchased, which is also referenced in the premise
if grapes_hypothesis <= grapes_premise or grape_rate_hypothesis != grape_rate_premise:
    # check if the hypothesis values contradict the estimate of more than 'grapes_premise' kgs of grapes and the rate of 'grape_rate_premise', mentioned in the premise
    label = "contradiction"
elif mangoes_hypothesis != mangoes_premise or mango_rate_hypothesis != mango_rate_premise:
    # check if the number of mangoes in kgs and the rate of mangoes in the hypothesis contradicts the number of mangoes in kgs and the rate of mangoes reported in the premise
    label = "contradiction"
elif grapes_hypothesis > grapes_premise and grape_rate_hypothesis == grape_rate_premise and mangoes_hypothesis == mangoes_premise and mango_rate_hypothesis == mango_rate_premise:
    # if the hypothesis values and estimates do not contradict the premise ones, but cannot be explicitly entailed from the premise, we can infer neutral
    label = "neutral"

print(label)
