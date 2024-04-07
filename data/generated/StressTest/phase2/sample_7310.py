# Premise: How many minutes does it take James to type 8 words if he types at the rate of 4 words per minute?
# Hypothesis: How many minutes does it take James to type less than 8 words if he types at the rate of 4 words per minute?
# Golden Label: contradiction

words_typed_premise = 8
words_typed_hypothesis = 8
typing_speed = 4

# the hypothesis and premise both refer to the number of words typed by James at a certain rate
if words_typed_hypothesis >= words_typed_premise:
    # check if the hypothesis contradicts the premise by stating that James types equal to or more than 'words_typed_premise'
    label = "contradiction"
else:
    # the hypothesis suggests James types less than 'words_typed_premise'
    # this does not contradict the premise but cannot be explicitly inferred from the premise
    label = "neutral"

print(label)

