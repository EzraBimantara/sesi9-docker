# Gunakan Python sebagai base image
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy semua file ke dalam container
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# Jalankan aplikasi
CMD ["python", "app.py"]
