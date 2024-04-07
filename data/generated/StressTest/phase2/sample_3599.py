# Premise: If Packard reads at a constant rate of 4 pages every 5 minutes, how many seconds will it take him to read N pages?
# Hypothesis: If Packard reads at a constant rate of more than 4 pages every 5 minutes, how many seconds will it take him to read N pages?
# Golden Label: contradiction

reading_rate_premise = 4
reading_rate_hypothesis = 4

# The hypothesis talks about the reading rate of Packard, which is also mentioned in the premise
if reading_rate_hypothesis > reading_rate_premise:
    # Check if the reading rate in the hypothesis contradicts the reading rate mentioned in the premise
    label = "contradiction"
elif reading_rate_hypothesis == reading_rate_premise:
    # If the reading rate in the hypothesis is the same as the premise, we can infer entailment
    label = "entailment"
else:
    # If the reading rate in the hypothesis is less than the premise, it does not contradict the premise but cannot be fully and explicitly entailed from the premise
    label = "neutral"

print(label)

