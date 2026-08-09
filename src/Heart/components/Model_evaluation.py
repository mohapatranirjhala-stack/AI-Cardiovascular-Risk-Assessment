import os
from src.Heart.utils.utils import load_object
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score


class ModelEvaluation:
    def __init__(self):
        pass

    def eval_metrics(self, actual, pred):

        accuracy = accuracy_score(actual, pred)
        precision = precision_score(actual, pred)
        recall = recall_score(actual, pred)
        f1 = f1_score(actual, pred)

        return accuracy, precision, recall, f1

    def initate_model_evaluation(self, train_array, test_array):

        X_test = test_array[:, :-1]
        y_test = test_array[:, -1]

        model_path = os.path.join("Artifacts", "Model.pkl")

        model = load_object(model_path)

        prediction = model.predict(X_test)

        accuracy, precision, recall, f1 = self.eval_metrics(
            y_test,
            prediction
        )

        print("\n==============================")
        print("MODEL EVALUATION")
        print("==============================")
        print(f"Accuracy : {accuracy:.4f}")
        print(f"Precision: {precision:.4f}")
        print(f"Recall   : {recall:.4f}")
        print(f"F1 Score : {f1:.4f}")
        print("==============================")