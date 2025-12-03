from collections import defaultdict
from statistics import mean
from patrol_env import PatrolMDPEnv
from oliver_mdp_baseline import baseline_policy, evaluate_policy as eval_baseline
import random

class QLearningAgent:
    def __init__(self, n_actions, alpha=0.1, gamma=0.95, epsilon=0.3):
        self.n_actions = n_actions
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.q = defaultdict(lambda: [0.0] * n_actions)

    def select_action(self, state):
        if random.random() < self.epsilon:
            return random.randrange(self.n_actions)
        qs = self.q[state]
        return qs.index(max(qs))

    def update(self, state, action, reward, next_state):
        best_next = max(self.q[next_state])
        td_target = reward + self.gamma * best_next
        td_error = td_target - self.q[state][action]
        self.q[state][action] += self.alpha * td_error

    def greedy_policy(self, state):
        qs = self.q[state]
        return qs.index(max(qs))


def train_q_learning(
    episodes=300,
    horizon=30,
    alpha=0.1,
    gamma=0.95,
    epsilon_start=0.3,
    epsilon_end=0.05,
    seed=0
):
    env = PatrolMDPEnv(seed=seed)
    agent = QLearningAgent(n_actions=env.n_actions, alpha=alpha, gamma=gamma, epsilon=epsilon_start)

    episode_returns = []
    for ep in range(episodes):
        agent.epsilon = max(epsilon_end, epsilon_start - (epsilon_start - epsilon_end) * (ep / episodes))

        state = env.reset()
        total_reward = 0.0

        for t in range(horizon):
            action = agent.select_action(state)
            next_state, reward, done, _ = env.step(action)
            agent.update(state, action, reward, next_state)
            state = next_state
            total_reward += reward

        episode_returns.append(total_reward)

    return agent, episode_returns


def evaluate_trained_agent(agent, episodes=200, horizon=30, seed=21):
    env = PatrolMDPEnv(seed=seed)
    returns = []

    for ep in range(episodes):
        state = env.reset()
        total_reward = 0.0
        for t in range(horizon):
            action = agent.greedy_policy(state)
            state, reward, done, _ = env.step(action)
            total_reward += reward

        returns.append(total_reward)

    return mean(returns), returns


if __name__ == "__main__":
    print("Training Q-learning agent...")
    agent, train_returns = train_q_learning()

    print(f"Last episode training reward: {train_returns[-1]:.3f}")

    baseline_avg, _ = eval_baseline(baseline_policy)
    print(f"Baseline policy average return: {baseline_avg:.3f}")

    learned_avg, _ = evaluate_trained_agent(agent)
    print(f"Q-learning learned policy average return: {learned_avg:.3f}")
