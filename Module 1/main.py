from itertools import product

terrain_states = ['Dense','Open','Riverbed']
time_states    = ['Day','Night']
hist_states    = ['High','Medium','Low']
hm_states      = ['Present','Absent']
hotspot_states = ['Near','Far']
risk_states    = ['High','Medium','Low']
prior_terrain = {'Dense':0.6, 'Open':0.3, 'Riverbed':0.1}
prior_time    = {'Day':0.5,  'Night':0.5}
prior_hist    = {'High':0.3, 'Medium':0.4, 'Low':0.3}
prior_hotspot = {'Near':0.2,'Far':0.8}
cpt_hm = {('Day','Present'):0.1, ('Day','Absent'):0.9,
          ('Night','Present'):0.5, ('Night','Absent'):0.5}

def risk_cpt(terrain, time, hist, hm, hotspot):
    score = 0
    score += 2 if terrain=='Riverbed' else 1 if terrain=='Dense' else 0
    score += 1 if time=='Day' else 0
    score += 2 if hist=='High' else 1 if hist=='Medium' else 0
    score += 2 if hm=='Present' else 0
    score += 2 if hotspot=='Near' else 0
    if score >= 5:
        return [0.8, 0.15, 0.05]
    elif score >= 3:
        return [0.5, 0.4, 0.1]
    elif score >= 1:
        return [0.2, 0.5, 0.3]
    else:
        return [0.1, 0.3, 0.6]

def joint_prob(terrain, time, hist, hm, hotspot, risk):
    p = prior_terrain[terrain] * prior_time[time] * prior_hist[hist] * prior_hotspot[hotspot]
    p *= cpt_hm[(time, hm)]
    p *= risk_cpt(terrain, time, hist, hm, hotspot)[ risk_states.index(risk) ]
    return p

def posterior_risk(evidence):
    num = {r:0.0 for r in risk_states}
    denom = 0.0
    for (terrain, time, hist, hm, hotspot, risk) in product(terrain_states, time_states, hist_states, hm_states, hotspot_states, risk_states):
        assign = {'Terrain':terrain,'Time':time,'Hist':hist,'Human':hm,'Hotspot':hotspot,'Risk':risk}
        if any(assign[var]!=val for var,val in evidence.items()):
            continue
        p = joint_prob(terrain,time,hist,hm,hotspot,risk)
        num[risk] += p
        denom     += p
    if denom==0: return None
    return {r: num[r]/denom for r in risk_states}

evidence = {'Terrain':'Dense','Time':'Night','Hist':'Medium','Hotspot':'Near'}
post = posterior_risk(evidence)
print("P(PoachingRisk | evidence) =", post)