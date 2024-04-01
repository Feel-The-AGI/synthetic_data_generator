# Synthetic Data Generator for Text Reports

## Overview
The Synthetic Data Generator is a Python tool designed to leverage OpenAI's GPT-3.5 model to create realistic text data. This tool can be particularly useful for generating datasets for training machine learning models or for any scenario where large amounts of text data are needed, but privacy concerns or data availability limit the use of real data.

## Features
- Utilizes OpenAI's powerful GPT-3.5-turbo-16k model for text generation due to its 16k output.
- Customizable parameters to control the diversity and uniqueness of generated text.
- Ability to generate large datasets of synthetic text data efficiently.
- Open-source for community collaboration and improvement.

## Prerequisites
Before you begin, ensure you have the following:
- Python 3.6 or higher.
- An OpenAI API key with access to GPT-3.5 models.

## Installation
Clone the repository to your local machine using:
```bash
git clone [[repository-link]](https://github.com/Jasiel-Stark8/synthetic_data_generator.git)
```
Navigate to the cloned directory and install the required packages using:
```
pip install -r requirements.txt
```

## Usage
To use the Synthetic Data Generator, follow these steps:
1. Import the `generate_synthetic_data` function from the script.
2. Call the function with the desired prompt and the number of data points to generate.

Example usage:
```python
from synthetic_data_generator import generate_synthetic_data

prompt = "Generate a report on the impact of climate change on global weather patterns."
synthetic_data_list = generate_synthetic_data(prompt, count=10)
for idx, data in enumerate(synthetic_data_list):
    print(f"Data point {idx + 1}: {data}")
```
Run in CLI:
```
python3 file.py >> data.txt
```

## Configuration
You can adjust the following parameters to fine-tune the data generation:
- `temperature`: Controls randomness. Higher values mean more creative responses.
- `top_p`: Controls the diversity of generated text.
- `frequency_penalty`: Decreases the likelihood of repetition.
- `presence_penalty`: Discourages the model from talking about topics it has already discussed.

## Contributing
Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".

Don't forget to give the project a star! Thanks again!

## License
Distributed under the MIT License. See `LICENSE` for more information.

## Contact
Singularity_engineer - [@Twitter](https://twitter.com/singularity_IA)
Jason Quist - [@LinkedIn](https://www.linkedin.com/in/jason-quist-4a0651261/)
Project Link: [Project](https://github.com/Jasiel-Stark8/synthetic_data_generator)

## Acknowledgments
- OpenAI for providing access to the GPT-3.5 API.
- Jason Quist for the initial development of the Synthetic Data Generator.
