<!-- PROJECT LOGO -->

<p align="center">
  <a href="https://creepypasta-demo.vercel.app/">
    <img src="/Images/logo.png" alt="Logo" width="100" height="100">
  </a>

  <h3 align="center">Creepypasta - Text Generator</h3>

  <p align="center">
    Website which uses Deep Learning to generate horror stories.
    <br />
    <br />
    <a href="https://creepypasta-demo.vercel.app/">View Demo</a>
    ·
    <a href="https://github.com/dhairya0907/Creepypasta-Text-Generator-Website">View Website Repo</a>
    ·
    <a href="https://github.com/dhairya0907/Creepypasta-Text-Generator/issues">Report Bug</a>
    ·
    <a href="https://github.com/dhairya0907/Creepypasta-Text-Generator/issues">Request Feature</a>
  </p>
</p>

<!-- PROJECT SHIELDS -->
<div align="center">
   <a target="_blank" href="https://github.com/dhairya0907/Creepypasta-Text-Generator/blob/main/LICENSE"><img src="https://badgen.net/badge/license/MIT/blue"></a>
   <a target="_blank" href="https://www.linkedin.com/in/dhairyasharma0907/"><img src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&logo=linkedin&style=social"></a>&nbsp;
    <a target="_blank" href="https://twitter.com/dhairya_0907"><img src="https://img.shields.io/twitter/follow/dhairya_0907?label=Follow&style=social"></a>
</div>




<!-- ABOUT THE PROJECT -->
<p>
  <br/>
  <br/>
</p>


## About The Project

<p align="center" >
   <a href="https://creepypasta-demo.vercel.app/">
    <img alt="Creepypasta Website Demo" src="/Images/Desktop_Screen_GIf.gif"/>
    </a>

</p>
<p  align="center">
  Creepypasta Website Demo
  <br/>
 <br/>
</p>

There are two parts to the project. One is the <a href="https://github.com/dhairya0907/Creepypasta-Text-Generator/tree/main/Data%20Sources/Models">Deep Learning model</a> which generates the text. The other is the <a href="https://creepypasta-demo.vercel.app/">website</a> which uses the model to generate text.

I have used <a href="https://github.com/dhairya0907/Creepypasta-Text-Generator/tree/main/Data%20Sources/Models">Deep Learning model</a> to generate text. It is a <a href="https://en.wikipedia.org/wiki/Neural_network">Neural Network</a> which uses <a href="https://en.wikipedia.org/wiki/Recurrent_neural_network">Recurrent Neural Network</a> to generate text.

I have hosted a model on  <a href="https://algorithmia.com/">Algorithmia</a> and used it's API to generate text.


