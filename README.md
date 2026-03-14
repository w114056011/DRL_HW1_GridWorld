# Retro Grid World: Policy Evaluation & Value Iteration

A web-based interactive application built with Flask and Vanilla HTML/JS to visualize fundamental Reinforcement Learning concepts: **Policy Evaluation** and **Value Iteration** on a customizable grid map.

# 網格地圖與價值迭代 (Value Iteration)
👉 **[點此馬上體驗 Live Demo](https://drl-hw1-gridworld-aezt.onrender.com)**

## 🌟 Features

- **Interactive Grid Map**: Users can customize the grid dimensions (from $n=5$ to $n=9$) and interactively set the Start state (Green), End state (Red), and Obstacles (Gray) using mouse clicks.
- **Retro Pixel-Art Aesthetic**: The UI is designed with a nostalgic 8-bit arcade style, utilizing the `DotGothic16` font, chunky borders, and high-contrast retro colors.
- **Step-by-Step Execution**: The visualization process is broken down into three logical steps for educational clarity:
  1. **[1. 產生隨機策略] (Generate Random Policy)**: Assigns a random action (Up, Down, Left, Right) to every valid state.
  2. **[2. 評估隨機策略] (Evaluate Random Policy)**: Uses the Iterative Policy Evaluation algorithm to compute the expected value $V(s)$ for each state under the random policy.
  3. **[3. 執行價值迭代] (Value Iteration)**: Executes the Value Iteration algorithm to discover the optimal value function $V^*(s)$ and extracts the optimal policy $\pi^*(s)$.
- **Split UI Comparison**: Displays both the Random Policy results (HW1-2) and the Optimal Policy results (HW1-3) side-by-side for easy comparison.
- **Optimal Path Highlighting**: Automatically traces and highlights the optimal path from the Start state to the End state using a distinct golden pixel aesthetic.

## 🛠️ Technology Stack

- **Backend**: Python, Flask (Handles API endpoints and MDP algorithm computations)
- **Frontend**: HTML5, CSS3, JavaScript (Handles DOM manipulation, state management, and asynchronous `fetch` requests)

## 🚀 How to Run

1. Ensure you have Python installed. If you created a virtual environment, activate it:
   ```bash
   source venv/bin/activate
   ```
2. Install the necessary dependencies (Flask):
   ```bash
   pip install Flask
   ```
3. Start the Flask development server:
   ```bash
   python app.py
   ```
4. Open your web browser and navigate to `http://127.0.0.1:5000/`.

## 🧠 Algorithm Configuration (MDP)

The Reinforcement Learning environment (Markov Decision Process) is configured in `app.py` with the following parameters:
- **Gamma ($\gamma$)**: `0.9` (Discount factor)
- **Reward for normal step ($R_{step}$)**: `-1`
- **Reward for reaching the goal ($R_{goal}$)**: `10`
- **Reward for hitting an obstacle/wall ($R_{obstacle}$)**: `-1` (Agent stays in place)

## 📂 Project Structure

- `app.py`: The Flask server containing the routing and the backend RL algorithms logic.
- `templates/index.html`: The frontend layout, styling, and JavaScript interaction logic.
- `Prompt.md`: Development log detailing the progression of prompts and AI actions used to build this project.
