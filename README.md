# Bug Analysis Web App

<hr>

### Required Python Libraries to use this repository :

1. OS
2. CSV
3. Pandas
4. SQLite3
5. Flask

### Steps to use this repository :

1. Store the all input CSV files in Input directory
2. Install all the required python libraries which is listed above.
3. If report database is not generated then Run the report.py using the command: `python report.py` .
4. Run the app.py using the command: `python app.py` , now local server as been started.
5. Then open the browser and search `http://127.0.0.1:5000/` which shows the Category table output in display and if you want to see the Sub-Category then go to `http://127.0.0.1:5000/sub` .
6. To close the local server press `Ctrl+C` in terminal.

<br>
<br>
<br>

<hr>

##### Create a new repository

- git clone https://gitlab.com/mugunthanraju/bug-analysis-web-app.git
- cd bug-analysis-web-app
- git switch -c main
- touch README.md
- git add README.md
- git commit -m "add README"
- git push -u origin main

<br>

##### Push an existing folder

- cd existing_folder
- git init --initial-branch=main
- git remote add origin https://gitlab.com/mugunthanraju/bug-analysis-web-app.git
- git add .
- git commit -m "Initial commit"
- git push -u origin main

<br>

##### Push an existing Git repository

- cd existing_repo
- git remote rename origin old-origin
- git remote add origin https://gitlab.com/mugunthanraju/bug-analysis-web-app.git
- git push -u origin --all
- git push -u origin --tags
