
import streamlit as st
import time
from datetime import datetime

from engine.calculations import (
    calculate_resources,
    validate_resources,
    validate_mission,
    MAX_BUDGET,
    MAX_MASS
)

import json
from pathlib import Path

# Load real NASA missions
REAL_MISSIONS_FILE = (
    Path(__file__).resolve().parent
    / "data"
    / "real_missions.json"
)

with open(REAL_MISSIONS_FILE, "r") as file:
    REAL_MISSIONS = json.load(file)


# Page settings
st.set_page_config(
    page_title="Mission Control",
    page_icon="🚀",
    layout="wide"
)

# Main heading
st.title("🚀 Mission Control")
st.subheader("Space Mission Design Simulator")

st.write(
    "Design your spacecraft, manage resources, "
    "and launch your own space mission!"
)

st.divider()

# Mission selection
st.header("1. Select Your Mission")

mission = st.selectbox(
    "Choose the mission you want to perform:",
    [
        "Earth Observation",
        "Mars Exploration",
        "Asteroid Monitoring"
    ]
)

# Mission objectives
mission_details = {
    "Earth Observation": (
        "Observe Earth and collect images and environmental data."
    ),
    "Mars Exploration": (
        "Explore Mars and collect scientific information."
    ),
    "Asteroid Monitoring": (
        "Monitor an asteroid and collect information about its properties."
    )
}

st.write("**Mission Objective:**")
st.info(mission_details[mission])

st.divider()

# Available resources
st.header("2. Available Resources")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Budget", "$10 Million")

with col2:
    st.metric("Maximum Spacecraft Mass", "500 kg")

with col3:
    st.metric("Available Power", "1000 W")

st.divider()

st.success("Mission selected! You are ready to design your spacecraft.")


st.divider()

st.header("3. Design Your Spacecraft")

st.write("Choose the components for your spacecraft.")

# Power source
st.subheader("Power Source")

power_source = st.selectbox(
    "Choose a power source:",
    ["Solar Panels", "Radioisotope Power System"]
)

# Communication system
st.subheader("Communication System")

communication = st.selectbox(
    "Choose a communication system:",
    ["Low Gain Antenna", "High Gain Antenna"]
)

# Camera
st.subheader("Scientific Equipment")

camera = st.selectbox(
    "Choose scientific equipment:",
    ["Basic Camera", "High Resolution Camera", "Thermal Camera"]
)

st.divider()

## selcted compnenets
st.subheader("Your Selected Components")

st.write("Power Source:", power_source)
st.write("Communication:", communication)
st.write("Scientific Equipment:", camera)

 


# Calculate spacecraft resources

st.divider()
st.header("4. Spacecraft Resource Analysis")

resources = calculate_resources(
    power_source,
    communication,
    camera
)

validation = validate_resources(resources)



# --------------------------------
# SPACECRAFT DESIGN SCORING SYSTEM
# --------------------------------

st.divider()

st.header("6. Spacecraft Design Score")

# 1. Budget efficiency (25 points)

budget_score = max(
    0,
    25 * (1 - resources["total_cost"] / MAX_BUDGET)
)

# 2. Mass efficiency (25 points)

mass_score = max(
    0,
    25 * (1 - resources["total_mass"] / MAX_MASS)
)

# 3. Power adequacy (25 points)

if validation["power_ok"]:
    power_score = 25

elif resources["power_used"] > 0:
    power_score = max(
        0,
        25 * resources["available_power"] /
        resources["power_used"]
    )

else:
    power_score = 25

# 4. Mission readiness (25 points)

if validation["mission_ready"]:
    readiness_score = 25
else:
    readiness_score = 0

# Calculate final score

total_score = round(
    budget_score +
    mass_score +
    power_score +
    readiness_score
)

# Display final score

st.subheader("Your Spacecraft Performance")

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "Total Design Score",
        f"{total_score}/100"
    )

with col2:

    if total_score >= 80:
        st.success("Excellent spacecraft design!")

    elif total_score >= 60:
        st.info("Good design, but some improvements are possible.")

    elif total_score >= 40:
        st.warning("Your spacecraft needs improvement.")

    else:
        st.error("Your spacecraft design needs major improvements.")

# Display individual scores

st.subheader("Score Breakdown")

score_details = {
    "Budget Efficiency": budget_score,
    "Mass Efficiency": mass_score,
    "Power Adequacy": power_score,
    "Mission Readiness": readiness_score
}

for category, score in score_details.items():

    st.write(f"**{category}:** {round(score, 1)}/25")

    st.progress(
        min(1.0, max(0.0, score / 25))
    )

