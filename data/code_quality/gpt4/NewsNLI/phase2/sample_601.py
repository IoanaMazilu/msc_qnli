men_charged_premise = 2
men_held_hypothesis = 2

# the hypothesis mentions the number of men held which is also referenced in the premise
# however, the hypothesis does not mention anything about the charges or the bond amount
# thus, it doesn't contradict the premise, but it cannot be fully entailed from it either
label = "neutral"

print(label)
