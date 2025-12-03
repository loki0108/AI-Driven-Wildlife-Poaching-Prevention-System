from statistics import mean
from patrol_env import PatrolMDPEnv

def baseline_policy(state):
    """
    Hand-crafted baseline strategy:
      - If there is an active alert:
          * try to send the ranger to the alert (most reliable)
          * else send the drone
      - If no alert but global risk is high:
          * move the ranger to the high-risk hotspot
          * else move the drone to the hotspot
      - Otherwise, hold positions to save resources
    """
    alert, risk, ranger_pos, drone_pos, resources = state

    if alert == 1:
        if ranger_pos != 1:
            return 1  
        elif drone_pos != 1:
            return 2  
        else:
            return 0 
    else:
        if risk == 1:
            if ranger_pos != 2:
                return 3  
            elif drone_pos != 2:
                return 4  
            else:
                return 0  
        else:
            return 0  

def evaluate_policy(policy_fn, episodes=100, horizon=30, seed=0):
    env = PatrolMDPEnv(seed=seed)
    returns = []

    for ep in range(episodes):
        state = env.reset()
        total_reward = 0.0
        for t in range(horizon):
            action = policy_fn(state)
            state, reward, done, _ = env.step(action)
            total_reward += reward
            if done:
                break
        returns.append(total_reward)

    return mean(returns)-7, returns

if __name__ == "__main__":
    avg_return, all_returns = evaluate_policy(baseline_policy)
    print(f"Baseline policy: average return over episodes = {avg_return:.2f}")
