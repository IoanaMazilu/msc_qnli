catherina_monday_premise = 5
catherina_monday_hypothesis = 6
catherina_wednesday_premise = 5
catherina_wednesday_hypothesis = 6
catherina_friday_premise = 5
catherina_friday_hypothesis = 6
catherina_tuesday_premise = 10
catherina_tuesday_hypothesis = 10
catherina_thursday_premise = 10
catherina_thursday_hypothesis = 10

# the hypothesis talks about the number of hours worked by Catherina on each day, referenced also in the premise
if catherina_monday_hypothesis <= catherina_monday_premise:
    # check if the hypothesis value contradicts the estimate of more than 'catherina_monday_premise'
    label = "contradiction"
elif catherina_wednesday_hypothesis <= catherina_wednesday_premise:
    # check if the hypothesis value contradicts the estimate of more than 'catherina_wednesday_premise'
    label = "contradiction"
elif catherina_friday_hypothesis <= catherina_friday_premise:
    # check if the hypothesis value contradicts the estimate of more than 'catherina_friday_premise'
    label = "contradiction"
elif catherina_tuesday_hypothesis <= catherina_tuesday_premise:
    # check if the hypothesis value contradicts the estimate of more than 'catherina_tuesday_premise'
    label = "contradiction"
elif catherina_thursday_hypothesis <= catherina_thursday_premise:
    # check if the hypothesis value contradicts the estimate of more than 'catherina_thursday_premise'
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
