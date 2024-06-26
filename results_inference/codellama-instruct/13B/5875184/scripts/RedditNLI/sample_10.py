rupee_premise = 65.36
rupee_hypothesis = 68.19

sensex_premise = 17685.58
sensex_hypothesis = 17685.58 - 300

nifty_premise = 27
nifty_hypothesis = 28

if rupee_hypothesis < rupee_premise:
    label = "contradiction"
elif sensex_hypothesis < sensex_premise:
    label = "contradiction"
elif nifty_hypothesis < nifty_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)
