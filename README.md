# robert-heroku <img align = "right" height = "150" src = "assets/logo.png">
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Project Status: WIP – Initial development is in progress, but there has not yet been a stable, usable release suitable for the public.](https://www.repostatus.org/badges/latest/wip.svg)](https://www.repostatus.org/#wip)
<br>

Robert Bot exists with the purpose of bridging gaps between humans and AI through our very own versatile, deployable non-rule based chatbot. We wish to work on the GRU based Seq2Seq model to further use for tasks in the medical field.

## Tech-Stack

For this particular implementation we have worked out very own code from scratch for the sequential model by using PyTorch and further to provide a face to the project have used Streamlit.

Set up the python environment yourself by first cloning the repo<br>
```git clone https://github.com/Aakash-kaushik/robert-heroku```

Use the following command to install the libraries from [requirements.txt](requirements.txt)<br>
```pip install -r requirements.txt```

## Dataset

<img src="assets/data.png" width=1000>

For this project we decided to go for the Cornell Movie Dialogue Corpus, which served as a very good dataset because of the following features:
- 220,579 conversational exchanges between 10,292 pairs of movie characters
- involves 9,035 characters from 617 movies
- in total 304,713 utterances

Once we got the data, we proceessed the data by formatting unwanted metadata and created sentence pairs that could serve as historic data for our GRU Module.

For this particular project we decided to go for a lexical approach for the analysis of the data. In which we proceeded to group streams of letters and words from source into basic units of meaning called tokens.

## Architecture

<img src="assets/model.png" width=1000>

### Model
Chatbot is a sequence-to-sequence (seq2seq) model. The goal of a seq2seq model is to take a variable-length sequence as an input, and return a variable-length sequence as an output using a fixed-sized model.

## How to run it

Set up the python environment yourself by first cloning the repo<br>
```git clone https://github.com/Aakash-kaushik/robert-heroku```

Use the following command to install the libraries from [requirements.txt](requirements.txt)<br>
```pip install -r requirements.txt```

Run the webapplication<br>
```streamlit run app.py```

## Bot in Action

Here you can see our model in action, while hosted on a streamlit application.

<img src="assets/bot.gif">

However if you want to check out the full functionality of the project, you can check out the following link: [CLICK ME](!https://drive.google.com/file/d/1ne1f7s1jswVHZxB1p-FqGAH_Eay9HUS_/view?usp=sharing)

## License 
This project is under the Apache License. See [LICENSE](LICENSE) for Details.

