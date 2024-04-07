# Premise: 5887 is divided between Shyam and Ram, such that Shyam's share at the end of 9 years is equal to Ram's share at the end of 11 years, compounded annually at the rate of 5 %.
# Hypothesis: 7887 is divided between Shyam and Ram, such that Shyam's share at the end of 9 years is equal to Ram's share at the end of 11 years, compounded annually at the rate of 5 %.
# Golden Label: contradiction

total_share_premise = 5887
total_share_hypothesis = 7887

# the hypothesis refers to the total share between Shyam and Ram as mentioned in the premise
if total_share_premise != total_share_hypothesis:
    # check if the total share in the hypothesis contradicts the total share reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

