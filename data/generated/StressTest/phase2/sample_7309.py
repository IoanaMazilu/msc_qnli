# Premise: How many minutes does it take James to type more than 7 words if he types at the rate of 4 words per minute?
# Hypothesis: How many minutes does it take James to type 8 words if he types at the rate of 4 words per minute?
# Golden Label: neutral

words_premise = 7
words_hypothesis = 8

# the hypothesis refers to the number of words James types, also mentioned in the premise
if words_hypothesis <= words_premise:
    # check if the number of words in the hypothesis contradicts the premise that James types more than 'words_premise'
    label = "contradiction"
elif words_hypothesis > words_premise:
    # the premise gives only an estimate for the number of words
    # any number of words greater than 'words_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
