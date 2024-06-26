base_hours_premise = 21
base_hours_hypothesis = 11

# The hypothesis talks about the number of base hours for which Harry is paid x dollars, referenced also in the premise
if base_hours_hypothesis > base_hours_premise:
    # check if the hypothesis value contradicts the number of base hours stated in the premise
    label = "contradiction"
elif base_hours_hypothesis < base_hours_premise:
    # the premise gives a specific number of base hours
    # any number of base hours less than 'base_hours_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
