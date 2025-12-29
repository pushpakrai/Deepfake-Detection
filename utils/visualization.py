import cv2
import base64
import matplotlib.pyplot as plt

def image_to_base64(image):
    _, buffer = cv2.imencode('.png', image)
    return base64.b64encode(buffer).decode('utf-8')

def visualize_predictions(confidences, threshold=0.48, fake_range=(0.49, 0.51)):
    plt.plot(confidences, label="Prediction Confidence", color="blue")
    plt.axhline(y=threshold, color='red', linestyle='--', label="Threshold (Fake)")
    plt.fill_between(range(len(confidences)), fake_range[0], fake_range[1], color='yellow', alpha=0.2, label="Uncertainty Range")
    plt.title("Prediction Confidence Across Frames")
    plt.xlabel("Frame Index")
    plt.ylabel("Confidence Score")
    plt.legend()

    plot_path = "static/confidence_plot.png"
    plt.savefig(plot_path)
    plt.close()
    return plot_path
