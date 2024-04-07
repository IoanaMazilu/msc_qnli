# Premise: However, Jane was indisposed 4 days before the work got over.
# Hypothesis: However, Jane was indisposed more than 4 days before the work got over.
# Golden Label: contradiction

indisposed_days_premise = 4
indisposed_days_hypothesis = 4

# the hypothesis refers to the number of days Jane was indisposed before the work got over, which is also mentioned in the premise
if indisposed_days_hypothesis > indisposed_days_premise:
    # check if the hypothesis value contradicts the exact number of 'indisposed_days_premise'
    label = "contradiction"
elif indisposed_days_hypothesis < indisposed_days_premise:
    # check if the number of days in the hypothesis is less than the number of days reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

