# ------------------------------
# 1. Use official Python image
# ------------------------------
FROM python:3.13

# ------------------------------
# 2. Set working directory
# ------------------------------
WORKDIR /app

# ------------------------------
# 3. Copy project files
# ------------------------------
COPY . /app



# ------------------------------
# 5. Install Python dependencies
# ------------------------------
RUN pip install --no-cache-dir -r requirements.txt

# ------------------------------
# 6. Expose Flask port
# ------------------------------
EXPOSE 5000

# ------------------------------
# 7. Run the Flask app
# ------------------------------
CMD ["python", "app.py"]
