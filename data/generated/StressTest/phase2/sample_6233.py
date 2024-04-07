# Premise: Bruce and Anne can clean their house in 4 hours working together at their respective constant rates.
# Hypothesis: Bruce and Anne can clean their house in 3 hours working together at their respective constant rates.
# Golden Label: contradiction

cleaning_time_premise = 4
cleaning_time_hypothesis = 3

# the hypothesis refers to the time Bruce and Anne need to clean their house, which is also mentioned in the premise
if cleaning_time_hypothesis != cleaning_time_premise:
    # check if the hypothesis contradicts the time reported in the premise
    label = "contradiction"
else:
    # if the hypothesis does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)

