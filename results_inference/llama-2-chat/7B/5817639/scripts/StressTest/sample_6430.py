london_eye_premise = 343
london_eye_hypothesis = 443
high_roller_premise = 550
high_roller_hypothesis = 550

# the hypothesis talks about the height of the London Eye and High Roller, which are also mentioned in the premise
if london_eye_hypothesis == london_eye_premise:
    # check if the estimate of 'london_eye_hypothesis' contradicts the number of 'london_eye_premise'
    label = "entailment"
elif high_roller_hypothesis == high_roller_premise:
    # check if the estimate of 'high_roller_hypothesis' contradicts the number of 'high_roller_premise'
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer neutrality
    label = "neutral"

print(label)
