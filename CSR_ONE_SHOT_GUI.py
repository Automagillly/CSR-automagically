import sys
from flask import Flask, request, send_file
import os
import subprocess
import zipfile
from io import BytesIO

app = Flask(__name__)

@app.route("/")
def index():
    return """
    <html>
    <body>
    <h1>Upload input file</h1>
    <form action="/upload" method="post" enctype="multipart/form-data">
    <input type="file" name="file">
    <input type="submit" value="Upload">
    </form>
    </body>
    </html>
    """

@app.route("/upload", methods=["POST"])
def upload_file():
    try:
        file = request.files["file"]
        file.save("CSR_infofile.csv")

        # Run your script with the input file
        subprocess.run([sys.executable, "Function_test.py", "CSR_infofile.csv"])

        # Create a zip file in memory
        buffer = BytesIO()
        with zipfile.ZipFile(buffer, 'w') as zip_file:
            for f in os.listdir('CSR'):
                if f.endswith(".csr"):
                    zip_file.write(os.path.join('CSR', f), f)

        # Return the zip file
        buffer.seek(0)
        return send_file(
            buffer,
            mimetype='application/zip',
            as_attachment=True,
            download_name='csr_files.zip'
        )

    except Exception as e:
        return str(e), 500

if __name__ == "__main__":
    app.run()