# Display resource information

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Cost", f"${resources['total_cost']:,}")

with col2:
    st.metric("Total Mass", f"{resources['total_mass']} kg")

with col3:
    st.metric("Power Available", f"{resources['available_power']} W")

with col4:
    st.metric("Power Used", f"{resources['power_used']} W")

st.divider()

# Validate spacecraft design

st.header("5. Mission Requirements Check")

if validation["budget_ok"]:
    st.success("Budget requirement satisfied!")
else:
    st.error("Budget exceeded!")

if validation["mass_ok"]:
    st.success("Spacecraft mass requirement satisfied!")
else:
    st.error("Spacecraft is too heavy!")

if validation["power_ok"]:
    st.success("Power requirement satisfied!")
else:
    st.error("Insufficient power!")

st.divider()

if validation["mission_ready"]:
    st.success("🚀 Spacecraft is ready for the next stage!")
else:
    st.error("Your spacecraft needs improvements before launch.")



# --------------------------------
# REAL NASA MISSIONS EXPLORER
# --------------------------------

st.divider()

st.title("Real NASA Missions 🚀")

st.write(
    "Explore actual space missions and learn about "
    "their objectives, spacecraft, and scientific instruments."
)

selected_real_mission = st.selectbox(
    "Choose a NASA Mission",
    list(REAL_MISSIONS.keys())
)

real_mission_details = REAL_MISSIONS[selected_real_mission]

st.subheader(selected_real_mission)

col1, col2 = st.columns(2)
with col1:
    st.metric("Launch Year", real_mission_details["launch_year"])
    st.write("**Agency:**", real_mission_details["agency"])

with col2:
    st.write("**Destination:**", real_mission_details["destination"])
    st.write("**Spacecraft Type:**", real_mission_details["spacecraft_type"])

st.write("### Mission Objective")
st.write(real_mission_details["objective"])

st.write("### Scientific Instruments")

for instrument in real_mission_details["instruments"]:
    st.write("🔹", instrument)

st.link_button(
    "Explore Official Mission Information",
    real_mission_details["source"]
)

# --------------------------------
# SMART NASA MISSION COMPARISON
# --------------------------------

st.divider()

st.title("NASA Mission Comparison 🔍")

st.write(
    "Compare two real NASA missions and discover "
    "their similarities and differences."
)

# Get all mission names from JSON

mission_names = list(REAL_MISSIONS.keys())

# Select two missions

col1, col2 = st.columns(2)

with col1:
    mission_1 = st.selectbox(
        "Select First Mission",
        mission_names,
        key="mission_1"
    )

with col2:
    mission_2 = st.selectbox(
        "Select Second Mission",
        mission_names,
        index=1 if len(mission_names) > 1 else 0,
        key="mission_2"
    )

# Retrieve mission information

mission_1_data = REAL_MISSIONS[mission_1]
mission_2_data = REAL_MISSIONS[mission_2]

st.divider()

if mission_1 == mission_2:

    st.warning(
        "Please select two different missions to compare."
    )

