toy_trucks_premise = 8
toy_trucks_hypothesis = 5

# the hypothesis talks about the number of toy trucks Rob has, referenced also in the premise
if toy_trucks_premise <= toy_trucks_hypothesis:
    # check if the number of trucks in the premise contradicts the hypothesis
    label = "contradiction"
else:
    # if the number of trucks in the premise does not contradict the hypothesis, we can infer entailment
    label = "entailment"

print(label)
