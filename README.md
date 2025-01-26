# Water Quality Prediction Application

---

This project is a Streamlit-based web application that predicts the potability of water based on various water quality parameters. It uses machine learning algorithms, particularly the XGBoost Classifier, to determine whether the water is safe for drinking.

# Screenshot

![img_alt](https://github.com/vinutmaradur/Water_Quality_Test/blob/main/wp%201.png?raw=true)
![img alt]()

# Features

- **Interactive User Interface**: Users can input water quality parameters and get predictions on water potability.
- **Machine Learning Model**: A trained XGBoost model is used to classify water as potable or non-potable.
- **Dataset Handling**: The app preprocesses the water potability dataset to handle missing values before training the model.

---

# Tech Stack
- Python
- Streamlit
- Pandas
- NumPy
- Scikit-learn
- XGBoost

---

# Installation and Setup
  1. Clone the Repository
  ```bash
  git clone https://github.com/your-username/your-repo-name.git  
  cd your-repo-name
  ```
  2. Install Dependencies
   Make sure you have Python 3.8 or higher installed. Run the following command to install the required Python libraries:
   ```bash
       pip install -r requirements.txt
   ```
   Example requirements.txt
   ```bash
     streamlit  
     pandas  
     numpy  
     scikit-learn  
     xgboost
   ```
   3. Prepare the Dataset
    - Place the water_potability.csv dataset in the project root directory.
   4. Run the Application
   Start the Streamlit app by running:
    ```bash
       streamlit run app.py  
    ```
   5. Access the Application
   Open your web browser and navigate to http://localhost:8501 to interact with the app.

  ---

 # Usage
 
1. Launch the app and input the following water parameters:
- pH Value
- Hardness
- Solids (mg/L)
- Chloramines (mg/L)
- Sulfate (mg/L)
- Conductivity (μS/cm)
- Organic Carbon (mg/L)
- Trihalomethanes (μg/L)
- Turbidity (NTU)
2. Click on the "Predict Water Quality" button.
3. The app will display whether the water is Potable or Not Potable based on the input parameters.

---

# File Structure
```bash
  ├── app.py                  # Main application script  
  ├── water_potability.csv    # Dataset (to be added manually)  
  ├── requirements.txt        # Dependency list  
  └── README.md               # Project documentation
 ```

 ---

 # Contributing
  
   Contributions are welcome! Feel free to submit a pull request or report issues.

 ---

# License

  This project is licensed under the MIT License.



 
