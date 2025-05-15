# testGenAIProjectCICD
-> Implemented CI/CD.

-> Cloud deployment 

-> Docker Image

-> GenAI app

The App has a web interface which takes input of a Organization name. Then:
  1. It finds open position in that org related to software developemnt
  2. Extracts the skills required
  3. Checks on vector database to get similar projects done by me.
  4. Generates a cold email and reference those project(s).
  5. Sends the email if the option is ticked and email address is given in the app.

GenAI complexities used: Prompt Engineering(LangChain), Vector Database, RAG

Programming Language: Python

CI/CD imp: Git, GitLab, Runner

Microservices Architecture: WebInterface, Docker Img of the apps.

Cloud: EC2 instance, S3 bucket, Vector Database.
