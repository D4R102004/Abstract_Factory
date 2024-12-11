# Step 1: Use the official Python image as the base image
FROM python:3.8-slim

# Step 2: Set the working directory inside the container
WORKDIR /app

# Step 3: Copy the requirements file into the container (if you have one, or install Flask directly)
# If you don’t have a `requirements.txt`, you can skip copying that file.
COPY requirements.txt /app/

# Step 4: Install the required dependencies (Flask in this case)
RUN pip install --no-cache-dir -r requirements.txt


# Step 5: Copy the rest of your Flask application into the container
COPY . /app

# Step 6: Expose the port that the Flask app will run on
EXPOSE 5000

# Step 7: Set the environment variable for Flask to run in production mode
ENV FLASK_APP=abs_fact.py
ENV FLASK_ENV=production

# Step 8: Set the command to run the Flask application
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
