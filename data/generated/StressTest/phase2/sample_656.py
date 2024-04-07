# Premise: Lee Colle insures its students for thefts up to $1000.
# Hypothesis: Lee Colle insures its students for thefts up to $3000.
# Golden Label: contradiction

insurance_premise = 1000
insurance_hypothesis = 3000

# the hypothesis mentions the insurance amount for thefts at Lee Colle, which is also mentioned in the premise
if insurance_hypothesis <= insurance_premise:
    # check if the 'insurance_hypothesis' contradicts the amount of insurance in the premise
    label = "entailment"
elif insurance_hypothesis > insurance_premise:
    # check if the 'insurance_hypothesis' contradicts the amount of insurance in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer neutral
    label = "neutral"

print(label)

