favorable_view_premise = 0.15
favorable_view_hypothesis = 0.10

# the hypothesis mentions the percentage of Saudis who have a favorable view of al Qaeda, which is also referenced in the premise
# however, the hypothesis refers to Saudis, while the premise refers to people who have a favorable view of al Qaeda's leader
# this is a neutral case, as the premise does not contradict the hypothesis
label = "neutral"

print(label)
