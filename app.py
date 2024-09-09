from flask import Flask, request, jsonify, render_template
from sort import insertion_sort, merge_sort, quicksort, counting_sort, radix_sort

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sort', methods=['POST'])
def sort_array():
    data = request.json
    arr = data.get("array")
    algorithm = data.get("algorithm")

    if algorithm == 'insertion_sort':
        sorting_steps = list(insertion_sort(arr))
    elif algorithm == 'merge_sort':
        sorting_steps = list(merge_sort(arr))
    elif algorithm == 'quicksort':
        sorting_steps = list(quicksort(arr))
    elif algorithm == 'counting_sort':
        sorting_steps = list(counting_sort(arr))
    elif algorithm == 'radix_sort':
        sorting_steps = list(radix_sort(arr))
    else:
        return jsonify({"error": "Invalid algorithm"}), 400

    return jsonify(sorting_steps)

if __name__ == '__main__':
    app.run(debug=True)
