injured_police_premise = 30
injured_police_hypothesis = 30

# the hypothesis mentions the number of police officers injured, which is also mentioned in the premise
# however, the hypothesis does not mention the fact that one police officer was taken hostage, which was reported in the premise
if injured_police_hypothesis != injured_police_premise:
    # check if the number of injured police officers in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
else:
    # if the number of injured police officers in the hypothesis does not contradict the number reported in the premise, we infer neutrality. Because the hostage situation is not mentioned in the hypothesis.
    label = "neutral"

print(label)
