<p align="left"> <img src="https://komarev.com/ghpvc/?username=bhch7051&label=Profile%20views&color=0e75b6&style=flat" alt="bhch7051" /> </p>

# Clothing Similarity Search (Vector Search Engine)


<p align="center">
<img src="./public/search-engine.gif" />
</p>


## Introduction
The Clothing Similarity Search project aims to provide a search functionality that allows users to find similar clothing items based on their descriptions. The project includes web scraping of product data from various websites, preprocessing of the data, generating sentence embeddings using the sentence-transformers library, and deploying a Flask server to provide an API for similarity search.

## Data Collection
To collect the clothing data, web scraping techniques were employed to extract product information from websites such as Ajio, Myntra, and Nike. The scraped data includes the product URL, title, and description. The data was stored in a CSV file with columns for URL, title, and description and contains details of **4,00,000** products.

## Data Preprocessing
The data preprocessing step involves cleaning and transforming the text data to make it suitable for similarity search. The following preprocessing steps were performed:
- Tokenization: The text was tokenized into individual words using the NLTK library's word_tokenize function.
- Lowercasing: All tokens were converted to lowercase.
- Special character removal: Special characters and punctuation marks were removed from the tokens.
- Stopword removal: Stopwords, such as common English words and symbols, were removed from the tokens.
- Lemmatization: The tokens were lemmatized using the WordNetLemmatizer from the NLTK library.
- HTML tag removal: HTML tags and entities were removed from the preprocessed text.

## Generating Sentence Embeddings
Sentence embeddings were generated using pretrained Sentence-BERT Transformers. The resulting embeddings represent the semantic meaning of the clothing descriptions.

## Similarity Search
To find similar clothing items, the cosine similarity measure was used to compare the embeddings of the query text with the embeddings of the clothing products. The higher the cosine similarity score, the more similar the items are in terms of their descriptions. The top matching products were retrieved based on the similarity scores.

## Deployment
The project includes a Flask server that provides an API for similarity search. The server was deployed using Docker on Google Cloud. The API endpoint accepts a query string as well as K and returns the top K most similar products as a JSON response.

## Project Structure
The project repository has the following structure:
- `data/`: Directory containing the scraped clothing data in CSV format and the embeddings.npy file.
- `main`: Containing the code for preprocessing, similarity search as well as Flask server.
- `requirements.txt`: File specifying the project dependencies.
- `Dockerfile`: Docker configuration file for containerization.
- `README.md`: Project documentation file.

## Running the Project Locally
To run the project locally, follow these steps:
1. Clone the repository to your local machine.
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Scrape clothing data from websites or use the provided sample data.
4. Run the Flask server using the command `python main.py`.
5. Access the API endpoint locally to perform clothing similarity search.


## Running the Project with Docker and Interacting with cURL

To run the project using Docker and interact with it using cURL, please follow these instructions:

1. Docker Installation: Ensure that Docker is installed on your computer. You can download and install Docker from the official Docker website (https://www.docker.com/get-started).

2. Project File Download: Download all the project files and save them in a single folder on your computer.

3. Open Command Prompt or Terminal: Open a command prompt or terminal window on your computer.

4. Navigate to Project Folder: Use the `cd` command to navigate to the folder where you saved the project files. For example:

   ```shell
   cd path/to/project/folder
   ```

5. Docker Image Build: Build the Docker image for the project by running the following command:

   ```shell
   docker build -t clothing-similarity-search .
   ```

   This command builds the Docker image using the provided Dockerfile.

6. Run Docker Container: Execute the following command to run the Docker container and start the application:

   ```shell
   docker run -p 8080:8080 clothing-similarity-search
   ```

   This command starts the Docker container and maps port 8080 of the container to port 8080 on your local machine.

7. Open Another Command Prompt or Terminal: Open a new command prompt or terminal window while keeping the Docker container running.

8. Navigate to Project Folder: Use the `cd` command to navigate to the folder where you saved the project files (same as step 4).

9. Send Request to the Application: Use the following `curl` command to send a POST request to the running application and obtain the output. You can modify the text to your desired input:

   ```shell
   curl -X POST -H "Content-Type: application/json" -d "{\"text\": \"A black top with a LOGO\", \"N\": 8}" http://localhost:8080/
   ```

   This command sends a POST request with the specified JSON payload to the application and retrieves the output.

By following these steps, you should be able to run the project and obtain the output using Docker.

Note: Please ensure that Docker is running on your computer before executing the commands.
## References
- [Sentence Transformers Documentation](https://www.sbert.net/)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Docker Documentation](https://docs.docker.com/)
- Reimers, Nils and Gurevych, Iryna. "Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks." In Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing, November 2019. Association for Computational Linguistics. Available at: [arXiv:1908.10084](http://arxiv.org/abs/1908.10084).



<h3 align="left">Languages and Tools:</h3>
<p align="left"> <a href="https://www.docker.com/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/docker/docker-original-wordmark.svg" alt="docker" width="40" height="40"/> </a> <a href="https://expressjs.com" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/express/express-original-wordmark.svg" alt="express" width="40" height="40"/> </a> <a href="https://git-scm.com/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/git-scm/git-scm-icon.svg" alt="git" width="40" height="40"/> </a> <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/javascript/javascript-original.svg" alt="javascript" width="40" height="40"/> </a> <a href="https://www.linux.org/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/linux/linux-original.svg" alt="linux" width="40" height="40"/> </a> <a href="https://mochajs.org" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/mochajs/mochajs-icon.svg" alt="mocha" width="40" height="40"/> </a> <a href="https://www.mongodb.com/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/mongodb/mongodb-original-wordmark.svg" alt="mongodb" width="40" height="40"/> </a> <a href="https://nodejs.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/nodejs/nodejs-original-wordmark.svg" alt="nodejs" width="40" height="40"/> </a> <a href="https://postman.com" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/getpostman/getpostman-icon.svg" alt="postman" width="40" height="40"/> </a> </p>
