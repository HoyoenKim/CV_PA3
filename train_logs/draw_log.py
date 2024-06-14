import re
import matplotlib.pyplot as plt

with open('log.txt', 'r') as file:
    text = file.read()

pattern = r"Train Loss: (\d+\.\d+), Train Per Image IOU: (\d+\.\d+), Train Dataset IOU: (\d+\.\d+)"
matches = re.findall(pattern, text)
print(matches)

pattern = r"Valid Loss: (\d+\.\d+), Valid Per Image IOU: (\d+\.\d+), Valid Dataset IOU: (\d+\.\d+)"
matches2 = re.findall(pattern, text)
print(matches2)

epochs = range(1, 41)
train_loss = [float(match[0]) for match in matches]
train_per_image_iou = [float(match[1]) for match in matches]
train_dataset_iou = [float(match[2]) for match in matches]
valid_loss = [float(match[0]) for match in matches2]
valid_per_image_iou = [float(match[1]) for match in matches2]
valid_dataset_iou = [float(match[2]) for match in matches2]

# Plotting the results
plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.plot(epochs, train_loss, label='Train Loss')
plt.title('Train Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend()

plt.subplot(2, 2, 2)
plt.plot(epochs, valid_loss, label='Valid Loss')
plt.title('Valid Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend()

plt.subplot(2, 2, 3)
plt.plot(epochs, train_per_image_iou, label='Train Per Image IOU')
plt.plot(epochs, valid_per_image_iou, label='Valid Per Image IOU')
plt.title('Train and Valid Per Image IOU')
plt.xlabel('Epoch')
plt.ylabel('IOU')
plt.legend()

plt.subplot(2, 2, 4)
plt.plot(epochs, train_dataset_iou, label='Train Dataset IOU')
plt.plot(epochs, valid_dataset_iou, label='Valid Dataset IOU')
plt.title('Train and Valid Dataset IOU')
plt.xlabel('Epoch')
plt.ylabel('IOU')
plt.legend()

plt.tight_layout()
plt.show()