# NEAT Python - Flappy Bird AI

This project implements an AI agent using the **NEAT (NeuroEvolution of Augmenting Topologies)** algorithm to play Flappy Bird. The AI evolves over multiple generations, improving its performance over time.

---

## 🚀 Features
- AI learns to play Flappy Bird using **Neuroevolution**.
- Uses **NEAT-Python** for evolutionary learning.
- Supports both training and loading pre-trained AI models.

---

## 🛠 Installation
### Prerequisites
Ensure you have Python installed. If not, download and install it from:
https://github.com/DilysT/Flappy_bird_NEAT-Python-.git

## ▶️ Running the AI
### 1️⃣ Training the AI from scratch
To train a new AI model, run:
```bash
python flappy_bird.py
```
The AI will evolve over multiple generations to improve its performance.
<p align="center">
  <img src="{53A78D66-4595-488A-B6DC-8D1BE2B37312}.png" width="400">
</p>

### 2️⃣ Running a test AI model
If you have already trained an AI and saved the best model to the best_genome.json, you can run it using:
```bash
python test.py
```
This will load the best-trained genome and allow it to play the game autonomously.

---

## 📁 Understanding Saved Models
### `best_genome.json`
- This file stores the best AI genome's structure in a **JSON format**.
- It allows you to analyze or modify the neural network manually if needed.

### `best.pickle`
- This file saves the **trained best genome** in a binary format.
- It is used to load and run the best-performing AI model efficiently.

---

## 📄 License
This project is open-source and available under the MIT License.

---

## 💡 Contributions
Feel free to fork, modify, and submit pull requests to improve the project!

