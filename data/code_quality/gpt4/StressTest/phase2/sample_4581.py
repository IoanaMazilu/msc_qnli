jessica_text_speed_premise = 125
maurice_text_speed_premise = 10
jessica_text_speed_hypothesis = 225
maurice_text_speed_hypothesis = 10

# the hypothesis refers to the texting speed of Jessica and Maurice mentioned in the premise
if jessica_text_speed_premise >= jessica_text_speed_hypothesis:
    # check if the 'jessica_text_speed_premise' contradicts the estimate of less than 'jessica_text_speed_hypothesis'
    label = "contradiction"
elif maurice_text_speed_premise != maurice_text_speed_hypothesis:
    # check if the 'maurice_text_speed_premise' contradicts the 'maurice_text_speed_hypothesis'
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
