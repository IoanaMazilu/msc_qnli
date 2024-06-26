words_premise = 25
words_hypothesis = 65
typing_speed = 5

# the hypothesis refers to the typing speed and number of words mentioned in the premise
if (words_hypothesis / typing_speed) <= (words_premise / typing_speed):
    # check if the time required to type 'words_hypothesis' at 'typing_speed' contradicts the time required to type 'words_premise'
    label = "contradiction"
elif words_hypothesis <= words_premise:
    # check if the number of words in the hypothesis contradicts the number of words mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer neutrality
    # the premise does not provide an upper limit for the number of words Sharuk can type in a certain time
    label = "neutral"

print(label)
