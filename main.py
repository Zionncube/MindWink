"""
MindWink – Cloud Database Module (CSE 310)
Author: Happiness Nonkululeko Ncube

This program demonstrates how to use Google Firebase Firestore
as a cloud-based NoSQL (key/value) database using Python.
"""

import firebase_admin
from firebase_admin import credentials, firestore
from datetime import datetime
import uuid

# ---------------------------------------------------
# Firebase Initialization
# ---------------------------------------------------

def initialize_firebase():
    """
    Initializes the Firebase application using a service account.
    This must be called before any Firestore operations.
    """
    cred = credentials.Certificate("serviceAccountKey.json")
    firebase_admin.initialize_app(cred)
    return firestore.client()


db = initialize_firebase()

# ---------------------------------------------------
# User Operations
# ---------------------------------------------------

def create_user(name, age):
    """
    Creates a new user document in the 'users' collection.
    Returns the generated user ID.
    """
    user_id = str(uuid.uuid4())
    db.collection("users").document(user_id).set({
        "name": name,
        "age": age,
        "created_at": datetime.utcnow()
    })
    return user_id


def get_user(user_id):
    """
    Retrieves a single user document by user ID.
    """
    doc = db.collection("users").document(user_id).get()
    if doc.exists:
        return doc.to_dict()
    return None


# ---------------------------------------------------
# Action Operations (Related to Users)
# ---------------------------------------------------

def add_action(user_id, action_text, mood_before, mood_after):
    """
    Adds a new action entry for a user.
    This document is stored in the 'actions' collection
    and linked to the user via user_id.
    """
    action_id = str(uuid.uuid4())
    db.collection("actions").document(action_id).set({
        "user_id": user_id,
        "action": action_text,
        "mood_before": mood_before,
        "mood_after": mood_after,
        "timestamp": datetime.utcnow()
    })
    return action_id


def get_actions_for_user(user_id):
    """
    Retrieves all action records associated with a specific user.
    """
    actions_ref = db.collection("actions").where("user_id", "==", user_id)
    return [doc.to_dict() for doc in actions_ref.stream()]


def update_action(action_id, new_mood_after):
    """
    Updates the 'mood_after' value for an existing action.
    """
    db.collection("actions").document(action_id).update({
        "mood_after": new_mood_after,
        "updated_at": datetime.utcnow()
    })


def delete_action(action_id):
    """
    Deletes an action document from the database.
    """
    db.collection("actions").document(action_id).delete()


# ---------------------------------------------------
# Demonstration Script
# ---------------------------------------------------

def run_demo():
    """
    Demonstrates full CRUD functionality:
    - Create user
    - Insert action
    - Retrieve actions
    - Update action
    - Delete action
    """
    print("=== MindWink Cloud Database Demo ===")

    # Create user
    user_id = create_user("Luna", 9)
    print(f"User created with ID: {user_id}")

    # Add action
    action_id = add_action(
        user_id,
        "Made my bed",
        mood_before=2,
        mood_after=4
    )
    print(f"Action added with ID: {action_id}")

    # Retrieve actions
    actions = get_actions_for_user(user_id)
    print("Actions retrieved:")
    for action in actions:
        print(action)

    # Update action
    update_action(action_id, new_mood_after=5)
    print("Action updated.")

    # Delete action
    delete_action(action_id)
    print("Action deleted.")

    print("=== Demo Complete ===")


if __name__ == "__main__":
    run_demo()
