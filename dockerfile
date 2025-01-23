FROM python:3.12.4

# Set the working directory
WORKDIR /Blog_API

# Copy application files
COPY . /Blog_API

# Install dependencies
RUN pip install -r requirements.txt

# Expose the FastAPI default port
EXPOSE 8000

# Start the application with Uvicorn
CMD ["fastapi", "run", "app/main.py"]
