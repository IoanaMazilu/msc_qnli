# Premise: Lexi got a new job that pays $150 per day.
# Hypothesis: Lexi got a new job that pays $less than 450 per day.
# Golden Label: entailment

daily_pay_premise = 150
daily_pay_hypothesis = 450

# the hypothesis refers to the daily pay mentioned in the premise
if daily_pay_hypothesis < daily_pay_premise:
    # check if the value in 'daily_pay_hypothesis' contradicts the daily pay in the premise
    label = "contradiction"
elif daily_pay_premise > daily_pay_hypothesis:
    # check if the daily pay in the premise contradicts the daily pay mentioned in the hypothesis
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)

