# 🏗️ Classification Hub: The SAIR PyTorch Mastery Portfolio

[![PyTorch](https://img.shields.io/badge/Framework-PyTorch-EE4C2C?style=for-the-badge&logo=pytorch)](https://pytorch.org/)
[![HuggingFace](https://img.shields.io/badge/Transformers-HuggingFace-FFD21E?style=for-the-badge&logo=huggingface)](https://huggingface.co/)
[![Accuracy](https://img.shields.io/badge/Status-All%20Targets%20Exceeded-brightgreen?style=for-the-badge)](https://github.com/your-username/classification-hub)

> "A comprehensive showcase of modern Deep Learning architectures applied to five diverse data modalities. From physical rice grain measurements to identifying Quranic reciters via Mel Spectrograms."

---

## 📺 Master Project Showcase
[![Watch the Master Demo](https://img.shields.io/badge/📽️_Master_Showcase-Play_Video-blue?style=for-the-badge&logo=youtube)](demos/Master_Classification_Hub_Demo.mp4)
*A consolidated 60-second tour of all live inference demos in this portfolio.*

---

## 🚀 Mission Control: Performance Dashboard

| Project | Modality | Architecture | Target | **Actual** | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Rice Type Classifier** | 📊 Tabular | 4-Layer MLP | 92% | **99.23%** | 🏆 Mastered |
| **Animal Faces** | 🖼️ Image (Scratch) | ResNet-Style CNN | 75% | **96.47%** | 🏆 Mastered |
| **Bean Disease Detector** | 🌿 Image (Transfer) | Fine-tuned ResNet18 | 88% | **94.74%** | 🏆 Mastered |
| **Quran Reciter ID** | 🎙️ Audio | VGG-style Mel-CNN | 70% | **99.55%** | 🏆 Mastered |
| **Sarcasm Detector** | 📝 Text | DistilBERT | 82% | **91.37%** | 🏆 Mastered |

---

## 🔬 Modality Spotlights

### 📊 1. Rice Type Classifier (Tabular Data)
**The Problem:** Automated sorting of "Cammeo" and "Osmancik" rice varieties based on physical camera measurements (area, perimeter, etc.).
**The Solution:** Implemented a robust Deep Neural Network (MLP) with **StandardScaler** normalization. Normalizing features was critical as raw measurements (e.g., Area vs. Eccentricity) varied by orders of magnitude.
**The Impact:** Achieved **99.23% accuracy**, nearly eliminating sorting errors.

### 🖼️ 2. Animal Face Classifier (Custom CNN)
**The Problem:** Categorizing wildlife images (Cat, Dog, Wild) using a model built entirely from scratch—no pretrained weights allowed.
**The Solution:** Designed a custom CNN incorporating **Residual Blocks** and **Global Average Pooling**. This architecture prevented vanishing gradients and allowed the model to learn complex spatial features effectively.
**The Impact:** Surpassed the 75% target to reach **96.47% accuracy**.

### 🌿 3. Bean Leaf Disease Detector (Transfer Learning)
**The Problem:** Detecting agricultural diseases from a very small dataset of leaf images.
**The Solution:** Leveraged **Transfer Learning** with a pretrained **ResNet-18** backbone. By freezing the early feature-extraction layers and fine-tuning the final classification head, we transferred ImageNet knowledge to the specific domain of botany.
**The Impact:** **94.74% accuracy**. [📽️ View Demo Video](demos/Bean%20Leaf%20Disease%20Detector.webm)

### 🎙️ 4. Quran Reciter Identifier (Audio Classification)
**The Problem:** Identifying unique vocal profiles in audio recordings—a task where raw waves are difficult for standard CNNs to process.
**The Solution:** Transformed raw `.wav` files into **Mel Spectrograms** (2D time-frequency representations) using `librosa`. This allowed us to treat audio classification as an image recognition problem, applying a **VGG-style CNN** to the spectrograms.
**The Impact:** Exceptional **99.55% accuracy** on vocal identification. [📽️ View Demo Video](demos/Quran%20Reciter%20Identifier.webm)

### 📝 5. Sarcasm Detector (NLP Transformers)
**The Problem:** Detecting nuance and irony in news headlines to prevent the erosion of reader trust.
**The Solution:** Fine-tuned a **DistilBERT** transformer model using the HuggingFace `transformers` ecosystem. We utilized stratified sampling to handle class balance and achieved high inference speeds without sacrificing precision.
**The Impact:** **91.37% accuracy** on unseen headlines. [📽️ View Demo Video](demos/Sarcasm%20Detector%20(DistilBERT).webm)

---

## 🛠️ Engineering Standards

- **Data Integrity:** Every model was validated using a rigorous Train/Validation/Test split (typically 70/15/15).
- **Inference Ready:** All notebooks include a `Gradio` or `PIL` based live inference demo.
- **Reproducibility:** Master configurations (LR, Batch Size, Seeds) are clearly defined at the top of every notebook.

---

*SAIR PyTorch Mastery Course — Final Portfolio Project*  
🔗 **Course Origin:** [SAIR Junior Program](https://github.com/SAIR-Org/SAIR_Jr)