else:

    # --------------------------------
    # 1. BASIC MISSION COMPARISON
    # --------------------------------

    st.header("1. Mission Overview")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader(mission_1)
        st.write("**Destination:**", mission_1_data["destination"])
        st.write("**Launch Year:**", mission_1_data["launch_year"])
        st.write("**Spacecraft:**", mission_1_data["spacecraft_type"])

    with col2:
        st.subheader(mission_2)
        st.write("**Destination:**", mission_2_data["destination"])
        st.write("**Launch Year:**", mission_2_data["launch_year"])
        st.write("**Spacecraft:**", mission_2_data["spacecraft_type"])

    st.divider()

    # --------------------------------
    # 2. LAUNCH YEAR ANALYSIS
    # --------------------------------

    st.header("2. Launch Year Analysis")

    year_1 = mission_1_data["launch_year"]
    year_2 = mission_2_data["launch_year"]

    if year_1 < year_2:

        st.info(
            f"{mission_1} launched earlier than {mission_2} "
            f"by {year_2 - year_1} years."
        )

    elif year_2 < year_1:

        st.info(
            f"{mission_2} launched earlier than {mission_1} "
            f"by {year_1 - year_2} years."
        )

    else:

        st.info("Both missions launched in the same year.")

    # --------------------------------
    # 3. INSTRUMENT COUNT ANALYSIS
    # --------------------------------

    st.header("3. Scientific Instruments Analysis")

    instruments_1 = mission_1_data["instruments"]
    instruments_2 = mission_2_data["instruments"]

    count_1 = len(instruments_1)
    count_2 = len(instruments_2)

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            f"{mission_1} Instruments",
            count_1
        )

    with col2:
        st.metric(
            f"{mission_2} Instruments",
            count_2
        )

    if count_1 > count_2:

        st.success(f"{mission_1} has more listed instruments.")

    elif count_2 > count_1:

        st.success(f"{mission_2} has more listed instruments.")

    else:

        st.info("Both missions have the same number of listed instruments.")

    st.caption(
        "Instrument counts are based on the instruments listed "
        "in our project database, not necessarily every instrument "
        "carried by each spacecraft."
    )

    st.divider()

    # --------------------------------
    # 4. COMMON INSTRUMENTS
    # --------------------------------

    st.header("4. Common Instruments")

    common_instruments = set(instruments_1).intersection(
        set(instruments_2)
    )

    if common_instruments:

        for instrument in sorted(common_instruments):
            st.write("🔹", instrument)

    else:

        st.info("No common instruments are listed for these missions.")

    st.divider()

    # --------------------------------
    # 5. UNIQUE INSTRUMENTS
    # --------------------------------

    st.header("5. Unique Instruments")

    unique_1 = set(instruments_1) - set(instruments_2)
    unique_2 = set(instruments_2) - set(instruments_1)

    col1, col2 = st.columns(2)

    with col1:

        st.subheader(mission_1)

        if unique_1:

            for instrument in sorted(unique_1):
                st.write("🔹", instrument)

        else:

            st.write("No unique listed instruments.")

    with col2:

        st.subheader(mission_2)

        if unique_2:

            for instrument in sorted(unique_2):
                st.write("🔹", instrument)

        else:

            st.write("No unique listed instruments.")

    st.divider()

    # --------------------------------
    # 6. MISSION OBJECTIVE COMPARISON
    # --------------------------------

    st.header("6. Mission Objectives")

    col1, col2 = st.columns(2)

    with col1:

        st.subheader(mission_1)
        st.write(mission_1_data["objective"])

    with col2:

        st.subheader(mission_2)
        st.write(mission_2_data["objective"])

    st.caption(
        "Compare the objectives to understand how the "
        "scientific goals of the two missions differ."
    )


# ==========================================
# MISSION DIFFICULTY LEVELS
# ==========================================

st.divider()
st.header("🎮 Select Mission Difficulty")

difficulty = st.selectbox(
    "Choose your challenge level:",
    ["Easy", "Medium", "Hard"]
)

difficulty_limits = {
    "Easy": {
        "budget": 10_000_000,
        "mass": 500,
        "description": "Beginner level: generous resource limits."
    },
    "Medium": {
        "budget": 3_000_000,
        "mass": 200,
        "description": "Intermediate level: manage your resources carefully."
    },
    "Hard": {
        "budget": 2_000_000,
        "mass": 150,
        "description": "Expert level: build a spacecraft with very limited resources."
    }
}

st.info(difficulty_limits[difficulty]["description"])




# ==========================================
# MISSION SIMULATION ENGINE
# ==========================================

st.divider()

st.header("🚀 Mission Control: Launch Simulation")

st.write(
    "Your spacecraft design is complete. "
    "Now it's time to simulate your mission!"
)

# Check whether the selected components suit the mission
mission_validation = validate_mission(
    mission,
    power_source,
    communication,
    camera
)
if "mission_history" not in st.session_state:
    st.session_state.mission_history = []

