# robert-heroku <img align = "right" height = "100" src = "assets/logo.png">
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

<img src="assets/data.png" width=500>

For this project we decided to go for the Cornell Movie Dialogue Corpus, which served as a very good dataset because of the following features:
- 220,579 conversational exchanges between 10,292 pairs of movie characters
- involves 9,035 characters from 617 movies
- in total 304,713 utterances

## Architecture

<img src="assets/model.png" width=500>

### Model
Chatbot is a sequence-to-sequence (seq2seq) model. The goal of a seq2seq model is to take a variable-length sequence as an input, and return a variable-length sequence as an output using a fixed-sized model.
### Encoder
The encoder RNN iterates through the input sentence one token (e.g. word) at a time, at each time step outputting an “output” vector and a “hidden state” vector. The hidden state vector is then passed to the next time step, while the output vector is recorded. The encoder transforms the context it saw at each point in the sequence into a set of points in a high-dimensional space, which the decoder will use to generate a meaningful output for the given task.
### Decoder
The decoder RNN generates the response sentence in a token-by-token fashion. It uses the encoder’s context vectors, and internal hidden states to generate the next word in the sequence. It continues generating words until it outputs an EOS_token, representing the end of the sentence. A common problem with a vanilla seq2seq decoder is that if we rely solely on the context vector to encode the entire input sequence’s meaning, it is likely that we will have information loss. This is especially the case when dealing with long input sequences, greatly limiting the capability of our decoder.


## How can you run it

Set up the python environment yourself by first cloning the repo<br>
```git clone https://github.com/Aakash-kaushik/robert-heroku```

Use the following command to install the libraries from [requirements.txt](requirements.txt)<br>
```pip install -r requirements.txt```

Run the webapplication<br>
```streamlit run app.py```

## License 
This project is under the Apache License. See [LICENSE](LICENSE) for Details.