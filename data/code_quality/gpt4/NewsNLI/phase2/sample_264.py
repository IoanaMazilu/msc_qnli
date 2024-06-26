people_in_peril_premise = 1000000
people_going_hungry_hypothesis = 1000000

# the hypothesis mentions the number of people going hungry, which is also referenced in the premise
# however, the premise talks about people in peril which could mean different things and not just going hungry
# thus it's not possible to fully entail the hypothesis from the premise
label = "neutral"

print(label)
