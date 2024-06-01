## Making a Splash

Having access to clean, potable water is something that many take for granted. It is
not something that most people think about until it directly affects them. This does not
detract from the fact that water quality is an extremely important issue, and a lot of work
goes in behind the scenes to maintain water quality for large populations. If water quality
fails, it cannot only be detrimental economically, but also for the health and wellbeing of
large areas.

Data science plays a crucial role in maintaining water quality through predictive
modeling by leveraging vast amounts of data to anticipate potential issues before they
escalate. By analyzing historical water quality data along with real-time monitoring data,
data scientists can identify patterns, trends, and anomalies that may indicate deteriorating
water quality or potential contamination events. Predictive models can alert water
management authorities to take preemptive measures that will safeguard public health
and ensure access to safe drinking water. In this project I will aim to identify trends found
within water samples and train a model to predict water quality.

The dataset used in this project contains the following variables; pH, Hardness,
Solids, Chloramines, Sulfate, Conductivity, Organic Carbon, Trihalomethanes, Turbidity
and Potability. All these variables affect the quality of drinking water, firstly pH, which
refers to the acid-base balance of water. It is an important indicator of whether water is
more acidic or alkaline. Calcium hardness is caused by dissolved minerals in the water
such as calcium or magnesium salts. Total dissolved solids (TDS) refers to the total
amount of organic and inorganic particles that are found within water, the maximum
concentration of TDS in drinking water is 1000 mg/l. Chlorine and chloramine are common
disinfectants in water systems; chloramines are formed when ammonia is added to
chlorine and used to treat drinking water. Sulfate is another important variable that can
affect the taste of water and, in high concentrations, can have a laxative effect.
Conductivity measures the water's ability to conduct electric current, which correlates
with the amount of dissolved salts and inorganic materials in the water. Organic carbon in
water, often from decaying vegetation or other organic materials, can react with
disinfectants like chlorine to form potentially harmful byproducts. Trihalomethanes (THMs)
are one such byproduct, formed when chlorine reacts with natural organic matter in the
water, and they are regulated due to their potential health risks. Turbidity refers to the
cloudiness or haziness of water caused by many individual particles, which can indicate
the presence of microorganisms or other contaminants. Finally, potability indicates
whether the water is safe to drink, considering all these factors combined.

The first step once data has been obtained is to perform exploratory data analysis
(EDA). EDA can inform you a lot about your data and can be a good way to form
hypotheses. To compare the variables, I first created two new datasets, splitting the data
into two categories, potable and not potable water. Then I made a simple function that
could be used to iterate through every column in a dataset and create a histogram of that
variable. If a certain variable has a higher concentration in either set, that could indicate
that the variable in question has a stronger influence on the quality of water.

![image](https://github.com/JamesPatalan/DSC680_Portfolio/assets/101024165/88029b53-9a99-4ffc-bbb4-4bda228fba08)

The first variable that stood out is pH. For water that is safe to drink, the clear mode
pH is between 7.0 and 7.5, a pH of 7.0 is considered neutral. It should also be noted that
pH affects the effectiveness of chlorine as a disinfectant, so it would make sense that pH
plays a huge role in the potability of water. Additionally, the data seems to have a trend
where potable water seems to have a clear mode whereas not potable water the data is
less concentrated and more spread out.

![image](https://github.com/JamesPatalan/DSC680_Portfolio/assets/101024165/4032fd23-ef1c-4955-b2ba-e87434e6a533)

For this project I chose to train and evaluate three different models; logistic regression
(LR), random forest (RF) and support vector machine (svm). LR is a simple and
interpretable model that works well for binary classification problems, (potable vs not
potable water). RF is a learning method that combines multiple decision trees to improve
predictive accuracy and control overfitting. Additionally, RF provides insights into feature
importance, helping to identify key factors affecting water quality. SVM handles high
dimensional data and is a good choice for complex water quality datasets where
relationships between variables might be non-linear.

It should be noted that missing values in this dataset were treated with mean
imputation. This is replacing the missing values in a dataset with the mean value of the
available data for that variable. This method is commonly used due to its simplicity and
ease of implementation. However, it can introduce bias if missing data is not completely at
random, and may distort relationships between variables by substituting a constant value
for missing data.

The LR model exhibited an accuracy of 57.01%, demonstrating moderate
performance in classifying instances. However, its precision-recall trade-off was skewed,
with perfect precision for one class but low recall, reflecting imbalance. RF surpassed LR
with an accuracy of 64.79%, showcasing a more balanced precision-recall trade-off for
both classes. SVM emerged as the top performer, boasting an accuracy of 66.16% and
achieving a robust balance between precision and recall for both classes. Notably, SVM
showcased superior performance compared to LR and RF in all metrics, making it the
optimal choice for this dataset.

![image](https://github.com/JamesPatalan/DSC680_Portfolio/assets/101024165/53e2814e-aed6-4e82-8a02-2c80481a668a)

The above confusion matrix shows that the model prefers to predict that the water
is unsafe to drink. In real world application, I suppose that it is preferable to have an overly
cautious model than one that might sign off on drinking unsafe water.
