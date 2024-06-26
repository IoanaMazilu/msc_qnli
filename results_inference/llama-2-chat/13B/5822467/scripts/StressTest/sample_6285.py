robin_score_premise = 83
num_tests_premise = 10

# define variables for the hypothesis
robin_score_hypothesis = float(input("Enter Robin's score on a less than 70th test: "))

# check if the hypothesis value contradicts the premise value
if robin_score_hypothesis < num_tests_premise * 83 / 10:
    # the hypothesis value contradicts the premise value, so the label is contradiction
    print("contradiction")
else:
    # the hypothesis value is consistent with the premise value, so the label is neutral
    print("neutral")
