# SignSense
A robust system for detecting and interpreting sign language, enabling seamless communication between sign language users and non-users through advanced computer vision and AI technologies

## Introduction

Ensuring the safety and wellbeing of physically challenged students and children with special abilities in educational environments and workplaces is crucial. Advanced surveillance systems can help detect and prevent incidents in real-time, addressing distress and emergencies effectively. Our project focuses on using hand sign detection to provide a covert way for individuals to seek help or express discomfort. By leveraging computer vision and machine learning, these systems enable non-verbal communication in challenging situations.

Our goal is to enhance safety and communication for physically challenged students and children with special abilities by integrating hand sign detection technology. This tool allows individuals to subtly signal distress or need assistance. This README outlines how we built a hand sign detection system using Python, MediaPipe, OpenCV, and Scikit-Learn. We aim to create an accurate system that identifies hand movements linked to emergencies through data collection, pre-processing, feature extraction, and machine learning techniques.

## Methodology

### Tools and Libraries

- **OpenCV**: For computer vision tasks.
- **NumPy**: For numerical operations and array handling.
- **Pandas**: To manipulate and analyze data.
- **Scikit-Learn**: For machine learning.
- **Pickle**: For serializing and deserializing Python objects.
- **MediaPipe**: For real-time perception applications, including hand tracking.

### Process Overview

1. **Image Collection**: Collect and annotate hand sign images using OpenCV.
2. **Dataset Creation**: Use MediaPipe to detect hand landmarks and extract features.
3. **Training Classifier**: Train a machine learning model using Scikit-Learn.
4. **Model Testing**: Test the model on live video streams for real-time detection.

For image collection, we set up a directory structure to store images and captured images for each hand sign class using a webcam. In dataset creation, we used MediaPipe Hands model to detect hand landmarks, normalized them, and serialized the dataset using Pickle.

Training the classifier involved loading and splitting the dataset, training a Random-Forest classifier, evaluating its performance, and saving the trained model. For testing, we loaded the model, captured video from the webcam, detected hand landmarks, and made predictions.

By following this approach, we aim to create a sign language detection system that enhances safety and communication for physically challenged students and children with special abilities in both educational settings and workplaces.
