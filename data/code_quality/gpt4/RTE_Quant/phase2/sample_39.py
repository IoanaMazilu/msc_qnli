permanent_judges_premise = 15
permanent_judges_hypothesis = 15

# the hypothesis states the maximum number of judges in the ICJ
# the premise also mentions the same maximum number of judges, but adds that there can be more if the parties involved in the dispute nominate additional judges
if permanent_judges_hypothesis < permanent_judges_premise:
    # check if the number of judges in the hypothesis is less than the number of judges in the premise
    label = "contradiction"
else:
    # if the maximum number of judges in the hypothesis does not contradict the maximum number of judges in the premise, we can infer neutrality
    label = "neutral"

print(label)
