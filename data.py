from openai import OpenAI

client = OpenAI(api_key='YOUR_OPENAI_API_KEY')

def generate_reviews(prompt, count=1):
    reviews = []
    for i in range(count):
        review_generated = False
        while not review_generated:
            try:
                # Generate a response using the ChatCompletion method
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo-16k",
                    messages=[
                        {"role": "system", "content": "You are a fast high quality covid text report generating assistant."},
                        {"role": "user", "content": prompt}
                    ],
                    temperature=0.7,
                    top_p=1,
                    frequency_penalty=1.7,
                    presence_penalty=1.6
                )
                review = response.choices[0].message.content.strip()
                word_count = len(review.split())
                print("word count:", word_count)
                print("counted")
                reviews.append(review)
                print(review)  # Add this line to print the generated review
                review_generated = True

                # Check if the word count is within the desired range
                if 15 <= word_count <= 70:
                    print("counted")
                    reviews.append(review)
                    review_generated = True

            except Exception as err:
                print(f"Encountered an error: {err}")

        # Optional: Add a slight variation to the prompt for next iteration
        prompt += " Provide another perspective."

    return reviews

# Corrected call to the function with a COVID-19 related prompt
generated_reviews = generate_reviews("give a high-quality full text report on  COVID-19.", count=10)

# Iterate over the generated reviews
for idx, review in enumerate(generated_reviews):
    print(f"Review {idx + 1}: {review}")
