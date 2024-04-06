# Premise: NEW YORK (CNN) -- Twenty-four people, including eight children, were injured in an apparent gas explosion at a Harlem apartment building, the New York Fire Department said.
# Hypothesis: About 200 firefighters were at the scene in Harlem.
# Golden Label: neutral

people_injured_premise = 24
children_injured_premise = 8
firefighters_hypothesis = 200

# the hypothesis does not mention anything about the number of people or children injured, which are the only numerical values mentioned in the premise
# the hypothesis introduces the number of firefighters at the scene, which is not mentioned in the premise

label = "neutral"

print(label)

