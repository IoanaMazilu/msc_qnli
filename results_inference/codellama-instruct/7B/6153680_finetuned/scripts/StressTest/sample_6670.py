efficiency_difference_premise = 35
efficiency_difference_hypothesis = 25

# the hypothesis talks about the efficiency difference between Suresh and Kamal, which is also mentioned in the premise
if efficiency_difference_hypothesis > efficiency_difference_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
