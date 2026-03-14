from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/evaluate', methods=['POST'])
def evaluate():
    data = request.json
    n = data.get('n')
    cells_data = data.get('cellsData')
    end_index = data.get('endIndex')

# Configs
GAMMA = 0.9
R_STEP = -1
R_GOAL = 10
R_OBSTACLE = -1
ACTIONS = ['U', 'D', 'L', 'R']

def get_next_state(idx, action, n, cells_data):
    r, c = idx // n, idx % n
    if action == 'U': r -= 1
    elif action == 'D': r += 1
    elif action == 'L': c -= 1
    elif action == 'R': c += 1

    if r < 0 or r >= n or c < 0 or c >= n:
        return idx
    
    next_idx = r * n + c
    if cells_data[next_idx] == 'obstacle':
        return idx
        
    return next_idx

@app.route('/generate_random_policy', methods=['POST'])
def generate_random_policy():
    data = request.json
    n = data.get('n')
    cells_data = data.get('cellsData')
    end_index = data.get('endIndex')
    
    import random
    pi_random = [None for _ in range(n * n)]
    for i in range(n * n):
        if cells_data[i] == 'obstacle' or i == end_index:
            continue
        pi_random[i] = random.choice(ACTIONS)
        
    return jsonify({'pi': pi_random})

@app.route('/evaluate_policy', methods=['POST'])
def evaluate_policy():
    data = request.json
    n = data.get('n')
    cells_data = data.get('cellsData')
    end_index = data.get('endIndex')
    pi = data.get('pi')
    
    V = [0.0 for _ in range(n * n)]
    max_diff = 1.0
    iters = 0
    
    while max_diff > 1e-5 and iters < 1000:
        max_diff = 0.0
        new_v = list(V)
        
        for i in range(n * n):
            if cells_data[i] == 'obstacle' or i == end_index:
                new_v[i] = 0.0
                continue
                
            a = pi[i]
            next_idx = get_next_state(i, a, n, cells_data)
            
            reward = R_STEP
            if next_idx == i:
                reward = R_OBSTACLE
                
            next_v = 0.0
            if next_idx == end_index:
                reward = R_GOAL
            else:
                next_v = V[next_idx]
                
            v = reward + GAMMA * next_v
            max_diff = max(max_diff, abs(v - V[i]))
            new_v[i] = v
            
        V = new_v
        iters += 1

    return jsonify({'V': V})

@app.route('/value_iteration', methods=['POST'])
def value_iteration():
    data = request.json
    n = data.get('n')
    cells_data = data.get('cellsData')
    end_index = data.get('endIndex')

    V = [0.0 for _ in range(n * n)]
    pi = [None for _ in range(n * n)]
    max_diff = 1.0
    iters = 0

    while max_diff > 1e-5 and iters < 1000:
        max_diff = 0.0
        new_v = list(V)

        for i in range(n * n):
            if cells_data[i] == 'obstacle' or i == end_index:
                new_v[i] = 0.0
                continue

            max_action_val = float('-inf')
            best_action = None

            for a in ACTIONS:
                next_idx = get_next_state(i, a, n, cells_data)
                reward = R_STEP
                if next_idx == i:
                    reward = R_OBSTACLE
                    
                next_v = 0.0
                if next_idx == end_index:
                    reward = R_GOAL
                else:
                    next_v = V[next_idx]

                v = reward + GAMMA * next_v
                if v > max_action_val:
                    max_action_val = v
                    best_action = a

            max_diff = max(max_diff, abs(max_action_val - V[i]))
            new_v[i] = max_action_val
            pi[i] = best_action

        V = new_v
        iters += 1

    return jsonify({
        'V': V,
        'pi': pi
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
