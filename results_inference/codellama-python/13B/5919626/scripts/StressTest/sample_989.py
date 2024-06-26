seniors_morse_premise = 300
seniors_morse_hypothesis = 300
cars_morse_premise = 0.5
cars_morse_hypothesis = 0.5

# the hypothesis talks about the number of seniors in a school, referenced also in the premise
if seniors_morse_hypothesis <= seniors_morse_premise:
    # check if the hypothesis value contradicts the estimate of more than'seniors_morse_premise'
    label = "contradiction"
elif cars_morse_hypothesis!= cars_morse_premise:
    # check if the number of cars in the hypothesis contradicts the number of cars reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
