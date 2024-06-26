mexico_premise = 5
new_zealand_premise = 1

# compare the number of goals scored by Mexico in the premise and hypothesis
if mexico_hypothesis > mexico_premise:
    # if the number of goals scored by Mexico in the hypothesis exceeds the number of goals scored in the premise, it entails entailment
    label = "entailment"
elif mexico_hypothesis == mexico_premise:
    # if the number of goals scored by Mexico in the hypothesis matches the number of goals scored in the premise, it does not entail anything
    label = "neutral"
else:
    # if the number of goals scored by Mexico in the hypothesis is less than the number of goals scored in the premise, it contradicts the premise
    label = "contradiction"

print(label)
