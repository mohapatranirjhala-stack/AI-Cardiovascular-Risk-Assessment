import os
import uuid

import shap
import numpy as np
import matplotlib.pyplot as plt

from src.Heart.utils.utils import load_object


class SHAPExplainer:

    def __init__(self):

        model_path = os.path.join("Artifacts", "Model.pkl")
        self.model = load_object(model_path)

    def generate_explanation(self, input_dataframe):

        explainer = shap.TreeExplainer(self.model)

        shap_values = explainer.shap_values(input_dataframe)

        # -----------------------------
        # Handle SHAP output for different versions
        # -----------------------------

        if isinstance(shap_values, list):
            values = shap_values[1][0]

        else:

            if len(shap_values.shape) == 3:
                values = shap_values[0, :, 1]

            elif len(shap_values.shape) == 2:
                values = shap_values[0]

            else:
                values = shap_values

        feature_names = list(input_dataframe.columns)
        feature_values = input_dataframe.iloc[0].values

        expected_value = explainer.expected_value

        if isinstance(expected_value, (list, np.ndarray)):
            expected_value = expected_value[1]

        explanation = shap.Explanation(
            values=values,
            base_values=expected_value,
            data=feature_values,
            feature_names=feature_names
        )

        # -----------------------------
        # Save Waterfall Plot
        # -----------------------------

        filename = f"shap_{uuid.uuid4().hex}.png"

        output_path = os.path.join(
            "static",
            filename
        )

        plt.figure(figsize=(10, 6))

        shap.plots.waterfall(
            explanation,
            max_display=5,
            show=False
        )

        plt.tight_layout()

        plt.savefig(
            output_path,
            dpi=300,
            bbox_inches="tight"
        )

        plt.close()

        # -----------------------------
        # Top Feature Ranking
        # -----------------------------

        importance = np.abs(values)

        sorted_idx = np.argsort(importance)[::-1]

        top_features = []

        for idx in sorted_idx[:5]:

            impact = float(values[idx])

            if impact >= 0:
                direction = "Increased Risk"
            else:
                direction = "Reduced Risk"

            top_features.append(
                {
                    "feature": feature_names[idx],
                    "value": round(float(feature_values[idx]), 2),
                    "impact": round(impact, 3),
                    "direction": direction
                }
            )

        return {
            "image": filename,
            "top_features": top_features
        }