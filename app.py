from flask import Flask, request, jsonify, render_template
from sort import insertion_sort, selection_sort, bubble_sort, merge_sort, quick_sort

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/insertion_sort_steps', methods=['POST'])
def insertion_sort_steps():
    data = request.json
    array = data.get('array', [])
    steps = insertion_sort(array)
    return jsonify(steps)

@app.route('/selection_sort_steps', methods=['POST'])
def selection_sort_steps():
    data = request.json
    array = data.get('array', [])
    steps = selection_sort(array)
    return jsonify(steps)

@app.route('/bubble_sort_steps', methods=['POST'])
def bubble_sort_steps():
    data = request.json
    array = data.get('array', [])
    steps = bubble_sort(array)
    return jsonify(steps)

@app.route('/merge_sort_steps', methods=['POST'])
def merge_sort_steps():
    data = request.json
    array = data.get('array', [])
    merge_sort(array, 0, len(array) - 1)
    steps = [array.copy()]  # Only one step in merge sort: the final sorted array
    return jsonify(steps)

@app.route('/quick_sort_steps', methods=['POST'])
def quick_sort_steps():
    data = request.json
    array = data.get('array', [])
    quick_sort(array, 0, len(array) - 1)
    steps = [array.copy()]  # Only one step in quick sort: the final sorted array
    return jsonify(steps)

if __name__ == '__main__':
    app.run(debug=True)
