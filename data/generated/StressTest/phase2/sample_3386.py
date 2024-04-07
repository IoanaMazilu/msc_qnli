# Premise: A “ Sophie Germain ” prime is any positive prime number p for which 2 p + 1 is also prime.
# Hypothesis: A “ Sophie Germain ” prime is any positive prime number p for which more than 2 p + 1 is also prime.
# Golden Label: contradiction

p_premise = 2
p_hypothesis = 2

# the hypothesis talks about the definition of a "Sophie Germain" prime, also mentioned in the premise
# it refers to a prime number p for which a certain relation holds
if p_premise != p_hypothesis:
    # check if the relation involving p in the hypothesis contradicts the one in the premise
    label = "contradiction"
else:
    # if the relation involving p in the hypothesis does not contradict the one in the premise, we can infer entailment
    label = "entailment"

print(label)

