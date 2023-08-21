# Time Series Forecasting App with Streamlit
__________________________________________________________________

# Introduction
__________________________________________________________________
Streamlit is a freely available resource for building and launching data-driven applications, requiring less coding effort in contrast to alternative technologies such as HTML, CSS, and JavaScript. Tailored for developing data science applications, it functions as a low-code platform. Moreover, it offers the capability to deploy applications on the Streamlit community cloud and effortlessly manage them, all without any associated expenses.

Furthermore, Streamlit incorporates component-oriented features for creating data-centric applications with limited coding requirements. It also provides possibilities to establish connections with various data origins, including but not limited to AWS S3, spreadsheets, BigQuery, PostgresSQL, MS SQL Server, and more.

# Setup
_________________________________________________________________________________________________
Install the required packages to be able to run the evaluation locally.

You need to have Python3 on your system. Then you can clone this repo and being at the repo's root (root :: repo_name> ...) follow the steps below:

 - Windows:
python -m venv venv; venv\Scripts\activate; python -m pip install -q --upgrade pip; python -m pip install -qr requirements.txt

 - Linux & MacOs:
python3 -m venv venv; source venv/bin/activate; python -m pip install -q --upgrade pip; python -m pip install -qr requirements.txt

The both long command-lines have a same structure, they pipe multiple commands using the symbol ; but you may manually execute them one after another.

1. Create the Python's virtual environment that isolates the required libraries of the project to avoid conflicts;
2. Activate the Python's virtual environment so that the Python kernel & libraries will be those of the isolated environment;
3. Upgrade Pip, the installed libraries/packages manager to have the up-to-date version that will work correctly;
4. Install the required libraries/packages listed in the requirements.txt file so that it will be allow to import them into the   python's scripts and notebooks without any issue.

NB: For MacOs users, please install Xcode if you have an issue.

# 🔧 The Streamlit App
__________________________________________________________________________________________________
Utilizing the Streamlit library, we'll craft the application. This application will incorporate input features like dropdown menus, sliders, and radio buttons, designed to gather user inputs and retain them as variables. Furthermore, an output element will be established to exhibit the churn prediction produced by the machine learning model.

# 🚀 Execution
_________________________________________________________________________________________________
To Run the app: Go to your terminal and type:

| streamlit run app.py |

Executing this will launch the application and provide you with a hyperlink to open in your web browser. Simply click the link, and you're all set to proceed!