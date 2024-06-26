time_diff_premise = 1
time_diff_hypothesis = 2

# the hypothesis talks about the difference in time taken by Abhay and Sammer in context of Abhay doubling his speed, which is also mentioned in the premise
if time_diff_hypothesis != time_diff_premise:
    # check if the difference in time taken by Abhay and Sammer in the hypothesis contradicts the difference in time taken stated in the premise
    label = "contradiction"
else:
    # if the difference in time taken by Abhay and Sammer in the hypothesis is consistent with the premise, we can infer entailment
    label = "entailment"

print(label)
