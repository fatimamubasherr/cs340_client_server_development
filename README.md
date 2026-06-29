# cs340_client_server_development
Portfolio artifacts for CS 340 Client/Server Development
## Project: Grazioso Salvare Rescue Animal Dashboard

This repository contains my CS 340 Project Two portfolio artifacts. The project is a dashboard application created for Grazioso Salvare to help identify dogs that may be suitable for search-and-rescue training.

## Files Included

- `ProjectTwoDashboard.ipynb` - Final dashboard code
- `animal_shelter.py` - CRUD Python module for MongoDB operations
- `Project2CompletedCS340.docx` - Project Two README document
- `Grazioso Salvare Logo.png` - Dashboard logo

## Reflection

One of the biggest lessons I learned in this course was the importance of writing code that is maintainable, readable, and adaptable. In Project One, I created a reusable CRUD Python module that separated all database operations from the dashboard itself. Instead of placing MongoDB queries throughout the dashboard code, I could simply call methods from the `AnimalShelter` class whenever data was needed. This made the dashboard much easier to read, debug, and modify.

This project also changed the way I approach problems as a computer scientist. Rather than immediately writing code, I first focused on understanding the client's requirements and breaking the project into smaller pieces. I designed the database connection first, then verified that queries returned the correct data before connecting them to the dashboard widgets.

Computer scientists create software that helps people solve real-world problems more efficiently. In this project, the dashboard allows Grazioso Salvare to quickly identify dogs that meet specific rescue training requirements instead of manually searching through thousands of records. Interactive filters, maps, and charts make the information easier to understand and help support faster decision-making.
