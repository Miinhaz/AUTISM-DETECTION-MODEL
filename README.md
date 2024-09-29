# Early Stage Autism Detection Model

### 🚀 Overview
Autism Spectrum Disorder (ASD) is a neurodevelopmental condition that can manifest in toddlers, significantly impacting communication, social interactions, and behavior. Early detection of ASD is crucial for timely interventions, improving outcomes for affected children. The **Early Stage Autism Detection Model** is a machine learning-based system designed to predict the likelihood of ASD in toddlers by analyzing responses to a series of diagnostic questions.

This project utilizes a dataset containing **10 quantitative autism checklist questions**, alongside other relevant features such as age, gender, ethnicity, and family history. The model employs various machine learning classifiers to predict ASD traits, assisting medical professionals and caregivers in identifying early signs of autism.

### 🧠 Why It’s Important
Early diagnosis of autism can lead to timely interventions, which are critical for enhancing development in children with ASD. This model offers an automated, data-driven approach to early autism detection, potentially saving time and resources for healthcare professionals. Early interventions based on reliable predictions can significantly improve social, communication, and cognitive development in children.

### ⚙️ What the Model Does
The model analyzes responses to questions like:
- Does your child look at you when you call his/her name?
- How easy is it for you to make eye contact with your child?
- Does your child point to indicate interest or to request something?

These responses, along with other demographic and health-related data, are processed using machine learning algorithms like **Logistic Regression**, **Decision Trees**, **SVM**, **Random Forest**, and more, to predict whether a child shows ASD traits.

#### Key features of the project:
- **Data Preprocessing**: Cleaning the dataset and encoding features for effective model training.
- **Model Training**: Applying various machine learning classifiers and tuning them for optimal accuracy.
- **Evaluation**: Assessing model performance based on metrics like accuracy, precision, recall, and confusion matrices.

### 📊 Dataset
The dataset comprises **1,055 cases** sourced from Kaggle, including responses to 10 autism-related questions designed for toddlers and additional features such as:
- Age in months
- Sex
- Ethnicity
- Family history of ASD
- Jaundice history
- Who completed the test

You can explore the dataset here: [Toddler Autism Dataset](https://github.com/Miinhaz/AUTISM-DETECTION-MODEL/blob/main/Toddler_Autism.csv).

### 🔬 How It Works
1. **Data Preprocessing**: The data is cleaned, unnecessary columns are removed, and categorical data is encoded for analysis.
2. **Feature Scaling**: Standardization techniques are applied to the feature set to enhance model performance.
3. **Model Training**: Multiple classifiers, including **Logistic Regression**, **Random Forest**, **SVM**, and others, are trained and tested.
4. **Evaluation**: The models are evaluated using confusion matrices and accuracy scores to identify the best performing model for detecting autism traits.

### 📈 Results
The model achieves high accuracy across different classifiers. For example:
- **Logistic Regression**: 98.7% accuracy
- **Random Forest**: 93% accuracy
- **SVM**: 96.8% accuracy

The high accuracy of these models indicates that the system can serve as a valuable tool for supporting early autism detection.

### 🌐 FastAPI & Streamlit Webpage Deployment for Instant Autism Detection

This project also features **real-time predictions** for early autism detection in toddlers through the deployment of the model using **FastAPI** and **Streamlit**. By making the model accessible on these platforms, healthcare professionals, caregivers, and parents can quickly check whether a toddler shows signs of Autism Spectrum Disorder (ASD) based on their responses to the 10-question checklist.

### ⚡ FastAPI Deployment
**FastAPI** is a modern web framework for building APIs with Python, enabling the deployment of the machine learning model through a simple API that integrates easily into various systems.

#### How It Works:
1. **Model Serialization**: The trained model is saved using **Pickle**, allowing it to be loaded for real-time predictions.
2. **API Endpoints**: FastAPI exposes an endpoint where users can input answers to the 10 autism-related questions, along with demographic details (age, gender, etc.).
3. **Instant Prediction**: Upon data submission, the API returns an instant prediction indicating whether the child has ASD traits, should be under observation, or shows no signs of autism.

#### Practical Application:
- **Healthcare Integration**: The API can be integrated into hospital systems, allowing doctors to assess toddlers during routine check-ups instantly.
- **Mobile Health Apps**: The API can serve as the backend for mobile apps, enabling parents and caregivers to check for early signs of autism from home.

---

### 📊 Streamlit Webpage Deployment
**Streamlit** is an open-source Python library that allows for rapid creation of interactive web applications. The **Streamlit Web App** developed for this project provides an easy-to-use interface for users to input their data and receive immediate results from the autism detection model.

#### How It Works:
1. **Interactive Web Interface**: Users can input answers to the 10 diagnostic questions and demographic data (age, gender, etc.) through the Streamlit app.
2. **Real-Time Results**: After submitting the data, the model processes the information and returns an instant prediction, displaying whether the child has ASD, should be monitored, or shows no signs of autism.
3. **User-Friendly Design**: The interface is designed for ease of use, ensuring that non-technical users (parents, caregivers) can navigate and assess their child's autism risk effortlessly.

#### Practical Application:
- **Remote Autism Screening**: Caregivers and parents can use the Streamlit app from anywhere, providing a convenient first step in autism screening without needing to visit a healthcare facility.
- **School Screening Tool**: The app can be employed in schools or early childhood centers for quick screenings, helping identify children who may need further evaluation or support.

### 💻 Why These Deployments Matter
The combination of **FastAPI** for backend API services and **Streamlit** for an interactive web app offers a powerful solution for real-time autism detection. This deployment provides:
- **Instant Feedback**: Quick access to predictive results can lead to faster diagnosis and intervention.
- **Accessibility**: Users can access the system from any device, whether integrated into a healthcare system or as a standalone web app.
- **Scalability**: Both FastAPI and Streamlit allow the model to handle numerous requests, making it practical for real-world applications.

By making autism detection more accessible and user-friendly, this deployment empowers early intervention, improving outcomes for children at risk of ASD.

### 📜 Full Report
For more details on the methodology, data analysis, and deployment of the model, you can refer to the full project report: [Autism Model and Deployment Report](https://github.com/Miinhaz/AUTISM-DETECTION-MODEL/blob/main/Autism%20model%20and%20deployment.pdf).

---

**Enhancing the future of autism detection through data-driven insights and accessible technology.**
