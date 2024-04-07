# Premise: However, after Mary and Alan eat four apples, the ratio changes to less than 5 to 2.
# Hypothesis: However, after Mary and Alan eat four apples, the ratio changes to 3 to 2.
# Golden Label: neutral

apples_eaten_premise = 4
ratio_premise = 5/2
ratio_hypothesis = 3/2

# the hypothesis talks about the ratio change after Mary and Alan eat four apples, similarly mentioned in the premise
if ratio_hypothesis >= ratio_premise:
    # check if the hypothesis value contradicts the estimate of less than 'ratio_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the ratio after eating four apples
    # any ratio less than 'ratio_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