if st.button("🚀 Launch Mission", type="primary"):
    simulation_resources = calculate_resources(
        power_source,
        communication,
        camera
    )

    difficulty_ready = (
        simulation_resources["total_cost"]
        <= difficulty_limits[difficulty]["budget"]
        and
        simulation_resources["total_mass"]
        <= difficulty_limits[difficulty]["mass"]
    )

    # Check resource requirements and mission suitability
    if (
    
        validation["mission_ready"]
        and mission_validation["mission_suitable"]
        and difficulty_ready
):
        st.success("All systems checked. Mission approved!")

        progress_bar = st.progress(0)
        status_text = st.empty()

        stages = [
            ("1/5: Pre-launch system check", 20),
            ("2/5: Rocket launching...", 40),
            ("3/5: Spacecraft travelling...", 60),
            ("4/5: Reaching mission destination...", 80),
            ("5/5: Mission operations completed!", 100)
        ]

        for stage, progress in stages:
            status_text.info(stage)
            progress_bar.progress(progress)
            time.sleep(1)

        status_text.success("Mission successfully completed!")
        st.balloons()

        st.subheader("📊 Mission Results Dashboard")

        st.write("**Difficulty Level:**", difficulty)
        
        col1, col2, col3 = st.columns(3)

        with col1:
           st.metric("Design Score", f"{total_score}/100")
        
        with col2:
            st.metric(
                "Total Cost",
                f"${resources['total_cost']:,}"
            )

        with col3:
            st.metric(
                "Spacecraft Mass",
                f"{resources['total_mass']} kg"
            )

        st.divider()

        st.write("### ⚡ Power Performance")

        power_percentage = (
            resources["power_used"]
            / resources["available_power"]
        ) * 100

        st.write(f"Power consumption: {power_percentage:.1f}%")

        st.progress(min(power_percentage / 100, 1.0))

        st.write("### Mission Summary")

        st.write("**Mission:**", mission)
        st.write("**Power Source:**", power_source)
        st.write("**Communication:**", communication)
        st.write("**Scientific Equipment:**", camera)

        st.success(
            "Congratulations! Your spacecraft completed "
            "the simulated mission."
        )
        st.session_state.mission_history.append({
    "Mission": mission,
    "Difficulty": difficulty,
    "Result": "Successful",
    "Score": total_score,
    "Cost": resources["total_cost"],
    "Mass": resources["total_mass"],
    "Time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
})

    else:
        st.error("🚨 Mission Launch Failed!")

        st.subheader("Mission Failure Analysis")

        problems = []

        if not validation["budget_ok"]:
            problems.append(
                "Budget exceeded! Reduce the cost of your components."
            )

        if not validation["mass_ok"]:
            problems.append(
                "Spacecraft is too heavy! Choose lighter components."
            )

        if not validation["power_ok"]:
            problems.append(
                "Insufficient power! Select a stronger power source "
                "or reduce power-consuming equipment."
            )

        if not mission_validation["camera_ok"]:
            problems.append(
                "Incorrect scientific equipment! Choose the camera "
                "required for this mission."
            )

        if not mission_validation["communication_ok"]:
            problems.append(
                "Incorrect communication system! Choose the required antenna."
            )

        if not mission_validation["power_source_ok"]:
            problems.append(
                "Incorrect power source! Choose the required power source."
            )
        if simulation_resources["total_cost"] > difficulty_limits[difficulty]["budget"]:
            problems.append(
                f"Budget exceeds the {difficulty} difficulty limit!"
            )

        if simulation_resources["total_mass"] > difficulty_limits[difficulty]["mass"]:
            problems.append(
                f"Spacecraft mass exceeds the {difficulty} difficulty limit!"
            )
        for problem in problems:
            st.warning("⚠️ " + problem)

        st.session_state.mission_history.append({
    "Mission": mission,
    "Difficulty": difficulty,
    "Result": "Failed",
    "Score": total_score,
    "Cost": resources["total_cost"],
    "Mass": resources["total_mass"],
    "Time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
})    

        st.info(
            "Go back to the Spacecraft Designer, correct the components, "
            "and try launching again."
        )


# ==========================================
# MISSION HISTORY SYSTEM
# ==========================================

st.divider()

st.header("📜 Mission History")

if st.session_state.mission_history:

    st.write("Your previous mission launch attempts:")

    st.dataframe(
        st.session_state.mission_history,
        use_container_width=True
    )

else:

    st.info("No mission attempts recorded yet. Launch your first mission!")
    

# ==========================================
# SMART MISSION RECOMMENDATION SYSTEM
# ==========================================

st.divider()

st.header("🧠 Smart Mission Recommendations")

st.write(
    "Get component recommendations based on your "
    "selected mission."
)

recommendations = {
    "Earth Observation": {
        "power": "Solar Panels",
        "communication": "Low Gain Antenna",
        "camera": "High Resolution Camera",
        "reason": "Solar panels provide power, the low gain antenna "
                  "supports communication, and the high resolution "
                  "camera helps capture detailed Earth images."
    },

    "Mars Exploration": {
        "power": "Radioisotope Power System",
        "communication": "High Gain Antenna",
        "camera": "Thermal Camera",
        "reason": "The radioisotope power system provides power, "
                  "the high gain antenna supports communication, "
                  "and the thermal camera helps study temperature "
                  "and surface properties."
    },

    "Asteroid Monitoring": {
        "power": "Solar Panels",
        "communication": "High Gain Antenna",
        "camera": "High Resolution Camera",
        "reason": "Solar panels provide power, the high gain antenna "
                  "supports communication, and the high resolution "
                  "camera helps observe asteroid features."
    }
}

