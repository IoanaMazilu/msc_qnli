senior_directors_premise = 5
senior_directors_hypothesis = 5
managing_directors_premise = 6
managing_directors_hypothesis = 6

# the hypothesis refers to the number of Senior Managing Directors and Managing Directors at Goldman Limited mentioned in the premise
if senior_directors_hypothesis != senior_directors_premise:
    # check if the number of Senior Managing Directors in the hypothesis contradicts the number stated in the premise
    label = "contradiction"
elif managing_directors_hypothesis != managing_directors_premise:
    # similarly, check if the number of Managing Directors in the hypothesis contradicts the number stated in the premise
    label = "contradiction"
else:
    # the hypothesis doesn't contradict the premise, but it also doesn't provide enough information to fully entail the premise
    label = "neutral"

print(label)
