premise_earned = 210
hypothesis_earned = float(input("Enter the amount earned by Michael: "))

# the hypothesis refers to the amount earned, which is also present in the premise
if premise_earned <= hypothesis_earned:
    # check if the estimate of 'hypothesis_earned' contradicts the amount earned in the premise
    label = "contradiction"
elif hypothesis_earned > premise_earned:
    # check if the amount earned in the hypothesis contradicts the amount earned in the premise
    label = "contradiction"
else:
    # if the hypothesis value and estimate do not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
