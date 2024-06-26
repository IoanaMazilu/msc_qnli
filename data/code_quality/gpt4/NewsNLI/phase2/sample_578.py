peacekeepers_premise = 11800
peacekeepers_hypothesis = 11800

# the hypothesis mentions the number of peacekeepers approved for deployment, which is also mentioned in the premise
# the hypothesis does not provide information about where these peacekeepers are deployed, 
# so it does not contradict the premise but it also does not fully entail it
if peacekeepers_hypothesis != peacekeepers_premise:
    # check if the number of peacekeepers in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
else:
    # if the number of peacekeepers in the hypothesis does not contradict the premise, we can infer neutrality
    label = "neutral"

print(label)