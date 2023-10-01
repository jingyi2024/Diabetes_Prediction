library(dplyr)

data <- read.csv("Diabetes_cleaned.csv")

data$gender <- factor(data$gender)
data$hypertension <- factor(data$hypertension)
data$heart_disease <- factor(data$heart_disease)
data$diabetes <- factor(data$diabetes)

set.seed(123)

train_indices <- sample(1:nrow(data), 0.7*nrow(data))
train_data <- data[train_indices,]
test_data <- data[-train_indices,]

model <- glm(diabetes ~ age + bmi + HbA1c_level + blood_glucose_level + gender + hypertension + heart_disease, data=train_data, family = binomial)

predictions <- predict(model, newdata = test_data)

predicted_classes <- ifelse(predictions > 0.5, 1, 0)

actual_classes <- test_data$diabetes

accuracy <- mean(predicted_classes == actual_classes)

print(accuracy)

coefficients <- coef(model)
print(coefficients)

library(caret)

levels(predicted_classes)
levels(actual_classes)

predicted_classes <- factor(predicted_classes, levels = c(1,0))
confusion_matrix <- confusionMatrix(predicted_classes, actual_classes)
print(confusion_matrix)

library(pROC)

roc_curve <- roc(test_data$diabetes, predictions)
plot(roc_curve, main = "ROC Curve", print.thres = 0.5)

