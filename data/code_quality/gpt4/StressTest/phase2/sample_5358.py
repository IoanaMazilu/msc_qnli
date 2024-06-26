books_claire_premise = 3
books_claire_hypothesis = 1

# the hypothesis talks about the number of books Claire has, referenced also in the premise
if books_claire_premise <= books_claire_hypothesis:
    # check if the number of books Claire has in the premise contradicts the hypothesis value
    label = "contradiction"
else:
    # if the number of books Claire has in the premise does not contradict the hypothesis, then it entails it
    label = "entailment"

print(label)
