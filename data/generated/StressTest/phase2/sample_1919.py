# Premise: In my bungalow in Bangalore I have a beautiful rose garden. The four sides of the garden are known to be 20, 16, 12 and 10 rods.
# Hypothesis: In my bungalow in Bangalore I have a beautiful rose garden. The four sides of the garden are known to be 50, 16, 12 and 10 rods.
# Golden Label: contradiction

side1_premise = 20
side2_premise = 16
side3_premise = 12
side4_premise = 10

side1_hypothesis = 50
side2_hypothesis = 16
side3_hypothesis = 12
side4_hypothesis = 10

# the hypothesis talks about the sides of the garden mentioned in the premise
if side1_hypothesis != side1_premise or side2_hypothesis != side2_premise or side3_hypothesis != side3_premise or side4_hypothesis != side4_premise:
    # check if the values of the sides of the garden in the hypothesis contradict the values reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

