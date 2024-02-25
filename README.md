# 🏥 Hospital Information System (HIS)

## 🎯 Problem Definition

In healthcare facilities, the management of patient data, clinical workflows, and administrative tasks often involves cumbersome paperwork and manual processes. These methods are prone to errors, inefficient, and can lead to delays in patient care. Furthermore, traditional systems may lack integrative features that allow for seamless communication and data retrieval among various departments. Our graduation project, the Hospital Information System (HIS), aims to address these issues by providing a centralized platform where healthcare facilities can efficiently manage all the relevant processes and ensure the delivery of timely and accurate healthcare services.

## 📋 Description

Developed as our graduation project, the Hospital Information System (HIS) is designed to streamline operations in healthcare facilities. The system integrates various modules, enabling different stakeholders including patients, doctors, receptionists, and others to efficiently manage clinical workflows and administrative tasks. 

### 🚀 Key Modules and Features

The system is structured around several key roles, each facilitated by a dedicated module designed to carry out specific functions:

- **Patient Module** 🤒:
  - **Book Appointments**: Allows patients to book, view, and manage their appointments.
  - **Medical History**: Enables patients to view their medical histories.
  - **Billing**: Lets patients view their billing details and track financial transactions.
   
- **Doctor Module** 🩺:
  - **View Appointments**: Helps doctors track their schedules.
  - **Test Requests**: Allows doctors to request tests from the laboratory and radiology departments.
  - **Prescription Requests**: Enables doctors to send prescription requests directly to the pharmacy.

- **Receptionist Module** 🛎️:
  - **Patient Registration**: Assists in the registration of new patients.
  - **Manage Appointments**: Grants the ability to view, book, and manage appointments.
  - **Test Request Confirmation**: Facilitates the confirmation or declination of test requests before they are sent to the relevant departments.

- **Pharmacy Module** 💊: 
  - A simple yet effective system to manage prescriptions sent by doctors and dispense medications accordingly.

- **Laboratory and Radiology Module** 🔬: 
  - **Handle Requests**: Processes test requests sent by doctors and uploads the results to be viewed by the necessary parties.
  
- **Medical Secretary Module** 🗃️: 
  - Takes charge of managing and organizing medical data efficiently to ensure seamless healthcare operations.
  
## 🔒 Security

In the Hospital Information System (HIS), we have instituted several security measures to safeguard sensitive data and to maintain a secure and trustworthy environment. Here are the key security features implemented in the system:

### Role-Based Access Control (RBAC)

RBAC plays a pivotal role in ensuring the integrity and security of data in the system. By defining roles based on job competencies and responsibilities (like patients, doctors, receptionists, etc.), we have created a system where access is granted according to a user’s role, effectively maintaining a secure boundary that safeguards sensitive information. Each role has distinct permissions ensuring that every user can only access the data and perform the operations that pertain to their role, thereby creating a secure and structured environment.

### Password Security

To protect user passwords from unauthorized access and potential breaches, we have employed the PBKDF2 algorithm paired with a SHA256 hash. This combination ensures a robust defense against brute-force attacks and other common password cracking methods, as it adds a computational barrier to the hashing process, thereby securing user passwords effectively.

### JSON Web Token (JWT)

Upon a successful login, a JSON Web Token (JWT) is generated for the user. JWTs are used to securely transmit information between parties in a JSON format. This security measure ensures that once a user is logged in, they can make authenticated requests to the server with a signed token, maintaining a secure session throughout their interaction with the system.

Through these security strategies, HIS establishes a secure, reliable, and user-friendly environment, where users can trust that their information is handled safely and responsibly. Implementing these security features not only helps in protecting sensitive data but also fosters trust with the users, laying a foundation for a reliable healthcare information system.



## 💻 Technologies Used
### Backend
- **Python**: Powered the server, and handled database operations.
- **Django**: Used as the backend framework to facilitate rapid development and clean design.


### 🛠️ Installation and Setup for Backend

To set up and run the backend of the Hospital Information System locally, follow the step-by-step guide below:

#### Prerequisites

- Ensure you have [Python](https://www.python.org/downloads/) (3.6 or newer) installed on your system.
- [Django](https://www.djangoproject.com/download/) (ensure to install a version compatible with your Python version).
- [pip](https://pip.pypa.io/en/stable/installing/) (Python’s package installer) should be installed.
- It is recommended to set up a [virtual environment](https://docs.python.org/3/tutorial/venv.html) for Python to manage dependencies and avoid conflicts.

#### Step 1: Clone the Repository

Open your terminal and run the following command to clone the repository:

```bash
git clone https://github.com/MahmoudAbdulfattah1/Hospital-Information-System/
```
To get started with the Hospital Information System, follow the instructions below to set up the environment and run the system on your local machine.
#### Step 2: Navigate to the Backend Directory
Change your current working directory to the backend directory of the cloned repository:
```bash
cd Hospital-Information-System/backend
```
(Replace "backend" with your actual backend directory name)

#### Step 3: Set Up a Virtual Environment (Recommended)
Set up a virtual environment to manage dependencies more effectively:
```bash
python3 -m venv venv
```
Activate the virtual environment:
- on Windows:
```bash 
.\venv\Scripts\activate
```
- on Mac:
```bash 
source venv/bin/activate
```
#### Step 4: Install the Required Dependencies
Install all the necessary dependencies using pip:
```bash
pip install -r requirements.txt
```
#### Step 5: Apply Migrations
Apply the migrations to set up your database schema:
```bash
python manage.py migrate
```
#### Step 6: Run the Server
Finally, run the server to start the application:
```bash
python manage.py runserver
```
- Your backend server should now be running locally. You can access the API endpoints through your browser or Postman using the following base URL:
```bash
http://127.0.0.1:8000/
```



## 📬 Contact

For any queries, collaborations, or feedback on the project, feel free to reach out through the following channel:

- **LinkedIn**: [Mahmoud A. Fattah](https://www.linkedin.com/in/mahmoud-a-fattah/)

Your input is highly appreciated, and we look forward to hearing from you!
