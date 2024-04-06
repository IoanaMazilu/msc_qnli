# Premise: Four other people were wounded, including Masoom Stanikzai, a key adviser to Rabbani, the police spokesman said.
# Hypothesis: Four people were wounded in the attack, a police spokesman says.
# Golden Label: entailment

wounded_people_premise = 4
wounded_people_hypothesis = 4

# the hypothesis mentions the number of wounded people, which is also referenced in the premise
if wounded_people_hypothesis != wounded_people_premise:
    # check if the number of wounded people in the hypothesis contradicts the number of wounded people in the premise
    label = "contradiction"
else:
    # if the number of wounded people in the hypothesis does not contradict the number of wounded people in the premise, we can infer entailment
    label = "entailment"

print(label)

