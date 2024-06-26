reward_premise = 5000
phone_number_premise = "641-228-182"

# define variables for the numerical entities in the hypothesis
reward_hypothesis = None
phone_number_hypothesis = None

# extract numerical information from the hypothesis
if reward_hypothesis is not None:
    reward_hypothesis = float(reward_hypothesis)
else:
    reward_hypothesis = None

if phone_number_hypothesis is not None:
    phone_number_hypothesis = phone_number_hypothesis.replace(" ", "")
    phone_number_hypothesis = int(phone_number_hypothesis)
else:
    phone_number_hypothesis = None

# compare the numerical entities in the premise and hypothesis
if reward_premise == reward_hypothesis:
    # the reward amounts in the premise and hypothesis are the same
    label = "entailment"
elif reward_premise!= reward_hypothesis:
    # the reward amounts in the premise and hypothesis are different
    label = "contradiction"
elif phone_number_premise == phone_number_hypothesis:
    # the phone numbers in the premise and hypothesis are the same
    label = "neutral"
else:
    # the phone numbers in the premise and hypothesis are different
    label = "neutral"

print(label)
