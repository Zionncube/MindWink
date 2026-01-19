
MindWink: Daily Alignment Page (Module 1 - Cloud Database CRUD)

MindWink is a child-centered learning application designed to help children understand cause and effect, emotional awareness, and personal growth through simple daily actions. This project demonstrates the first module: implementing cloud database CRUD (Create, Read, Update, Delete) operations using Firebase Firestore through a real-world web application.

Project Overview

MindWink is built as a real-world web application (HTML, CSS, JS) where children and guardians interact with the Focus page to:
• Enter daily actions (e.g., "I made my bed")
• Select their mood before and after each action (using emojis)
• Reflect on how actions influence feelings
• See their actions and mood changes visualized in a chart
• Edit or delete any action entry for accurate records
• Submit daily reflections and guardian notes

All data is stored per user, ensuring privacy. Each child only sees their own data, protected by Firebase Authentication and Firestore security rules. All data is securely stored in Firebase, allowing for later analysis and visualization.

Features

• Cloud database creation (Firestore)
• CRUD operations (Create, Read, Update, Delete)
• User authentication (concept, per-user data)
• Two related collections: users and actions

Technologies Used

• HTML, CSS, JavaScript
• Firebase Firestore
• Firebase Authentication
• Git & GitHub

Repository Structure

project/
index.html
about.html
attribution.html
focus.html
form.html
siteplan.html
strategies.html
styles.css
thankyou.html
images/
scripts/
	main.js
styles/
	large.css
	normalize.css
	styles.css

Never upload your serviceAccountKey.json file.

How to Run

To verify that data is being stored in the database, open the Firebase Firestore browser console while using the app. You will see new documents and updates appear live as you interact with MindWink. This process is also demonstrated in the video submission.

1. Clone the Repository
Click the green "Code" button and clone this repository to your local machine.

2. Set Up Your Own Firebase Firestore Backend
Go to Firebase Console and create a new project.
Enable Firestore Database and Authentication (email/password or Google sign-in recommended).
Add a new web app in Firebase and copy the configuration snippet.
Replace the Firebase config in your web app (project/scripts/main.js or similar) with your own credentials.
(Optional) Download your serviceAccountKey.json for Python backend demo and place it in the project root (do NOT upload to GitHub).

3. Running the Real MindWink Web App (Recommended for Users & Video Demo)
Open the project/ folder.
Double-click index.html to launch the app in your browser.
Use the Focus page to add, edit, and view actions and moods.
All data is stored in your own Firebase Firestore and protected by authentication.

Software Demo Video


Cloud Video (Final)

Watch the cloud video (final): Reflection / Learning Strategies

The most effective learning strategy in this module was breaking the work into small, manageable steps and following official documentation. Incremental testing helped reduce errors. Initially, Firebase configuration was challenging, but persistence and structured troubleshooting improved my understanding. In the next module, I will prototype earlier and test more frequently.

Reflection / Learning Strategies

The most effective learning strategy in this module was breaking the work into small, manageable steps and following official documentation. Incremental testing helped reduce errors. Initially, Firebase configuration was challenging, but persistence and structured troubleshooting improved my understanding. In the next module, I will prototype earlier and test more frequently.

Reflection / Learning Strategies

The most effective learning strategy in this module was breaking the work into small, manageable steps and following official documentation. Incremental testing helped reduce errors. Initially, Firebase configuration was challenging, but persistence and structured troubleshooting improved my understanding. In the next module, I will prototype earlier and test more frequently.

watch thi new demo video: https://youtu.be/rbmN3yo63BE

Watch the demo video: https://youtu.be/Pu0dJ-mWMAY

Time Log

Monday – 3 hrs: Planning & schema design
Tuesday – 4 hrs: Firebase setup & authentication
Wednesday – 4 hrs: CRUD implementation
Thursday – 3 hrs: Testing & debugging
Friday – 3 hrs: Documentation & README
Saturday – 3 hrs: Video recording & GitHub publishing
Total: 20 hours

Reflection / Learning Strategies

The most effective learning strategy in this module was breaking the work into small, manageable steps and following official documentation. Incremental testing helped reduce errors. Initially, Firebase configuration was challenging, but persistence and structured troubleshooting improved my understanding. In the next module, I will prototype earlier and test more frequently.

Security & Privacy

MindWink uses Firebase Authentication to ensure each child’s data is private. Firestore security rules restrict access so users can only read and write their own data. Mood values are validated, and unauthenticated access is blocked for safety.

Example Firestore rules:

rules_version = '2';
service cloud.firestore {
	match /databases/{database}/documents {
		match /users/{userId} {
			allow read, write: if request.auth != null && request.auth.uid == userId;
		}
		match /actions/{actionId} {
			allow read, write: if request.auth != null;
		}
	}
}

.gitignore (Required)

serviceAccountKey.json

Never upload your Firebase service account key.

