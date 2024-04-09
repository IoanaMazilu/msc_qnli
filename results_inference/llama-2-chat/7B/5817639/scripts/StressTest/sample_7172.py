problems_premise = 70
problems_hypothesis = 40

# the hypothesis talks about the range of problems solved by Andy, which is also mentioned in the premise
if problems_hypothesis <= problems_premise:
    # check if the hypothesis value contradicts the estimate of the range of problems solved by Andy in the premise
    label = "contradiction"
elif problems_hypothesis - problems_premise > 30:
    # check if the number of problems solved by Andy in the hypothesis is more than 30 greater than the number of problems solved in the premise
    label = "entailment"
else:
    # if the hypothesis value and the estimate of the range of problems solved in the premise do not contradict each other, we can infer neutrality
    label = "neutral"

print(label)
