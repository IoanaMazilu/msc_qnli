# The hypothesis refers to the same situation as the premise, but with a different percentage for the on-time departure rate
if_flights_depart_on_time_premise = 40
if_flights_depart_on_time_hypothesis = 50

# the hypothesis refers to the same situation as the premise, but with a different percentage for the on-time departure rate
if entailment:
    # the hypothesis refers to the same situation as the premise, but with a different percentage for the on-time departure rate
    # the premise states that the next three flights departed on-time, which is also the case in the hypothesis
    # therefore, the hypothesis does not contradict the premise
    label = "entailment"
elif contradiction:
    # the hypothesis states a higher percentage for the on-time departure rate than the premise
    # this contradicts the premise, which states that the on-time departure rate is higher than 40%
    label = "contradiction"
else:
    # if the hypothesis percentage is the same as the premise percentage, it is neutral
    label = "neutral"

print(label)
