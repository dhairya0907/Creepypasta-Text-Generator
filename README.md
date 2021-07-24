<!-- PROJECT LOGO -->

<p align="center">
  <a href="https://creepypasta-demo.vercel.app/">
    <img src="/Images/logo.png" alt="Logo" width="100" height="100">
  </a>

  <h3 align="center">Creepypasta - Text Generator(Website)</h3>

  <p align="center">
    Website which uses Deep Learning to generate horror stories.
    <br />
    <br />
    <a href="https://creepypasta-demo.vercel.app/">View Demo</a>
    ·
    <a href="https://github.com/dhairya0907/Creepypasta-Text-Generator">View Training Repo</a>
    ·
    <a href="https://github.com/dhairya0907/Creepypasta-Text-Generator-Website/issues">Report Bug</a>
    ·
    <a href="https://github.com/dhairya0907/Creepypasta-Text-Generator-Website/issues">Request Feature</a>
  </p>
</p>

<!-- PROJECT SHIELDS -->
<div align="center">
   <a target="_blank" href="https://github.com/dhairya0907/Creepypasta-Text-Generator-Website/blob/main/LICENSE"><img src="https://badgen.net/badge/license/MIT/blue"></a>
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

There are two parts to the project. One is the <a href="https://github.com/dhairya0907/Creepypasta-Text-Generator">Deep Learning model</a> which generates the text. The other is the <a href="https://creepypasta-demo.vercel.app/">website</a> which uses the model to generate text.

I have used <a href="https://github.com/dhairya0907/Creepypasta-Text-Generator">Deep Learning model</a> to generate text. It is a <a href="https://en.wikipedia.org/wiki/Neural_network">Neural Network</a> which uses <a href="https://en.wikipedia.org/wiki/Recurrent_neural_network">Recurrent Neural Network</a> to generate text.

I have hosted a model on  <a href="https://algorithmia.com/">Algorithmia</a> and used it's API to generate text.


### Built With
* [React Native](https://reactnative.dev/)
* [Algorithmia](https://algorithmia.com/)
* [Deployed using Vercel](https://vercel.com/)

### What I learned
* How to host Machine Learning models on Algorithmia.
* How to to develop a website using React Native.
* How to use Machine Learning model to generate text and display it on the website.



<!-- GETTING STARTED -->
## Getting Started

To host web application on user localhost follow below steps :

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* Follow the steps to Train and Host Machine Learning Model on [Creepypasta - Text Generator](https://github.com/dhairya0907/Creepypasta-Text-Generator).

* yarn
  ```sh
  npm install --global yarn
  ```

### Installation
1. Clone the repo
   ```sh
   git clone https://github.com/dhairya0907/Creepypasta-Text-Generator-Website.git
   ```
2. Install YARN packages
   ```sh
   yarn install
   ```
3. Run on localhost
   ```sh
   yarn web
   ```

4. Opens browser on http://localhost:3000/

**Note:** To avoid CORS issue while using Algorithmia, go to ```node_modules\algorithmia\lib``` and open file ```algorithm.js``` and change the line 
```js 
algorithmia.com/v1/algo/demo/Hello
  ``` 
  <p  align="center">to</p>

  ```js
  algorithmia.com/v1/web/algo/demo/Hello  <- CORS-enabled route
  ```
* Refer to [https://github.com/algorithmiaio/algorithmia-nodejs/issues/12](https://github.com/algorithmiaio/algorithmia-nodejs/issues/12) for more information.
<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/dhairya0907/Creepypasta-Text-Generator-Website/issues) for a list of proposed features (and known issues).



<!-- LICENSE -->
## License

Distributed under the MIT License. See [`LICENSE`](https://github.com/dhairya0907/Creepypasta-Text-Generator-Website/blob/main/LICENSE) for more information.



<!-- CONTACT -->
## Contact

Dhairya Sharma - [@dhairya_0907](https://twitter.com/dhairya_0907) - dhairya.sharma532@gmail.com.com

Project Github Link: [https://github.com/dhairya0907/Creepypasta-Text-Generator-Website](https://github.com/dhairya0907/Creepypasta-Text-Generator-Website)

Project Web Application Link: [https://creepypasta-demo.vercel.app](https://creepypasta-demo.vercel.app)