### Built With
* [React Native](https://reactnative.dev/)
* [Algorithmia](https://algorithmia.com/)
* [Deployed using Vercel](https://vercel.com/)

### What I learned
* How to clear raw data to use it for training.
* How to use <a href="https://github.com/dhairya0907/Creepypasta-Text-Generator/tree/main/Data%20Sources/Models">Deep Learning model</a> to generate text.
* How to use <a href="https://algorithmia.com/">Algorithmia</a> to generate text.
* How to use <a href="https://vercel.com/">Vercel</a> to deploy a website.
* How to use <a href="https://www.tensorflow.org/">TensorFlow</a> to train a model.
* How to train a model incrementally.
* How to handle large <a href="https://github.com/dhairya0907/Creepypasta-Text-Generator/tree/main/Data%20Sources">data</a>.
* How to use Machine Learning model to generate text and display it on the website.



<!-- GETTING STARTED -->
## Getting Started

To host web application on user localhost follow below steps :

### Prerequisites

* Reddit API Key
  ```
  Go to https://www.reddit.com/prefs/apps/
  ```
* Algorithmia Account
  ```
  Go to https://algorithmia.com/
  ```
* Optional: 
    1. Wandb Account and Wandb API Key to track training
    ```
    Go to https://wandb.com/
    ```
    2. Firebase Account to upload files while scrapping reddit
    ```
    Go to https://console.firebase.google.com/u/2/project/ml-research-ab177/settings/serviceaccounts/adminsdk
    ```
  Note: If you don't have a Wandb account, remove Wandb code from the scripts.

### Installation
* Common Steps
    1. Run <a href="https://github.com/dhairya0907/Creepypasta-Text-Generator/blob/main/Scripts/Reddit%20Scraping%20Script.py">Reddit Scraping Script.py</a> to scrape data from Reddit.
    2. Run <a href="https://github.com/dhairya0907/Creepypasta-Text-Generator/blob/main/Scripts/Filter%20Dates.py">Filter Dates.py</a> to filter dates.
    3. Run <a href="https://github.com/dhairya0907/Creepypasta-Text-Generator/blob/main/Scripts/Csv%20to%20Story%20Text.py">Csv to Story Text.py</a> to convert csv to story text.
    4. Run <a href="https://github.com/dhairya0907/Creepypasta-Text-Generator/blob/main/Scripts/Split%20Text%20Files.py">Split Text Files.py</a> to split text files into smaller chunks.
    5. Run <a href="https://github.com/dhairya0907/Creepypasta-Text-Generator/blob/main/Scripts/Vocabulary%20details.py">Vocabulary details.py</a> to get details of the vocabulary.
    6. Run <a href="https://github.com/dhairya0907/Creepypasta-Text-Generator/blob/main/Scripts/Train%20Model.py">Train Model.py</a> to train the model.

* For Word Level
    1. Run <a href="https://github.com/dhairya0907/Creepypasta-Text-Generator/blob/main/Scripts/Word_Level_Text_Generation_First_Time.ipynb">Word_Level_Text_Generation_First_Time.ipynb</a> to train the model for the first time.
    2. Run <a href="https://github.com/dhairya0907/Creepypasta-Text-Generator/blob/main/Scripts/Word_Level_Text_Generation_After_First_Time.ipynb">Word_Level_Text_Generation_After_First_Time.ipynb</a> to train the model incrementally.

* For Character Level
    1. Run <a href="https://github.com/dhairya0907/Creepypasta-Text-Generator/blob/main/Scripts/Charcter_Level_Text_Generation.ipynb">Charcter_Level_Text_Generation.ipynb</a> to train the model for the first time.
    2. Again run <a href="https://github.com/dhairya0907/Creepypasta-Text-Generator/blob/main/Scripts/Charcter_Level_Text_Generation.ipynb">Charcter_Level_Text_Generation.ipynb</a> with changes mentioned to train the model incrementally.

* To host Model on Algorithmia
    1. Go to <a href="https://algorithmia.com/">Algorithmia</a> and create a new project.
    2. Upload all the files in <a href="https://github.com/dhairya0907/Creepypasta-Text-Generator/tree/main/Data%20Sources">Data Sources</a> to your project.
    3. Past <a href="https://github.com/dhairya0907/Creepypasta-Text-Generator/blob/main/Scripts/Algorithmia.py">Algorithmia.py</a> to Source Code on Algorithmia.
    4. Add Deppendency to the project.
        ```
        algorithmia>=1.0.0,<2.0
        tensorflow-gpu
        keras
        h5py
        ```
    5. Now Build and Publish the model.


<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/dhairya0907/Creepypasta-Text-Generator/issues) for a list of proposed features (and known issues).



<!-- LICENSE -->
## License

Distributed under the MIT License. See [`LICENSE`](https://github.com/dhairya0907/Creepypasta-Text-Generator/blob/main/LICENSE) for more information.



<!-- CONTACT -->
## Contact

Dhairya Sharma - [@dhairya_0907](https://twitter.com/dhairya_0907) - dhairya.sharma532@gmail.com.com

Project Github Link: [https://github.com/dhairya0907/Creepypasta-Text-Generator](https://github.com/dhairya0907/Creepypasta-Text-Generator)

Project Web Application Link: [https://creepypasta-demo.vercel.app](https://creepypasta-demo.vercel.app)
