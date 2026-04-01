import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

data = pd.DataFrame({
    "study_hours": [2,3,4,5,6,7,8],
    "sleep_hours": [6,7,6,8,7,8,7],
    "screen_time": [5,4,6,3,2,2,1],
    "break_time": [2,2,3,2,1,1,1],
    "productivity": [50,60,55,75,85,90,95]
})

X = data[["study_hours", "sleep_hours", "screen_time", "break_time"]]
y = data["productivity"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = LinearRegression()
model.fit(X_train, y_train)

print("\nEnter your daily habits:\n")
study = float(input("Study hours: "))
sleep = float(input("Sleep hours: "))
screen = float(input("Screen time: "))
break_time = float(input("Break time: "))

pred = model.predict([[study, sleep, screen, break_time]])
score = pred[0]

print("\nYour Productivity Score:", round(score, 2))

print("\nSuggestions:")

if study < 4:
    print("- Increase study hours for better productivity")

if sleep < 6:
    print("- Get more sleep (at least 6-8 hours)")

if screen > 4:
    print("- Reduce screen time to avoid distractions")

if break_time > 3:
    print("- Optimize break time")

if score > 85:
    print("- Excellent productivity! Keep it up ")
elif score > 65:
    print("- Good, but can improve ")
else:
    print("- Needs improvement ")