## Pop the cork!

Within the realm of oenology, the science of wine, the fusion of technology and tradition has
given rise to a new era of analysis. Since winemakers first started crushing grapes, wine has been
evaluated by humans using our senses of sight, smell and taste. However, in our technological age
would it be possible to have a computer evaluate wine? Obviously, the computer cannot drink wine, but
it can evaluate wine using machine learning algorithms.

According to the International Organization Of Vine and Wine’s annual report, global wine sales
reached a record figure of $41.24 billion in 2022. The wine industry is huge and more popular than ever,
and as the industry continues to expand, the need for robust methodologies to dissect and comprehend
the multifaceted nature of wine becomes increasingly relevant. Which properties can lead to a
bestselling wine? Everyone's taste is subjective, but there could exist trends in acidity, sugar or alcohol
content that tend to be found in wines that are rated well by consumers.

Leveraging Python's versatility and analytical capabilities, this study combines the realms of
data science and oenology, seeking to unravel patterns, correlations, and insights that may inform the
elusive relationship between the chemical nuances of wine and its subjective customer appeal. The
dataset used in this study examines the properties of red wine from Portugal, listing the chemical
properties, as well as how its quality was rated from 0-10. It is assumed that a higher rated wine will be
more profitable.

![image](https://github.com/JamesPatalan/DSC680_Portfolio/assets/101024165/4195ef9e-81c7-4a4b-b203-27ad07758f5a)

What do all the variables in the data represent, how do they affect wine, and should they all be
included in the data? Fixed acidity refers to the total concentration of titratable acids in a wine, mainly
malic, lactic, tartaric and citric acids. Volatile acids differ from the fixed acids in that they cannot be
measured through titration (think pH color change measurement). Volatile acids must be measured
using steam distillation, and is mainly composed of formic, acetic, propionic and butyric acids. Reaching
a proper pH balance in wine is important, as too little and a wine will taste flat, but too much can cause
sourness.

Citric acid is a natural acid found in citrus fruits like lemons and oranges. In wine, it contributes
to the overall acidity, providing a crisp and refreshing taste. It is an important component for balancing
the sweetness in a wine. Speaking of sweetness, a wine’s residual sugar refers to the amount of
unfermented sugar left in the wine after fermentation is complete. It influences the sweetness of the
wine. Wines with higher residual sugar levels tend to be sweeter, while those with lower levels are drier.
Chlorides in wine are salts of hydrochloric acid. They contribute to the overall taste and can affect the
perception of bitterness.

Sulfur dioxide or SO2 is used throughout the food industry as a way to prevent oxidization. Free
sulfur refers to SO2 in wine that has not reacted yet and is still protecting the wine, as soon as the cork
comes out, that's it and the clock is ticking on shelf life. Total sulfur includes the free sulfur level as well
as bound sulfur, which is SO2 that has reacted with the chemicals in the wine and "bound" itself to the
wine, making it no longer useful for preservation. Bound sulfites greatly reduce the aromatic qualities in
wine.

Density in wine is a measure of how tightly packed the molecules are, and pH is a measure of
the acidity or basicity of a solution. Sulphates, or sulfites, are compounds containing sulfur and are often
added to wine as a preservative to prevent oxidation and bacterial spoilage. Some people have a
sensitivity or mild allergy to sulphates. Finally, alcohol content in wine is the percentage of ethanol it
contains. It is a crucial factor in determining the body, mouthfeel, and overall warmth of the wine.

## Data Preparation & Modeling

Before any analysis can be conducted on a dataset, the data must first be cleaned, and new
features should be engineered if applicable. In the wine data, the quality variable is given on a 10-point
scale, however for machine learning purposes, this must be converted to a binary variable. Using the
following function, wines rated at 7 or higher will be considered a quality wine, and will be marked as 1,
otherwise the wine will be marked as 0.

![image](https://github.com/JamesPatalan/DSC680_Portfolio/assets/101024165/9e96725d-9a30-4138-9e46-d254ae240d55)

Since total sulfur includes the free sulfur, another variable must be engineered that represents
the SO2 present in the wine. Additionally, when a wine has a high sugar content, the wine must also
have acidity to cut through the sweetness, or else the wine may come across like drinking maple syrup.
Another new variable that tracks the total acidity ratio to sweetness must be engineered as well, both
new variables are listed below.

![image](https://github.com/JamesPatalan/DSC680_Portfolio/assets/101024165/e2a1ebe8-f863-4033-b0c5-b4c7f7e97507)

There are many different Machine Learning models that exist, but the one that was chosen for
this study is the Random Forrest Regressor model. The Random Forest Regressor operates by
constructing a multitude of decision trees during training and outputs the average prediction of the
individual trees for regression problems. Each tree in the forest is built by selecting a random subset of
the features and a random subset of the training data, which introduces diversity among the trees. The
randomness and diversity in the model make Random Forest Regressor robust, capable of capturing
complex relationships in the data, and less sensitive to outliers compared to individual decision trees.
Because this model simulates human decisions, it shall be used to evaluate the wine data. When
humans evaluate wine, they make many decisions on whether or not they enjoy the wine and what
qualities stick out to them such as its sweetness, acidity, or alcohol level.

Now that the model has been trained, it must be evaluated, one common metric is the Root Mean Square Error (RMSE),
which measures the magnitude of the errors between predicted and actual values. RMSE calculates the square root of the
average of the squared differences between predicted and actual values. Lower RMSE values indicate
better model performance, as they signify smaller prediction errors. RMSE is sensitive to large errors,
making it a valuable tool for assessing the accuracy of regression models in machine learning.

![image](https://github.com/JamesPatalan/DSC680_Portfolio/assets/101024165/12750d54-c188-4420-b797-67f63f450fe3)

A RMSE of 0.2562 is a good result, indicating that the model's predictions are, on average, very
close to the actual values in the dataset. The RMSE suggests that on average the model’s predictions are
approximately 0.2562 units away from the true values. Removing the engineered values and re-testing
the model changes the RMSE to 0.2553, which suggests that removing the engineered columns did not
significantly impact the model's predictive performance.

While the low RMSE is a positive sign, this model’s readiness for deployment depends on several
factors, such as data quality. While the data that the model was trained on contains 1600 different
wines, was this robust enough for an accurate model? The model should be scaled and tested to see if it
can handle real-time predictions and scale to meet production demands. Going forward, I would
recommend experimenting with hyperparameter tuning to optimize the model further. As well as
creating a simpler model for purposes of explainability to non-technical stakeholders.

It is also worth noting that the wines contained within this dataset are all of the Portuguese
Vinho Verde varietal. As a result, the model may be unable to correctly predict the quality of other
grapes such as Malbec or Cabernet Sauvignon. Additionally, this dataset was last updated in 2017, and
consumer tastes may have changed since then. Further testing of the model with newer data may reveal
that the model must be periodically updated to remain accurate.
