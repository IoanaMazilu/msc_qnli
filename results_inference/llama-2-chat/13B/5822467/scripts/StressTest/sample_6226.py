boys_premise = less_than_400
boys_hypothesis = 300
girls_premise = 240
girls_hypothesis = 240

# the hypothesis refers to the number of boys and girls in the senior class
if boys_hypothesis <= boys_premise and girls_hypothesis == girls_premise:
    # the hypothesis is consistent with the premise, and the number of girls is the same in both
    label = "neutral"
elif boys_hypothesis!= boys_premise:
    # the number of boys in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # the hypothesis is consistent with the premise, but we cannot infer entailment since the premise only gives an estimate
    label = "neutral"

print(label)
