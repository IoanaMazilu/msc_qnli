john_age_premise = 21
john_age_hypothesis = 71
wilson_age_premise = 21
wilson_age_hypothesis = 71

# the hypothesis talks about the age of John and Wilson in the future
if john_age_hypothesis <= john_age_premise:
    # check if the hypothesis value contradicts the estimate of John's age in the premise
    label = "contradiction"
elif wilson_age_hypothesis!= wilson_age_premise:
    # check if the number of Wilson's age in the hypothesis contradicts the number of Wilson's age reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
