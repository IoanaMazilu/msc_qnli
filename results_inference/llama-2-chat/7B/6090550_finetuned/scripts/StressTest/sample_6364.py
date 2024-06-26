y = 136

watermelons_premise = 536

watermelons_hypothesis = 136

# the hypothesis talks about the number of watermelons Mike had after Sally left, which is also mentioned in the premise
if watermelons_hypothesis!= watermelons_premise:
    # check if the number of watermelons in the hypothesis contradicts the number of watermelons reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
