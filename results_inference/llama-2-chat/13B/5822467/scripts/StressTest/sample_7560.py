random_premise = 310
scramjet_premise = 232
both_premise = 112

random_hypothesis = 110
scramjet_hypothesis = 232
both_hypothesis = 112

# the hypothesis mentions the number of students studying random-processing methods and Scramjet rocket engines
if random_hypothesis > random_premise and scramjet_hypothesis == scramjet_premise and both_hypothesis == both_premise:
    # the hypothesis is consistent with the premise, so we can infer entailment
    label = "entailment"
elif random_hypothesis > random_premise or scramjet_hypothesis!= scramjet_premise or both_hypothesis!= both_premise:
    # the hypothesis contradicts the premise in at least one aspect
    label = "contradiction"
else:
    # the premise and hypothesis values are consistent, but we cannot explicitly entail the hypothesis from the premise
    label = "neutral"

print(label)
