from flask import Flask, render_template, request, flash, redirect, url_for
import random
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Initialize the Flask application
app = Flask(__name__)

# Access the secret key
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY') # Set the secret key for session management and flash messages

# Predefined categories for the bio generator
careers = ['Software Engineer', 'Entrepreneur', 'Artist', 'Teacher', 'Chef', 'Musician']
interests = ['Cooking', 'Travel', 'Sports', 'Music', 'Literature', 'Gaming', 'Technology']
traits = ['Adventurous', 'Creative', 'Empathetic', 'Introverted', 'Outgoing']

# Bio templates
bio_templates = [
    "{trait} {career} who is passionate about {interest}.",
    "A {trait} professional with a love for {interest} and a career as a {career}.",
    "{career} by profession, {trait} by nature, and enjoys {interest} in free time.",
    "A {trait} individual, thriving in a {career} role, with a passion for {interest}.",
    "Driven by curiosity, this {career} is {trait} and enjoys {interest} in their free time.",
    "{career} by profession, {trait} by personality, and when not working, they love to {interest}.",
    "From {interest} to {career}, this {trait} individual brings their unique energy to everything they do.",
    "{career} with a flair for {interest}, always bringing their {trait} energy wherever they go.",
    "Passionate about {interest}, {trait} by nature, and building a career as a {career}.",
    "With a professional background in {career}, this {trait} individual enjoys {interest} outside of work.",
    "When they’re not being a {career}, you can find them {interest}, driven by their {trait} personality.",
    "A {trait} {career}, always learning and growing, with a deep love for {interest}.",
    "Quietly excelling as a {career}, this {trait} soul finds joy in {interest}.",
    "Combining a love for {interest} with a career in {career}, this {trait} individual believes in constant self-improvement.",
    "A {career} with a {trait} mindset, they balance work and play through a love for {interest}.",
    "A {trait} {career} who envisions a future full of {interest} and excitement.",
    "Always seeking new opportunities as a {career}, while {interest} keeps them grounded in the present.",
    "{trait} {career}, spending their free time {interest} to unwind and recharge.",
    "In the world of {career}, {trait} individuals like to spend their downtime {interest}.",
    "Taking on life as a {career}, they combine their {trait} mindset with a love for {interest}.",
    "A {trait} {career} exploring life and all its adventures through {interest}.",
    "A {trait} {career}, always reflecting on life while enjoying {interest}.",
    "They approach {career} with a {trait} spirit and find balance through a deep connection with {interest}."
]

# Homepage route
@app.route('/')
def index():
    """
    Render the homepage with dropdown options for career, interest, and trait.
    """
    return render_template('index.html', careers=careers, interests=interests, traits=traits)

# Generate bio route
@app.route('/generate_bio', methods=['POST'])
def generate_bio():
    """
    Handle the form submission to generate a personalized bio based on user input.

    Returns:
        - Renders a result page with the generated bio if successful.
        - Redirects back to the homepage with an error message if input is incomplete.
    """
    # Get user selections from the form
    career = request.form.get('career')
    interest = request.form.get('interest')
    trait = request.form.get('trait')

    # Validate form inputs
    if not career or not interest or not trait:
        flash("All fields must be selected.", 'error')  # Display an error message
        return redirect(url_for('index'))  # Redirect back to the form

    # Generate the bio using a random template
    template = random.choice(bio_templates)
    bio = template.format(career=career, interest=interest, trait=trait)

    # Render the result page with the generated bio
    return render_template('result.html', bio=bio)

# Run the application
if __name__ == '__main__':
    app.run(debug=True)