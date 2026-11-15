# 🚀 Space Mission Design Simulator

An interactive, educational web application that allows users to design a spacecraft, manage its resources, and simulate space missions. Users can select spacecraft components, check whether their design meets mission requirements, and explore real NASA missions.

## ✨ Features

### 1. Spacecraft Design

- Select a mission and its objective.
- Choose spacecraft components:
  - Power source
  - Communication system
  - Camera
- Calculate the spacecraft's total cost, mass, and power consumption.

### 2. Resource Analysis

Evaluate your spacecraft design based on:

- **Budget:** Is the design within the available budget?
- **Mass:** Is the spacecraft within the maximum mass limit?
- **Power:** Can the selected power source support the components?
- **Design Score:** Get a score based on your spacecraft's performance.

### 3. Mission Validation

Check whether your selected components meet the requirements of your chosen mission.

The simulator checks:

- Required camera
- Required communication system
- Required power source

### 4. Mission Difficulty Levels

Choose your challenge level:

| Difficulty | Budget Limit | Mass Limit |
| ---------- | -----------: | ---------: |
| Easy       |  $10,000,000 |     500 kg |
| Medium     |   $3,000,000 |     200 kg |
| Hard       |   $2,000,000 |     150 kg |

### 5. Mission Simulation

- Launch your designed spacecraft.
- Follow the simulated launch stages.
- Receive a successful or failed mission result.
- View a mission results dashboard.

### 6. Mission History

Keep track of previous mission attempts, including:

- Mission name
- Difficulty level
- Result
- Design score
- Total cost
- Total mass
- Attempt date and time

_Mission history is stored during the current app session._

### 7. NASA Mission Explorer

Explore real-world space missions, including:

- Mars Perseverance Rover
- OSIRIS-REx
- Landsat 9
- DART

View mission objectives, destinations, launch years, spacecraft types, instruments, and source links.

### 8. Additional Features

- NASA mission comparison
- Smart mission recommendations
- Mission difficulty challenges
- Custom spacecraft vs. NASA spacecraft comparison

---

## 🛠️ Technologies Used

- **Python** – Application logic and calculations
- **Streamlit** – Interactive web interface
- **JSON** – Mission and spacecraft component data
- **Git** – Version control

---

## 📁 Project Structure

```text
Spacemissiondesignsimulator/
│
├── app.py
│
├── engine/
│   └── calculations.py
│
├── data/
│   ├── components.json
│   ├── missions.json
│   └── real_missions.json
│
├── tests/
│
├── requirements.txt
│
└── .gitignore
```

---

## ⚙️ Installation and Setup

### Prerequisites

- Python 3.10 or later
- pip

### Step 1: Clone the Repository

```bash
git clone <your-repository-url>
```

### Step 2: Navigate to the Project Folder

```bash
cd Spacemissiondesignsimulator
```

### Step 3: Create a Virtual Environment

```bash
python -m venv .venv
```

### Step 4: Activate the Virtual Environment

For Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, run:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
```

Then activate the environment again.

### Step 5: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 6: Run the Application

```bash
streamlit run app.py
```

The application will open in your browser, usually at:

```text
http://localhost:8501
```

---

## 🎮 How to Use

1. Open the application.
2. Select a space mission.
3. Choose your spacecraft components.
4. Review the resource analysis and design score.
5. Check whether your spacecraft meets the mission requirements.
6. Select a difficulty level.
7. Launch your mission simulation.
8. Review the mission results and history.
9. Explore real NASA missions and compare spacecraft designs.

---

## 🎯 Project Purpose

The goal of this project is to make basic spacecraft design concepts easier to understand through an interactive simulation.

Instead of only learning about spacecraft components theoretically, users can experiment with different designs and understand how budget, mass, power, and mission requirements affect mission success.

## ⚠️ Disclaimer

This is an educational simulation. Component costs, masses, power values, resource limits, and mission requirements are simplified illustrative values created for the simulator. They do not represent official NASA engineering specifications or actual spacecraft design requirements.
