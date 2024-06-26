age_diff_premise = 82
age_diff_hypothesis = 12

# the hypothesis talks about the age difference between Mary and Albert, which is also mentioned in the premise
if age_diff_hypothesis > age_diff_premise:
    # check if the age difference in the hypothesis contradicts the limit set by the premise
    label = "contradiction"
elif age_diff_hypothesis < age_diff_premise:
    # check if the age difference in the hypothesis is less than the limit set by the premise
    label = "entailment"
else:
    # if the age difference in the hypothesis equals the limit set by the premise, it is consistent but not explicitly stated in the premise
    label = "neutral"

print(label)
