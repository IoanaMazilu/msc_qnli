overall_jobless_rate_premise = 0.23
overall_jobless_rate_hypothesis = 0.23
youth_jobless_rate_premise = 0.50

# the hypothesis mentions the overall jobless rate in Spain, which is also mentioned in the premise
# however, the hypothesis doesn't mention the youth jobless rate
if overall_jobless_rate_hypothesis != overall_jobless_rate_premise:
    # check if the overall jobless rate in the hypothesis contradicts the overall jobless rate reported in the premise
    label = "contradiction"
else:
    # if the hypothesis doesn't contradict the premise, but also doesn't mention all the data from the premise
    # we can infer neutrality
    label = "neutral"

print(label)
