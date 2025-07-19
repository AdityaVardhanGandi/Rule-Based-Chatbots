# Chatbot Development Repository

This repository contains three different implementations of chatbots, showcasing the evolution from simple rule-based systems to advanced machine learning-powered conversational AI.

## 📋 Table of Contents
- [Overview](#overview)
- [Chatbot Versions](#chatbot-versions)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Features](#features)
- [Contributing](#contributing)
- [Creator](#creator)

## 🤖 Overview

This project demonstrates three different approaches to building chatbots:

1. **Rule-Based Chatbot V1**: Simple keyword matching using Tkinter GUI
2. **Rule-Based Chatbot V2**: Enhanced pattern matching using NLTK
3. **Self-Learning Chatbot V1**: Neural network-based chatbot using Keras/TensorFlow

## 🚀 Chatbot Versions

### Version 1: Basic Rule-Based Chatbot
- **File**: `Rule Based ChatBot_V1.py`
- **Technology**: Python Tkinter
- **Features**: 
  - Simple GUI interface
  - Basic keyword matching
  - Hardcoded responses
  - Limited conversation capabilities

### Version 2: Enhanced Rule-Based Chatbot
- **File**: `Rule Based ChatBot_V2.py`
- **Technology**: Python NLTK
- **Features**:
  - Pattern matching with regex
  - More natural conversation flow
  - Support for variations in user input
  - Personality traits (location: Mumbai, creator: Aditya Vardhan)
  - Jokes, weather responses, and more

### Version 3: Self-Learning Chatbot
- **File**: `Self Learning Chatbots_V1.py`
- **Technology**: Python, NLTK, Keras, TensorFlow
- **Features**:
  - Neural network-based responses
  - Intent classification
  - Learns from training data
  - Advanced GUI with Tkinter
  - Extensible through JSON configuration

## 📋 Prerequisites

Before running the chatbots, ensure you have the following installed:

- Python 3.7 or higher
- Required Python packages (see Installation section)

## 🔧 Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd chatbot-repository
   ```

2. **Install required packages**:
   ```bash
   pip install nltk numpy keras tensorflow scikit-learn
   ```

3. **Download NLTK data** (for V2 and V3):
   ```python
   import nltk
   nltk.download('punkt')
   nltk.download('wordnet')
   nltk.download('stopwords')
   ```

## 🏃‍♂️ Usage

### Running Rule-Based Chatbot V1
```bash
python "Rule Based ChatBot_V1.py"
```
- A simple GUI window will open
- Type your messages and click "Send"
- Limited responses based on exact keyword matches

### Running Rule-Based Chatbot V2
```bash
python "Rule Based ChatBot_V2.py"
```
- Console-based interaction
- More sophisticated pattern matching
- Type your messages and press Enter
- Type "bye", "exit", or "quit" to end the conversation

### Running Self-Learning Chatbot V1
```bash
python "Self Learning Chatbots_V1.py"
```
**Note**: This version requires the `intents.json` file to be in the same directory.

- The script will first train the model (may take a few minutes)
- A GUI window will open after training
- More intelligent responses based on intent classification
- The model will be saved as `chatbot_model.h5` for future use

## 📁 File Structure

```
chatbot-repository/
│
├── Rule Based ChatBot_V1.py          # Basic rule-based chatbot
├── Rule Based ChatBot_V2.py          # Enhanced rule-based chatbot
├── Self Learning Chatbots_V1.py      # ML-powered chatbot
├── intents.json                      # Training data for ML chatbot
├── .gitattributes                    # Git configuration
├── Link for Reference.txt            # Reference link
└── README.md                         # This file
```

## ✨ Features

### Common Features Across All Versions:
- Interactive conversation interface
- Greeting and farewell handling
- Basic conversational responses

### Version-Specific Features:

#### V1 Features:
- Simple Tkinter GUI
- Basic text input/output
- Hardcoded response logic

#### V2 Features:
- Pattern matching with regex
- Reflections for personalized responses
- Multiple response variations
- Support for:
  - Personal information queries
  - Weather inquiries
  - Jokes and entertainment
  - Sports and entertainment preferences
  - Help and assistance

#### V3 Features:
- Neural network-based intent classification
- JSON-configurable training data
- Advanced GUI with scrolling
- Model persistence
- Support for:
  - Multiple intents and patterns
  - Emotional responses
  - Technical topics (AI, ML)
  - Time and date queries
  - Custom personality traits

## 🎯 Training Data (V3 Only)

The `intents.json` file contains training data with the following structure:
- **Intents**: Categories like greeting, goodbye, thanks, etc.
- **Patterns**: Various ways users might express the same intent
- **Responses**: Possible bot responses for each intent

### Available Intent Categories:
- Greetings and farewells
- Gratitude and politeness
- Personal information
- Help and support
- Weather and time
- Emotions and feelings
- Technology topics (AI, ML)
- Entertainment (jokes, sports)

## 🔧 Customization

### For Rule-Based Chatbots (V1 & V2):
- Modify the conditional statements or pattern-response pairs
- Add new keywords or patterns
- Customize responses

### For Self-Learning Chatbot (V3):
- Edit `intents.json` to add new intents, patterns, or responses
- Adjust neural network parameters in the code
- Modify GUI appearance and behavior

## 🐛 Troubleshooting

### Common Issues:

1. **NLTK Data Missing**:
   ```python
   import nltk
   nltk.download('all')  # Downloads all NLTK data
   ```

2. **Keras/TensorFlow Issues**:
   - Ensure compatible versions: `pip install tensorflow==2.12.0`
   - For M1 Macs: `pip install tensorflow-macos`

3. **GUI Not Appearing**:
   - Check if Tkinter is installed: `python -m tkinter`
   - On Linux: `sudo apt-get install python3-tk`

4. **Model Training Errors**:
   - Ensure `intents.json` is in the same directory
   - Check JSON formatting for syntax errors

## 🤝 Contributing

Feel free to contribute to this project by:
- Adding new intents and responses
- Improving the GUI design
- Optimizing the neural network architecture
- Adding new features or chatbot versions

## 👨‍💻 Creator

**Aditya Vardhan**
- Location: Mumbai, Maharashtra
- Created using Python, NLTK, and Machine Learning technologies

## 📚 Reference

Additional resources and inspiration: [ChatGPT Reference Link](https://chatgpt.com/share/68664848-46f8-800c-b673-7b82b7b01e9c)

---

**Note**: This repository demonstrates the progression from simple rule-based systems to machine learning-powered chatbots. Each version serves as a learning step in understanding different approaches to conversational AI development.
