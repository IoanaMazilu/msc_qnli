Roshan_age_premise = 5
Roshan_age_hypothesis = 2
Raj_age_premise = 3
Raj_age_hypothesis = 4

# the hypothesis talks about the age difference between Roshan and Raj, which is also mentioned in the premise
if Roshan_age_hypothesis <= Roshan_age_premise:
    # check if the hypothesis value contradicts the estimate of the age difference in the premise
    label = "contradiction"
elif Raj_age_hypothesis!= Raj_age_premise:
    # check if the hypothesis value contradicts the estimate of the age ratio in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
