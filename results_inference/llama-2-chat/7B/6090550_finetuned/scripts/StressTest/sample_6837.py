 number_earned_premise = 9000
number_earned_hypothesis = 4000

# the hypothesis refers to the number of dollars earned by John and Rick at the end of a year
if number_earned_premise <= number_earned_hypothesis:
    # check if the number of dollars earned in the premise contradicts the hypothesis
    label = "contradiction"
else:
    # if the number of dollars earned in the premise is greater than the hypothesis, we can infer entailment
    label = "entailment"

print(label)
