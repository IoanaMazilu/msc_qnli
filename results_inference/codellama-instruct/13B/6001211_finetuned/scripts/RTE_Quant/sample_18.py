total_killed_premise = 70000
total_killed_hypothesis = 200000

# the hypothesis talks about the number of people killed in an air attack in the Darfur region
# the premise also mentions the number of people killed in the Darfur region
# we compare the total number of people killed in the hypothesis with the total number of people killed in the premise
if total_killed_hypothesis > total_killed_premise:
    # check if the total number of people killed in the hypothesis contradicts the total number of people killed in the premise
    label = "contradiction"
else:
    # if the total number of people killed in the hypothesis does not contradict the total number of people killed in the premise, we infer neutrality
    label = "neutral"

print(label)
