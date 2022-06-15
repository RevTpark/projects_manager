# Project Manager Desktop App
![image](https://user-images.githubusercontent.com/78678620/173767823-36890fe9-fce8-4eb1-a5d0-19084ee63a59.png)
## Tech Stack
- Rust Backend
- PyQt5 Frontend
## Idea
- I had my all projects in different directories due to which I had difficulty locating them. 
- So I thought I needed to make a app that gathers all my project directories and shows them in one place.
## Functionalities
- Made a floating GUI that displays all my projects in one place.
- Added what project used what language as an icon beside the directory.
- Allows to filter on basis on langauge used.
- Allows to search for a particular directory/project based on name.
- Clicking on the name opens the particular project folder
## Execution
- I wrote all the backend needed in Rust and made a Python module using PyO3.
- Used Qt5 designer I designed GUI of the application. Imported the ui file and created the frontend functionality.
