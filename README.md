# Student Management System

A Python student-record management project with a Tkinter desktop interface and a browser dashboard for GitHub Pages.

## Why the GitHub Pages site did not match the desktop screenshot

The desktop application in `dashboard.py` uses Tkinter, which runs as a native Python desktop program. GitHub Pages serves static web files; it does not execute Python/Tkinter or display the desktop window. With no root `index.html`, Pages displayed this README instead of the dashboard. The new `index.html` provides a browser-based dashboard styled to match the desktop app and reads the initial demo records from `data/students.json`.

The web version supports viewing, searching, registering, editing, and deleting student records. Browser changes are stored in that browser's local storage; they do not update `data/students.json` in GitHub. To change the shared initial data, edit the JSON file and commit the change.

## Run the desktop application

1. Install Python and open the project folder in a terminal.
2. Run `python main.py` (or `python login.py`).
3. Demo administrator credentials: username `admin`, password `admin123`.

## Features

- Register, view, search, update, and delete student records
- View available courses and calculate grades
- Display student statistics and unique courses

## Python concepts

Variables, input/output, conditionals, loops, operators, lists, dictionaries, sets, functions, modules, file handling, and JSON.

## Developer

Ahlam Ali — Kenya Coast National Polytechnic
