words_premise = 8
words_hypothesis = 7
words_per_minute = 4

# The hypothesis refers to the number of words James types, which is also mentioned in the premise.
if words_hypothesis <= words_premise:
    # Check if the number of words in the hypothesis contradicts the number of words in the premise.
    label = "contradiction"
elif words_hypothesis > words_premise:
    # Check if the number of words in the hypothesis is greater than the number of words in the premise.
    label = "entailment"
else:
    # If the number of words in the hypothesis is equal to the number of words in the premise, we can infer entailment.
    label = "neutral"

print(label)
