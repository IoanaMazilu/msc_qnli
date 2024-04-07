# Premise: How many minutes does it take Dhoni to type 64 words if he types at the rate of 16 words per minute?
# Hypothesis: How many minutes does it take Dhoni to type less than 84 words if he types at the rate of 16 words per minute?
# Golden Label: entailment

words_premise = 64
words_hypothesis = 84
typing_rate = 16

# the hypothesis refers to the number of words Dhoni can type, which is mentioned in the premise
# and it refers to the typing rate, which is the same in both the premise and the hypothesis
if words_hypothesis <= words_premise:
    # check if the estimate of 'words_hypothesis' contradicts the number of words in the premise
    label = "contradiction"
else:
    # the premise gives the exact time for Dhoni to type 'words_premise'
    # any number of words less than 'words_hypothesis' but more than 'words_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

