# Premise: How many minutes does it take Sharuk to type less than 65 words if he types at the rate of 5 words per minute?
# Hypothesis: How many minutes does it take Sharuk to type 25 words if he types at the rate of 5 words per minute?
# Golden Label: neutral

words_premise = 65
words_hypothesis = 25
typing_rate = 5

# the hypothesis talks about the time it would take Sharuk to type a certain number of words at a given rate, a topic also addressed in the premise
if words_hypothesis >= words_premise:
    # check if the number of words in the hypothesis contradicts the estimate of less than 'words_premise'
    label = "contradiction"
elif words_hypothesis < words_premise:
    # the premise is about the time it would take to type less than 'words_premise', so 'words_hypothesis' could be a valid number of words he might type
    # however, the premise does not explicitly state that Sharuk would type 'words_hypothesis', so it is not an entailment
    label = "neutral"

print(label)

