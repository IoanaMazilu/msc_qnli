problems_solved_premise = 70 to 125
problems_solved_hypothesis = 30 to 125

# the hypothesis refers to the range of problems solved by Andy, which is also mentioned in the premise
if problems_solved_premise <= problems_solved_hypothesis:
    # check if the range of problems solved in the premise contradicts the range of problems solved in the hypothesis
    label = "contradiction"
else:
    # if the range of problems solved in the premise does not contradict the range of problems solved in the hypothesis, we can infer entailment
    label = "entailment"

print(label)
