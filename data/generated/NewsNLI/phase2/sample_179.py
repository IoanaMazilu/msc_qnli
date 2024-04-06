# Premise: Eighteen people were killed and 291 were wounded, the Lebanese national news agency NNA reported.
# Hypothesis: 18 killed, 291 wounded, state news says.
# Golden Label: entailment

killed_premise = 18
killed_hypothesis = 18
wounded_premise = 291
wounded_hypothesis = 291

# the hypothesis mentions the number of killed and wounded people, which is also mentioned in the premise
if killed_hypothesis != killed_premise:
    # check if the number of killed people in the hypothesis contradicts the number of killed people reported in the premise
    label = "contradiction"
elif wounded_hypothesis != wounded_premise:
    # check if the number of wounded people from the hypothesis contradicts the number of wounded people in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

