jill_wage_premise = 6.00
jill_wage_hypothesis = 6.00
jill_tip_premise = 0.35
jill_tip_hypothesis = 0.65

# the hypothesis talks about the same wage and tip rate as the premise
if jill_wage_hypothesis == jill_wage_premise and jill_tip_hypothesis == jill_tip_premise:
    label = "entailment"
else:
    label = "contradiction"

print(label)
