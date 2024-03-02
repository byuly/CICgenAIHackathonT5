This is our Hackathon project for nwHacks 2024!

Here is the link to our repository: https://github.com/johnny-581/Hackathon-Project

# This is how to commit your changes to git

## Before you make any changes:
make sure you pull the latest changes from the remote repository:  
```
git pull origin main
```
Then create and swich to a new branch. You must make your changes in this new branch, so that later it can be reviewed and merged into the main branch:
```
git checkout -b <branch_name>
```
Replace <branch_name> with the name you wish to give to your new branch.  
You can swich between the main branch and your branch using this command:
```
git checkout <branch_name>
```

## Regularly stage, commit, and push your changes
```
git add .
git commit -m "Your commit message"
git push origin <branch_name>
```
Replace "Your commit message" with a brief, informative description of the changes included in the commit.

/

# Suggestions from ChatGTP

Creating a website with Java as the backend involves several steps and components. Here's a simple breakdown of how you can achieve this, focusing on the motivational/comforting sentence generator feature and the hosting of links to resources:

### Backend (Java)

1. **Java Web Server:** Use a lightweight framework like Spring Boot or Spark Framework for ease of setup. Spring Boot is more feature-rich and can easily serve content, handle requests, and manage dependencies.
   
2. **Sentence Generator API:** Create a RESTful API endpoint that returns a random motivational sentence. The sentences can be stored in an array or fetched from a database.

3. **Resource Links API:** Another API endpoint to provide the mental health resources links for UBC students.

4. **Database (Optional):** If you want to store the sentences and resources in a database, you might use a simple database like H2 or SQLite for starters.

5. **Maven or Gradle:** Use a build tool like Maven or Gradle for dependency management and to build your project.

### Frontend

1. **HTML Page:** A simple HTML file to display the motivational sentence and resources. This will be served by the Java backend.

2. **CSS File:** To style the webpage, including the layout shown in the sketch.

3. **JavaScript File:** To fetch the motivational sentence from the backend API and refresh it every few seconds, as well as to fetch and display the resources.

### Files and Structure

Here's a simple structure for your project:

```
project-root/
│
├── src/
│   ├── main/
│   │   ├── java/
│   │   │   └── Your Java backend code
│   │   │
│   │   ├── resources/
│   │   │   └── static/
│   │   │       ├── index.html
│   │   │       ├── styles.css
│   │   │       └── script.js
│   │   └── application.properties (or yaml)
│   │
│   └── test/
│       └── Java test code
│
├── pom.xml (for Maven) or build.gradle (for Gradle)
└── .gitignore
```

### Steps to Create the Backend

1. **Set up the project:** Initialize a Maven/Gradle project with dependencies for your chosen framework.

2. **Create the main application class:** Set up the main class to run the web server.

3. **Implement the APIs:**
   - **Sentence API:** Create a method that returns a random sentence.
   - **Resources API:** Create a method that returns the list of resources.

4. **Static content serving:** Configure your application to serve `index.html`, `styles.css`, and `script.js` from the `static` directory in resources.

### Steps to Create the Frontend

1. **index.html:** Write the HTML code to layout the page as per your sketch.
   
2. **styles.css:** Add CSS to style the page, including responsive design if needed.

3. **script.js:**
   - Fetch the motivational sentence from the Java backend and update the sentence on the page every few seconds.
   - Fetch and display the resources.

### Deployment

1. Build your Java application into a JAR file.
2. Deploy it on a server that can run Java applications, such as a Tomcat server or a simpler standalone server if you use Spring Boot.

Remember to ensure your Java backend is CORS (Cross-Origin Resource Sharing) enabled so that your frontend JavaScript can make AJAX requests to your backend if they are not being served from the same domain.

This is a high-level overview and the actual implementation may require more specific steps based on the tools and libraries you choose to use.