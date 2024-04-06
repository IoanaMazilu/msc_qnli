# Premise: (CNN) -- Norway's world 100-meter breaststroke champion and Olympic silver medalist Alexander Dale Oen has died suddenly at the age 26.
# Hypothesis: Norwegian swimmer Alexander Dale Oen dies suddenly at the age of 26.
# Golden Label: entailment

age_premise = 26
age_hypothesis = 26

# the hypothesis mentions the sudden death of Alexander Dale Oen at age 26, which is also mentioned in the premise
if age_hypothesis != age_premise:
    # check if the age in the hypothesis contradicts the age reported in the premise
    label = "contradiction"
else:
    # if the age in the hypothesis does not contradict the age in the premise, we can infer entailment
    label = "entailment"

print(label)

