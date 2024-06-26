# define variables with representative names for the numerical entities in both inputs
tshirt_avg_premise = float(input("Enter the average price of the t-shirts in the premise: "))
tshirt_avg_hypothesis = float(input("Enter the average price of the t-shirts in the hypothesis: "))
num_tshirts_premise = int(input("Enter the number of t-shirts in the premise: "))

# extract all quantities as valid numbers (integers or floats)
tshirt_avg_premise = float(tshirt_avg_premise)
tshirt_avg_hypothesis = float(tshirt_avg_hypothesis)
num_tshirts_premise = int(num_tshirts_premise)

# use brief comments to explain what comparison you do between the defined variables
# do not use their values in the comments
# the hypothesis refers to the number of t-shirts and the average price mentioned in the premise

# perform calculations if necessary
if tshirt_avg_hypothesis > tshirt_avg_premise:
    # check if the hypothesis value contradicts the estimate of the average price in the premise
    label = "contradiction"
elif tshirt_avg_hypothesis == tshirt_avg_premise:
    # check if the hypothesis value is consistent with the estimate of the average price in the premise
    label = "neutral"
else:
    # check if the hypothesis value contradicts the estimate of the number of t-shirts in the premise
    label = "contradiction"

# use the correct comparison operators
print(label)
