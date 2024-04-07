## Ring Ring

Customer Churn is bound to happen for any service provider, be it insurance, credit
card, or telecommunications. Customers are going to switch providers if they can get a
better deal with a different company. With this inevitability in mind, what can phone
companies do to predict when a customer is likely to leave? Could they then take
preventative measures to keep that customer? This project aims to develop a predictive
model to identify factors contributing to customer churn. By analyzing historical customer
data, the project seeks to answer questions such as what factors influence churn rates,
which demographics are more prone to churn, and how proactive retention strategies can
be implemented to reduce churn and increase customer loyalty.

The first step that I did on this project was perform some light EDA to see what the data
looked like and make initial predictions. To do this, I first created two new datasets,
splitting the data into two categories, churned customers and retained customers. Then I
made a simple function that could be used to iterate through every column in a dataset
and create a histogram of that variable. If a certain variable has a higher concentration in
either set, that could indicate that the variable in question has a stronger influence on the
decision of the customer.

![image](https://github.com/JamesPatalan/DSC680_Portfolio/assets/101024165/978f9367-f39b-435e-ab94-d7e1420e1e1b)

The first variable that caught my attention was tenure. Tenure represents the total
number of months that the customer has stayed with the company. It is not surprising that
most people tend to have a certain loyalty towards a company if they have not had any
issues with the company or service. Switching providers can be a hassle, so unless
customers are deal seeking or unhappy with the service, there is no obvious reason for
them to switch.

This factor however cannot be the only influence on the data, and often it is a
combination of factors that impact the outcome. This is where machine learning models
come in. Before a model can be trained however, the data must be cleaned slightly in order
to be better digested by the model. Dummy data, or dummy variables are numeric
representations used to incorporate categorical data into algorithms like regression
analysis or machine learning. They maintain independence between categories by
representing each category with its own binary variable, ensuring no false ordinal
relationships are introduced.

For example, in this dataset, the variable “PaperlessBilling” represents whether or
not the customer enrolls in paperless billing. Normally this column contains the values
“Yes” or “No”, however the new dummy data will split this column into
“PaperlessBilling_Yes” and “PaperlessBilling_No”, each containing a 0 or a 1, used to
represent whether the Yes or No variable was present.

Now that the data has been prepared for the models, it is time to train them. I chose
to evaluate two different models, a logistic regression and random forest model. These two
models were chosen because logistic regression is very good at predicting binary
variables, and random forest models are good at simulating human decision making.

## Evaluation

The Logistic Regression (LR) model exhibits higher accuracy at 80.7% compared to
Random Forest’s (RF) score of 77.9%. In terms of precision, LR surpasses RF for both
churn and non-churn classes, implying LR's better ability to accurately identify true
positives while minimizing false positives. LR also demonstrates superior recall for non-
churn instances but slightly lags behind RF in capturing churn cases. However, LR
achieves higher F1-scores for both classes, indicating a better balance between precision
and recall. Ultimately, while LR outperforms RF overall, the choice between the two
models should consider specific business priorities; for instance, if accurately identifying
churn cases is paramount, the RF model's slightly better recall for churn instances might
be preferred despite LR's higher overall performance.

![image](https://github.com/JamesPatalan/DSC680_Portfolio/assets/101024165/dbe1ef6c-388c-401b-82d5-831092d8b2b0)

To find which variables were the most important to each model, feature importance
must be implemented. For the RF model, the two most important variables by far were
tenure and monthly charges. Tenure was identified early in the project as an important
feature, monthly charges however represents the total dollar amount that was charged to
each customer monthly. This also makes sense as it demonstrates customers staying for
the right price or leaving due to the wrong one.

![image](https://github.com/JamesPatalan/DSC680_Portfolio/assets/101024165/87e3d19e-a386-49a9-ab8f-b8bca08f77dd)

Interestingly, the LR model identified different variables than the RF model. The LR model
identified the contract type as the variable with the greatest importance, specifically
customers on a monthly contract. The model also identified customers on two year
contracts to have negative importance, which is interesting. The month to month customer
bracket would make sense to have a high amount of churn because they are not locked in
for any set amount of time and could leave at any notice. The next most important factor in
the LR model, turned out to be whether or not the customer has home internet service
through the provider. Home internet service is not something people switch all the time,
and often those outside the city are stuck with one option.

While the LR model surpasses the RF model for both churn and non-churn customer groups, the
highest accuracy achieved was 81% which is far from perfect. Also the scores on both models
for churned customers were poor, which indicated that there are outside factors influencing
churn that are not contained within the data, such as customers seeking a promotion or switching
due to bad experience. These findings underscore the complex relationship between variables that
contribute to customer churn.
