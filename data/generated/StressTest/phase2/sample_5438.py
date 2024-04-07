# Premise: If T = 5/9 * (K-32), and if T = 50, then what is the value of K?
# Hypothesis: If T = 1/9 * (K-32), and if T = 50, then what is the value of K?
# Golden Label: contradiction

T_premise = 50
T_hypothesis = 50
K_premise = (T_premise / (5/9)) + 32
K_hypothesis = (T_hypothesis / (1/9)) + 32

# the hypothesis refers to the same variables T and K mentioned in the premise
# but with different formula for T 
if K_premise == K_hypothesis:
    # check if the calculated value of K in the premise equals the one in the hypothesis
    label = "entailment"
else:
    # if the calculated values of K are different, we have contradiction
    label = "contradiction"

print(label)

