animals_killed_premise = 48
animals_killed_hypothesis = 48
primates_killed_premise = 2
primates_killed_hypothesis = 2

# the hypothesis mentions the number of animals killed by law enforcement, which is also referenced in the premise
# the hypothesis also mentions the number of primates killed by other animals, which is not mentioned in the premise
if animals_killed_hypothesis!= animals_killed_premise:
    # check if the number of animals killed in the hypothesis contradicts the number of animals killed in the premise
    label = "contradiction"
elif primates_killed_hypothesis!= primates_killed_premise:
    # check if the number of primates killed from the hypothesis contradicts the number of primates killed in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer neutrality
    label = "neutral"

print(label)
