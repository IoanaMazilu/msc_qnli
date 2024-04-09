days_worked_premise = 5
days_worked_hypothesis = 5

# the hypothesis talks about the number of days worked together after Sushil goes away, which is also mentioned in the premise
if days_worked_hypothesis == days_worked_premise:
    # the hypothesis and premise values match, so there is entailment
    label = "entailment"
elif days_worked_hypothesis > days_worked_premise:
    # the hypothesis value exceeds the premise value, so there is entailment
    label = "entailment"
else:
    # the premise gives only an estimate for the number of days worked together, and the hypothesis value contradicts it
    label = "contradiction"

print(label)
