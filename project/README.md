# MindWink: Daily Alignment Page (Module 1 - Cloud Database CRUD)

## Overview
MindWink is a child-centered learning application designed to help children understand cause and effect, emotional awareness, and personal growth through simple daily actions. This project demonstrates the first module: implementing cloud database CRUD (Create, Read, Update, Delete) operations using Firebase Firestore.

On the "Focus" page, children (or guardians) can:
- Enter daily actions (e.g., "I made my bed")
- Select their mood before and after each action (using emojis)
- Reflect on how actions influence feelings
- See their actions and mood changes visualized in a chart

- Edit or delete any action entry for accurate records
- Submit daily reflections and guardian notes

All data is stored per user, ensuring privacy. Each child only sees their own data, protected by Firebase Authentication and Firestore security rules.

All data is securely stored in Firebase, allowing for later analysis and visualization.

## Purpose
The purpose of this module is to:
- Practice and demonstrate cloud database CRUD operations in a real-world, child-friendly application
- Lay the foundation for future modules (data analysis, visualization, security, etc.)
- Show how children interact with the app and how their data is stored and retrieved

- Demonstrate secure, ethical data handling for children

## Software Demo Video
[Demo Video Link](https://your-youtube-link-here)

## Development Environment
- Visual Studio Code
- Git & GitHub
- JavaScript, HTML, CSS
- Firebase Firestore
- Firebase Authentication
- Browser: Chrome/Edge/Firefox

## Programming Language
- JavaScript (ES6)
- HTML5
- CSS3

## Useful Websites
- [Firebase Docs](https://firebase.google.com/docs)
- [MDN Web Docs](https://developer.mozilla.org/)
- [Chart.js Docs](https://www.chartjs.org/docs/)
- [W3Schools](https://www.w3schools.com/)
- [GitHub Docs](https://docs.github.com/)

## Security & Privacy

MindWink uses Firebase Authentication to ensure each child’s data is private. Firestore security rules restrict access so users can only read and write their own data. Mood values are validated, and unauthenticated access is blocked for safety.

Example Firestore rules:

```
rules_version = '2';
service cloud.firestore {
	match /databases/{database}/documents {
		match /days/{userId}/{date}/{document=**} {
			allow read, write: if request.auth != null && request.auth.uid == userId;
		}
	}
}
```

This ensures ethical, secure handling of children’s data.

---

Feel free to personalize this README and add your video link above!
