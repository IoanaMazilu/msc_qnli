# Premise: How many minutes does it take Dhoni to type less than 84 words if he types at the rate of 16 words per minute?
# Hypothesis: How many minutes does it take Dhoni to type 64 words if he types at the rate of 16 words per minute?
# Golden Label: neutral

words_premise = 84
words_hypothesis = 64
typing_rate = 16

# the hypothesis refers to the typing speed of Dhoni mentioned in the premise, and his ability to type a specific number of words
if words_hypothesis >= words_premise:
    # check if the number of words in the hypothesis contradicts the estimate of less than 'words_premise'
    label = "contradiction"
elif words_hypothesis / typing_rate != words_premise / typing_rate:
    # check if the estimated time to type 'words_hypothesis' contradicts the estimated time to type 'words_premise'
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

