# Premise: Maddie has 4 apples, if she give 2 to mike, how many does she have left?
# Hypothesis: Maddie has less than 7 apples, if she give 2 to mike, how many does she have left?
# Golden Label: entailment

apples_maddie_premise = 4
apples_given_to_mike_premise = 2
apples_maddie_hypothesis = 7
apples_given_to_mike_hypothesis = 2

# the hypothesis talks about the number of apples Maddie has and the number she gives to Mike
# both these aspects are also mentioned in the premise
if apples_maddie_premise >= apples_maddie_hypothesis:
    # check if the number of apples Maddie has according to the premise contradicts the estimate in the hypothesis
    label = "contradiction"
elif apples_given_to_mike_premise != apples_given_to_mike_hypothesis:
    # check if the number of apples Maddie gives to Mike according to the premise contradicts the number in the hypothesis
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

