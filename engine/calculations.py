
import json
from pathlib import Path


# Load component information from JSON file

DATA_FILE = (
    Path(__file__).resolve().parent.parent
    / "data"
    / "components.json"
)

with open(DATA_FILE, "r") as file:
    COMPONENTS = json.load(file)

# Load mission requirements from JSON file

MISSION_FILE = (
    Path(__file__).resolve().parent.parent
    / "data"
    / "missions.json"
)

with open(MISSION_FILE, "r") as file:
    MISSIONS = json.load(file)

# Resource limits

MAX_BUDGET = 10_000_000
MAX_MASS = 500


# Calculate spacecraft resources

def calculate_resources(power_source, communication, camera):

    power_data = COMPONENTS[power_source]
    communication_data = COMPONENTS[communication]
    camera_data = COMPONENTS[camera]

    total_cost = (
        power_data["cost"]
        + communication_data["cost"]
        + camera_data["cost"]
    )

    total_mass = (
        power_data["mass"]
        + communication_data["mass"]
        + camera_data["mass"]
    )

    available_power = power_data["power"]

    power_used = (
        communication_data["power"]
        + camera_data["power"]
    )

    return {
        "total_cost": total_cost,
        "total_mass": total_mass,
        "available_power": available_power,
        "power_used": power_used
    }


# Validate spacecraft resources

def validate_resources(resources):

    budget_ok = resources["total_cost"] <= MAX_BUDGET

    mass_ok = resources["total_mass"] <= MAX_MASS

    power_ok = resources["power_used"] <= resources["available_power"]

    mission_ready = budget_ok and mass_ok and power_ok

    return {
        "budget_ok": budget_ok,
        "mass_ok": mass_ok,
        "power_ok": power_ok,
        "mission_ready": mission_ready
    }


def validate_mission(mission, power_source, communication, camera):

    # Get the requirements for the selected mission
    requirements = MISSIONS[mission]

    # Check whether selected components match mission requirements
    camera_ok = camera == requirements["required_camera"]

    communication_ok = (
        communication == requirements["required_communication"]
    )

    power_source_ok = (
        power_source == requirements["required_power_source"]
    )

    # Mission is suitable only if all three components match
    mission_suitable = (
        camera_ok and communication_ok and power_source_ok
    )

    return {
        "camera_ok": camera_ok,
        "communication_ok": communication_ok,
        "power_source_ok": power_source_ok,
        "mission_suitable": mission_suitable
    }
