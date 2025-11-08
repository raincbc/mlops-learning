from abc import ABC, abstractmethod
from sklearn.linear_model import LogisticRegression
from xgboost import XGBClassifier

# # 1
# class ModelInterface(ABC):
#     @abstractmethod
#     def fit(self,x,y):
#         pass
#     @abstractmethod
#     def predict(self,x):
#         self.predict(x)
#
#     @abstractmethod
#     def save(self,path):
#         self.save(path)
#
#     @abstractmethod
#     def load(self,path):
#         self.load(path)
#
#
# # 2
#
# class SklearnModel(ModelInterface):
#     def __init__(self):
#         self.model = LogisticRegression()
#
#     def fit(self, x, y):
#         self.model.fit(x, y)
#
#     def predict(self, x):
#         return self.model.predict(x)
#
#     def save(self, path):
#         import joblib
#         joblib.dump(self.model, path)
#
#     def load(self, path):
#         import joblib
#         self.model = joblib.load(path)
#
# # 3
#
# class XGBoostModel(ModelInterface):
#     def __init__(self):
#         self.model = XGBClassifier()
#
#     def fit(self, x, y):
#         self.model.fit(x, y)
#
#     def predict(self, x):
#         return self.model.predict(x)
#
#     def save(self, path):
#         self.model.save_model(path)
#
#     def load(self, path):
#         self.model.load_model(path)
#
# #4
#
# def test_model():
#     model = SklearnModel()
#     x = [[0], [1]]
#     y = [0, 1]
#     model.fit(x, y)
#
#     print("🔍 Предсказываем:")
#     print("predict([[0]]) =", model.predict([[0]]))
#     print("predict([[1]]) =", model.predict([[1]]))
#
#     assert model.predict([[0]])[0] == 0
#     assert model.predict([[1]])[1] == 1
#     model.save("sklearn_model.pkl")
#     model.load("sklearn_model.pkl")
#
# test_model()

#5

class SklearnModel:
    def fit(self, x, y):
        self.x = x
        self.y = y

    def predict(self, x):
        return [self.y[0] for _ in x]

class DataLoger:
    def load_data(self, path):
        X = [[0], [1]]
        y = [0, 1]
        return X, y


class Logger:
    def log_metrics(self, metrix):
        pass

class Notifier:
    def send_email_report(self, email):
        pass

class Trainer:
    def __init__(self, model, data_loader, logger, notifier):
        self.model = model
        self.data_loader = data_loader
        self.logger = logger
        self.notifier = notifier

    def run(self):
        X, y = self.data_loader.load_data("data.csv")
        self.model.fit(X, y)
        preds = self.model.predict(X)
        print(preds)
        self.logger.log_metrics({"accuracy": 1.0})
        self.notifier.send_email_report("admin@example.com")

trainer = Trainer(
    model=SklearnModel(),
    data_loader=DataLoger(),
    logger=Logger(),
    notifier=Notifier()
)

trainer.run()
