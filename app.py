from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

class Solution:
    def pancakeSortLevel1(self, A):
        flips = []

        if A[1] > A[0]:  # If the larger pancake is on top
            flips.append(2)  # Flip the entire stack
            flips.append(1)

        return flips if flips else None

    def pancakeSortLevel2(self, A):
        flips = []

        largest_idx = A.index(max(A))
        smallest_idx = A.index(min(A))

        if largest_idx != 1:  # Flip the largest pancake to the middle
            flips.append(largest_idx + 1)
            A[:largest_idx + 1] = A[:largest_idx + 1][::-1]

        if smallest_idx != 2:  # Flip the smallest pancake to the bottom
            flips.append(smallest_idx + 1)
            A[:smallest_idx + 1] = A[:smallest_idx + 1][::-1]

        return flips if flips else None

    # Implement Level 3 logic similarly...

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/flip_pancakes/<int:level>', methods=['POST'])
def flip_pancakes(level):
    pancake_sizes = request.get_json()
    solution = Solution()

    if level == 1:
        if len(pancake_sizes) == 2:
            flips = solution.pancakeSortLevel1(pancake_sizes)
            if flips:
                return jsonify({'flips': flips})
            else:
                return jsonify({'message': 'Pancakes already sorted'})
        else:
            return jsonify({'error': 'Invalid pancake sizes for Level 1'})

    elif level == 2:
        if len(pancake_sizes) == 3:
            flips = solution.pancakeSortLevel2(pancake_sizes)
            if flips:
                return jsonify({'flips': flips})
            else:
                return jsonify({'message': 'Pancakes already sorted'})
        else:
            return jsonify({'error': 'Invalid pancake sizes for Level 2'})

    # Implement Level 3 route similarly...

    return jsonify({'error': 'Unknown level'})

if __name__ == '__main__':
    app.run(debug=True)
