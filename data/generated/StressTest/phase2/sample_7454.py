# Premise: If T = 5/9 * (K-32), and if T = 105, then what is the value of K?
# Hypothesis: If T = less than 5/9 * (K-32), and if T = 105, then what is the value of K?
# Golden Label: contradiction

T_premise = 105
T_hypothesis = 105
# the formula for T in the premise and hypothesis is the same, but the hypothesis suggests a lower value for T
# this is a contradiction because the value for T is the same in both premise and hypothesis

label = "contradiction"
print(label)

