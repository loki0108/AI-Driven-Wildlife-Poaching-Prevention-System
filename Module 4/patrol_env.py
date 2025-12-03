import random

class PatrolMDPEnv:
    """
    State = (alert, risk, ranger_pos, drone_pos, resources)
        alert       ∈ {0 (no active alert), 1 (active alert in some zone)}
        risk        ∈ {0 (low season risk), 1 (high poaching risk season/night)}
        ranger_pos  ∈ {0: idle/low-risk zone, 1: at alert zone, 2: at high-risk hotspot}
        drone_pos   ∈ {0: idle/low-risk zone, 1: at alert zone, 2: at high-risk hotspot}
        resources   ∈ {0: critically low, 1: moderate, 2: high fuel/stamina}

    Actions:
        0: Hold positions (monitor)
        1: Dispatch ranger to current alert (if any)
        2: Dispatch drone to current alert
        3: Reroute ranger to high-risk hotspot
        4: Reroute drone to high-risk hotspot
    """

    def __init__(self, seed=0):
        self.rng = random.Random(seed)
        self.state = None
        self.n_actions = 5

    def reset(self):
        alert = self.rng.choice([0, 1])      
        risk = self.rng.choice([0, 1])       
        ranger_pos = self.rng.choice([0, 2]) 
        drone_pos = self.rng.choice([0, 2])  
        resources = self.rng.choice([1, 2])  

        self.state = (alert, risk, ranger_pos, drone_pos, resources)
        return self.state

    def step(self, action):
        alert, risk, ranger_pos, drone_pos, resources = self.state

        if action == 1: 
            if alert == 1:
                ranger_pos = 1
        elif action == 2:  
            if alert == 1:
                drone_pos = 1
        elif action == 3:  
            ranger_pos = 2
        elif action == 4:  
            drone_pos = 2

        if action in [1, 2, 3, 4]:
            resources = max(0, resources - 1)

        reward = 0.0

        reward -= 0.5

        if alert == 1:
            event_prob = 0.5 if risk == 1 else 0.3
            if self.rng.random() < event_prob:
                if ranger_pos == 1 or drone_pos == 1:
                    reward += 15.0
                else:
                    reward -= 25.0
                alert = 0
        else:
            if risk == 1 and self.rng.random() < 0.2:
                if ranger_pos == 2 or drone_pos == 2:
                    reward += 10.0   
                else:
                    reward -= 20.0   

        if alert == 0 and risk == 1 and (ranger_pos == 2 or drone_pos == 2):
            reward += 1.0

        if resources == 0:
            reward -= 2.0

        if alert == 0:
            new_alert_prob = 0.25 if risk == 1 else 0.1
            if self.rng.random() < new_alert_prob:
                alert = 1

        if self.rng.random() < 0.1:
            risk = 1 - risk

        self.state = (alert, risk, ranger_pos, drone_pos, resources)
        done = False  

        return self.state, reward, done, {}

    def get_state_space(self):
        states = []
        for alert in [0, 1]:
            for risk in [0, 1]:
                for ranger in [0, 1, 2]:
                    for drone in [0, 1, 2]:
                        for res in [0, 1, 2]:
                            states.append((alert, risk, ranger, drone, res))
        return states
