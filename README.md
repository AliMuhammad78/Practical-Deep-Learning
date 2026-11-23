#  Practical Deep Learning

<div align="center">

### From Neural Network Fundamentals to Computer Vision & Transfer Learning

A practical collection of Jupyter Notebooks documenting my journey through Deep Learning, mathematical foundations, neural network architectures, model optimization, and hands-on experimentation.

**Understanding the mathematics • Implementing the concepts • Learning through experimentation**

<br>

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)
![Keras](https://img.shields.io/badge/Keras-D00000?style=for-the-badge&logo=keras&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)

<br>

![GitHub repo size](https://img.shields.io/github/repo-size/AliMuhammad78/Deep-Learning-Notebooks?color=blue&style=flat-square)
![GitHub last commit](https://img.shields.io/github/last-commit/AliMuhammad78/Deep-Learning-Notebooks?style=flat-square)
![GitHub stars](https://img.shields.io/github/stars/AliMuhammad78/Deep-Learning-Notebooks?style=flat-square)

</div>

---

## 📖 About This Repository

This repository is a collection of my practical experiments, implementations, and learning notes in **Deep Learning and Neural Networks**.

After building my foundation in Machine Learning, I moved towards understanding how neural networks work, how they learn from data, and how different architectures solve different problems.

Rather than focusing only on theoretical explanations, I explored the mathematical foundations behind these concepts and implemented them using Python, TensorFlow, Keras, NumPy, and other libraries.

The notebooks cover several areas, including:

- Fundamentals of Artificial Neural Networks and Multilayer Perceptrons.
- Mathematical understanding of activation functions and neural network operations.
- Data preprocessing, normalization, and regularization.
- Model training, optimization, and performance improvement.
- Recurrent architectures, including RNN, LSTM, and GRU.
- Convolutional Neural Networks and image classification.
- Transfer Learning using pretrained models.
- Model monitoring and visualization with TensorBoard.

The repository reflects a hands-on learning process involving different datasets, experiments, model configurations, and implementation approaches.

## 🗂️ Learning Roadmap & Topics Covered

### 01. 🧠 Artificial Neural Networks (ANN) & MLP

Started with the fundamentals of neural networks and gradually explored how multiple layers work together to learn patterns from data.

**Concepts explored:**

- Biological inspiration behind Artificial Neural Networks.
- Artificial Neurons and Perceptrons.
- Input, Hidden, and Output Layers.
- Weights, Biases, and Network Architecture.
- Forward Propagation.
- Backpropagation and its mathematical intuition.
- Loss Functions and Model Training.
- Multilayer Perceptrons (MLP).
- Gradient Descent and parameter updates.

**Practical implementation:**

Built neural network models using TensorFlow and Keras, including an MLP experiment on the Tips dataset.

### 02. ⚡ Activation Functions & Their Mathematics

One of the important areas of my learning was understanding activation functions, their mathematical formulas, behavior, and role in neural networks.

Explored both linear and nonlinear activation functions and understood why nonlinear functions are essential for learning complex patterns.

| Activation Function | Key Concept |
|---|---|
| Linear | Produces a linear output |
| Binary Step | Produces a threshold-based output |
| Sigmoid | Maps values between 0 and 1 |
| Tanh | Maps values between -1 and 1 |
| ReLU | Introduces nonlinearity by removing negative values |
| Leaky ReLU | Allows a small gradient for negative inputs |
| Other ReLU Variants | Explores alternative approaches to ReLU |
| Softmax | Converts output scores into a probability distribution |

**Focus areas:**

- Mathematical formulas and graphical representations.
- Derivatives and gradients.
- Activation behavior and output ranges.
- Vanishing gradient considerations.
- Choosing suitable activation functions for different layers.
- Differences between linear and nonlinear functions.

### 03. 📊 Data Preprocessing & Regularization

Explored how data preparation and regularization techniques influence neural network training and generalization.

**Topics explored:**

- Data Cleaning and Preprocessing.
- Feature Scaling and Normalization.
- Training, Validation, and Testing Data.
- Dropout Layers.
- L1 Regularization.
- L2 Regularization.
- Batch Normalization.
- Data Augmentation.
- Underfitting and Overfitting.
- Cross-Validation.
- Hyperparameter Tuning.

**Key learning:** Understanding why a model may perform well on training data but poorly on unseen data, and exploring techniques to improve its generalization.

### 04. ⚙️ Model Training, Optimization & Callbacks

Explored the training process in TensorFlow and Keras, including optimization algorithms, training configurations, and techniques for monitoring model performance.

**Topics explored:**

- Gradient Descent.
- Adam Optimizer.
- Learning Rate and its importance.
- Loss and Accuracy Monitoring.
- Training and Validation Performance.
- Batch Size and Epochs.
- TensorFlow Callbacks.
- Early Stopping.
- Model Checkpointing.
- Model Performance Monitoring.
- TensorBoard.

**Practical focus:**

Used callbacks during model training to monitor performance, prevent unnecessary training, and save model checkpoints.

Also explored TensorBoard to visualize training metrics and understand how model performance changes across epochs.

### 05. 🔁 Recurrent Neural Networks (RNN), LSTM & GRU

Moved towards sequential neural network architectures and explored how neural networks process information where the order of data matters.

**Architectures explored:**

**Recurrent Neural Networks (RNN)**
- Basic architecture and recurrent connections.
- Hidden states and sequential information.
- Mathematical understanding of recurrent operations.
- Challenges associated with learning long-term dependencies.

**Long Short-Term Memory (LSTM)**
- LSTM architecture.
- Cell states and hidden states.
- Input, Forget, and Output Gates.
- Mathematical intuition behind gate operations.
- Understanding how LSTM handles long-term dependencies.

**Gated Recurrent Units (GRU)**
- GRU architecture.
- Update and Reset Gates.
- Mathematical foundations.
- Understanding its structure and differences from LSTM.

The main focus was understanding the mathematical foundations, architecture, and working principles of these models, along with practical exploration.

### 06. 🖼️ Convolutional Neural Networks (CNN) & Computer Vision

Explored how neural networks process images and learn visual patterns through convolutional operations.

**Concepts explored:**

- Introduction to Computer Vision.
- CNN Architecture.
- Convolution Operations.
- Filters and Feature Maps.
- Pooling Operations.
- Flattening.
- Fully Connected Layers.
- Image Classification.
- Image Preprocessing using OpenCV.
- Working with Image Datasets.

**Practical experiments:**

| Dataset | Application |
|---|---|
| MNIST | Handwritten Digit Classification |
| Fashion-MNIST | Clothing Image Classification |
| Paddy Rice Dataset | Rice Disease Classification |

Worked with image data, preprocessing, CNN-based classification, and model training using TensorFlow and Keras.

Also explored TensorFlow's official tutorials and notebooks to understand different approaches to image classification.

### 07. 🔬 Transfer Learning & Pretrained Models

Explored Transfer Learning to understand how knowledge learned by an existing model can be reused for another image classification task.

**Concepts explored:**

- Introduction to Transfer Learning.
- Pretrained Neural Networks.
- Feature Extraction.
- Fine-Tuning.
- Freezing and Unfreezing Model Layers.
- Adapting Pretrained Models to New Datasets.

**Practical experiment: MobileNetV2 + CIFAR-10**

Worked with the pretrained **MobileNetV2** architecture and explored its application to the CIFAR-10 dataset.

The experiment involved:

1. Loading and preprocessing the CIFAR-10 dataset.
2. Loading a pretrained MobileNetV2 model.
3. Preparing the model for the classification task.
4. Exploring fine-tuning and model training.
5. Evaluating the model's performance.

This provided practical exposure to using pretrained models instead of building every model from scratch.

### 08. 📈 TensorBoard & Experiment Monitoring

Explored TensorBoard as a tool for understanding and monitoring Deep Learning experiments.

**Areas explored:**

- TensorBoard Setup.
- TensorFlow Logging.
- Training and Validation Metrics.
- Loss and Accuracy Visualization.
- Tracking Model Training.
- Integration with TensorFlow Callbacks.

Used TensorBoard alongside model training to visualize learning progress and better understand training behavior.

---

## 🧪 Practical Experiments & Datasets

The following datasets were used during different learning experiments:

| Dataset | Learning Application |
|---|---|
| Tips Dataset | Regression/MLP experimentation |
| MNIST | Handwritten Digit Classification |
| Fashion-MNIST | Clothing Image Classification |
| Paddy Rice Dataset | Rice Disease Classification |
| CIFAR-10 | Transfer Learning and Image Classification |

Each experiment provided an opportunity to understand different aspects of neural network development, from data preparation to model training and evaluation.

## 🛠️ Technologies & Tools

The following technologies and libraries were used throughout the learning and experimentation process.

| Technology | Usage |
|---|---|
| Python | Core programming language |
| NumPy | Numerical operations and array manipulation |
| Pandas | Data manipulation and preprocessing |
| TensorFlow | Deep Learning framework |
| Keras | Building and training neural networks |
| OpenCV | Image processing and computer vision |
| Matplotlib | Data visualization |
| Scikit-learn | Data preprocessing and evaluation utilities |
| TensorBoard | Training visualization and experiment monitoring |
| Jupyter Notebook | Interactive development and experimentation |

## 💻 Development Environment & GPU Configuration

Most experiments were developed using Python and Jupyter Notebooks.

An important part of this journey was configuring the Deep Learning environment on Windows.

I spent considerable time troubleshooting TensorFlow installation, GPU compatibility, and environment configuration.

Since newer TensorFlow versions do not support native Windows GPU execution in the same way as older versions, I explored **WSL2 with Ubuntu** for TensorFlow GPU-based development.

This involved:

- Setting up WSL2 and Ubuntu.
- Configuring the Python environment.
- Installing TensorFlow and its dependencies.
- Troubleshooting GPU compatibility.
- Working through environment and configuration issues.

It took several days of troubleshooting, but this experience helped me understand the practical side of setting up a working Deep Learning environment.

## 📚 Learning Resources & References

Books, documentation, and learning materials played an important role in understanding both the mathematical and practical sides of Deep Learning.

### 📕 Books

**1. Deep Learning with Python — François Chollet**

A valuable resource for understanding neural networks, Deep Learning fundamentals, model development, and practical implementation with Keras.

**2. Hands-On Large Language Models — Jay Alammar & Maarten Grootendorst**

Used as a reference for exploring concepts related to modern language models and the foundations of Generative AI.

**3. Speech and Language Processing — Daniel Jurafsky & James H. Martin**

A reference for understanding concepts in Natural Language Processing and language technologies.

### 🌐 Official Documentation & Tutorials

- [TensorFlow Official Documentation](https://www.tensorflow.org/)
- [TensorFlow Tutorials & Notebooks](https://www.tensorflow.org/tutorials)
- [Keras Documentation](https://keras.io/)
- [NumPy Documentation](https://numpy.org/doc/)
- [OpenCV Documentation](https://docs.opencv.org/)

## 🎓 Acknowledgements

Learning becomes more meaningful when guided by people who can explain both the concepts and their practical applications.

I would like to express my gratitude to my instructors:

**Agha Ali Raza**

For explaining the mathematical foundations, underlying intuition, and architectures behind Deep Learning concepts, particularly CNNs and Transformers.

**Dr. Ammar Tufail**

For practical guidance on implementing Deep Learning concepts, working with CNNs, OpenCV, TensorFlow, and related coding experiments.

I am also thankful to the authors, educators, and open-source communities whose books, documentation, tutorials, and notebooks made this learning journey possible.

## 🎯 What This Repository Represents

This repository is not just a collection of notebooks. It represents my progression from understanding basic neural networks to exploring more advanced architectures and practical Deep Learning applications.

Through these experiments, I have focused on:

- Understanding the mathematics behind neural networks.
- Connecting theoretical concepts with practical implementations.
- Exploring different architectures and their working principles.
- Learning how to prepare data and improve model performance.
- Experimenting with real datasets.
- Understanding the challenges involved in training and configuring Deep Learning models.

## 🔭 What's Next?

With a stronger foundation in Deep Learning, my next focus is on exploring modern AI architectures and Generative AI.

Some of the areas I am particularly interested in are:

- **Generative AI** — Understanding how modern generative systems work.
- **Transformer Architecture** — Exploring self-attention and transformer components.
- **Encoder-Decoder Architecture** — Understanding information encoding and generation.
- **Large Language Models (LLMs)** — Exploring the foundations, architectures, and working principles of LLMs.

The goal is to build a deeper understanding of the architectures behind modern AI systems and continue progressing towards practical AI engineering.

## 🤝 Connect With Me

I am continuously learning, experimenting, and building in Artificial Intelligence, Machine Learning, and Deep Learning.

- **GitHub:** [AliMuhammad78](https://github.com/AliMuhammad78)
 

If you find this repository useful, feel free to explore the notebooks, share suggestions, or leave a ⭐.

---

<div align="center">

### 🚀 Learn the Mathematics. Understand the Architecture. Build Through Implementation.

**Keep Learning • Keep Experimenting • Keep Building**

</div>
