library(rpart)

data <- read.csv("Diabetes_cleaned.csv")

data$gender <- factor(data$gender)
data$hypertension <- factor(data$hypertension)
data$heart_disease <- factor(data$heart_disease)
data$diabetes <- factor(data$diabetes)

set.seed(123)

train_indices <- sample(1:nrow(data), 0.7*nrow(data))
train_data <- data[train_indices,]
test_data <- data[-train_indices,]

model <- rpart(diabetes ~ age + bmi + HbA1c_level + blood_glucose_level + gender + hypertension + heart_disease, data=train_data, method = "class")

plot(model)
text(model, use.n = TRUE, all = TRUE)

predictions <- predict(model, newdata =  test_data, type = "class")

confusion_matrix <- table(predictions, test_data$diabetes)
print(confusion_matrix)

accuracy <- sum(diag(confusion_matrix)) / sum(confusion_matrix)
print(accuracy)
