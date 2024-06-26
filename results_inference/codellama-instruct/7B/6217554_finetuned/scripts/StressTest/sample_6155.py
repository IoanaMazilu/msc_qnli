john_age_in_premise = 21
wilson_age_in_premise = 21
john_age_in_hypothesis = 71
wilson_age_in_hypothesis = 71

# the hypothesis talks about the age of John and Wilson at a future time, referenced also in the premise
if john_age_in_hypothesis!= john_age_in_premise:
    # check if the age of John in the hypothesis contradicts the age of John in the premise
    label = "contradiction"
elif wilson_age_in_hypothesis!= wilson_age_in_premise:
    # check if the age of Wilson in the hypothesis contradicts the age of Wilson in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
