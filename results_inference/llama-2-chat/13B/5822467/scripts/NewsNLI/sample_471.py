real_madrid_premise = 5
real_murcia_premise = 1

# define variables for the numerical entities in the premise and hypothesis
real_madrid_hypothesis = 5

# compare the variables
if real_madrid_hypothesis == real_madrid_premise:
    # the hypothesis mentions the same number of goals scored by Real Madrid as in the premise
    label = "neutral"
elif real_madrid_hypothesis!= real_madrid_premise:
    # check if the number of goals scored by Real Madrid in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
