# Step 1: Use a lightweight official Python image
FROM python:3.11-slim

# Step 2: Set environment variables to avoid Python buffering and .pyc files
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Step 3: Set working directory
WORKDIR /app

# Step 4: Copy the requirements file
COPY requirements.txt .

# Step 5: Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Step 6: Copy the rest of the code into the container
COPY . .

# Step 7: Expose Flask port (if running in dev server)
EXPOSE 5000

# Step 8: Default command — runs the app
# Make sure your Python file that starts the app is named `app.py`
CMD ["python", "app.py"]