suggestion = recommendations[mission]

st.subheader(f"Recommended Design: {mission}")

col1, col2, col3 = st.columns(3)

with col1:
    st.write("☀️ **Power Source**")
    st.info(suggestion["power"])

with col2:
    st.write("📡 **Communication**")
    st.info(suggestion["communication"])

with col3:
    st.write("📷 **Scientific Equipment**")
    st.info(suggestion["camera"])

st.write("### Why these components?")
st.write(suggestion["reason"])

# Compare recommendations with current selections

recommendation_match = (
    power_source == suggestion["power"]
    and communication == suggestion["communication"]
    and camera == suggestion["camera"]
)

if recommendation_match:
    st.success("Your current spacecraft matches all recommendations!")
else:
    st.warning(
        "Your current spacecraft does not match all recommendations."
    )

    st.write("Update your selections in the Spacecraft Designer:")
    st.write("**Recommended Power Source:**", suggestion["power"])
    st.write("**Recommended Communication:**", suggestion["communication"])
    st.write("**Recommended Camera:**", suggestion["camera"])



# --------------------------------
# CUSTOM SPACECRAFT VS NASA MISSION
# --------------------------------

st.divider()

st.title("My Spacecraft vs NASA 🚀")

st.write(
    "Compare your custom spacecraft design with "
    "a real NASA mission."
)

# Select a real NASA mission as reference

reference_mission = st.selectbox(
    "Choose a NASA reference mission:",
    list(REAL_MISSIONS.keys()),
    key="reference_mission"
)

# Get NASA mission information

reference_data = REAL_MISSIONS[reference_mission]

st.divider()

st.header("Design Comparison")

# Two comparison columns

col1, col2 = st.columns(2)

with col1:

    st.subheader("Your Spacecraft")

    st.write("**Mission:**", mission)

    st.write("**Power Source:**", power_source)

    st.write("**Communication:**", communication)

    st.write("**Scientific Equipment:**", camera)

    st.write(
        "**Total Mass:**",
        f"{resources['total_mass']} kg"
    )

    st.write(
        "**Total Cost:**",
        f"${resources['total_cost']:,}"
    )

    st.write(
        "**Available Power:**",
        f"{resources['available_power']} W"
    )

    st.write(
        "**Power Used:**",
        f"{resources['power_used']} W"
    )

    st.write(
        "**Design Score:**",
        f"{total_score}/100"
    )

with col2:

    st.subheader(reference_mission)

    st.write(
        "**Destination:**",
        reference_data["destination"]
    )

    st.write(
        "**Launch Year:**",
        reference_data["launch_year"]
    )

    st.write(
        "**Spacecraft Type:**",
        reference_data["spacecraft_type"]
    )

    st.write(
        "**Agency:**",
        reference_data["agency"]
    )

    st.write(
        "**Mission Objective:**",
        reference_data["objective"]
    )

    st.write("**Actual Listed Instruments:**")

    for instrument in reference_data["instruments"]:
        st.write("🔹", instrument)

st.divider()

# Compare mission purposes

st.header("Mission Purpose Comparison")

st.write("**Your mission objective:**")

st.info(mission_details[mission])

st.write("**NASA mission objective:**")

st.info(reference_data["objective"])

# Compare scientific equipment with NASA instruments

st.header("Scientific Equipment Comparison")

st.write(
    "**Your selected scientific equipment:**",
    camera
)

st.write("**NASA mission instruments:**")

for instrument in reference_data["instruments"]:
    st.write("🔹", instrument)

st.caption(
    "Your camera selection is a simplified educational component. "
    "It should not be treated as technically equivalent to a "
    "specific NASA instrument."
)

st.divider()

# Final design assessment

st.header("Your Design Assessment")

if validation["mission_ready"]:

    st.success(
        "Your spacecraft passes the simulator's "
        "budget, mass, and power checks."
    )

else:

    st.warning(
        "Your spacecraft does not currently pass all "
        "resource checks. Improve your design before proceeding."
    )

if total_score >= 80:

    st.success("Your design has a strong resource-efficiency score.")

elif total_score >= 60:

    st.info("Your design has reasonable resource efficiency.")

else:

    st.warning("Your design needs further optimization.")

st.write(
    "Use the NASA mission as a learning reference to understand "
    "how real missions differ in objectives, spacecraft types, "
    "and scientific instruments."
)

st.link_button(
    "View Official NASA Mission",
    reference_data["source"]
)
