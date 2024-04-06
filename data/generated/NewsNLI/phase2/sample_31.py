# Premise: There are only three African-Americans on the 53-person police force.
# Hypothesis: Of Ferguson's 53 police officers, three are African-American.
# Golden Label: entailment

force_size_premise = 53
force_size_hypothesis = 53
african_americans_premise = 3
african_americans_hypothesis = 3

# the hypothesis mentions the size of the police force and the number of African-American officers, which are also referenced in the premise
if force_size_hypothesis != force_size_premise:
    # check if the size of the police force in the hypothesis contradicts the size of the police force reported in the premise
    label = "contradiction"
elif african_americans_hypothesis != african_americans_premise:
    # check if the number of African-American officers from the hypothesis contradicts the number of African-American officers in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

