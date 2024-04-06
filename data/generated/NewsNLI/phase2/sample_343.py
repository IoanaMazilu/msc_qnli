# Premise: Eight of them were still in critical condition, said Dr. Waseem Qurashi, head of the medical department at Change Square, Sanaa University.
# Hypothesis: Eight other people are still in critical condition, Dr. Waseem Qurashi says.
# Golden Label: neutral

critical_condition_premise = 8
critical_condition_hypothesis = 8

# the hypothesis mentions the number of people in critical condition, which is also mentioned in the premise
if critical_condition_hypothesis != critical_condition_premise:
    # check if the number of people in critical condition in the hypothesis contradicts the number in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

