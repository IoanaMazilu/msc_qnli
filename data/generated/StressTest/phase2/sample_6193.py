# Premise: Lexi got a new job that pays $less than 450 per day.
# Hypothesis: Lexi got a new job that pays $150 per day.
# Golden Label: neutral

pay_premise = 450
pay_hypothesis = 150

# the hypothesis talks about the daily pay of Lexi's new job, which is also mentioned in the premise
if pay_hypothesis >= pay_premise:
    # check if the value of 'pay_hypothesis' contradicts the premise's upper limit of 'pay_premise'
    label = "contradiction"
elif pay_hypothesis < pay_premise:
    # any pay less than 'pay_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

