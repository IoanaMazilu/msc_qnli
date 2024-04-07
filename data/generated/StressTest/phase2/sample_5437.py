# Premise: If T = less than 6/9 * (K-32), and if T = 50, then what is the value of K?
# Hypothesis: If T = 5/9 * (K-32), and if T = 50, then what is the value of K?
# Golden Label: neutral

T_premise = 50
T_hypothesis = 50
K_premise = (T_premise / (6/9)) + 32
K_hypothesis = (T_hypothesis / (5/9)) + 32

# the hypothesis is about the value of K when T=50, using a different formula than the one in the premise
if K_premise == K_hypothesis:
    # check if the calculated value of K in the hypothesis contradicts the calculated value of K in the premise
    label = "contradiction"
else:
    # if the calculated values of K in the premise and the hypothesis are not equal, 
    # it means the hypothesis is not contradicting the premise, but also cannot be entailed from the premise
    label = "neutral"

print(label)

