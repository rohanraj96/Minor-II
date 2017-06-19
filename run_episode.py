import numpy as np
import gym

def run_episode(env,parameters):
    observation=env.reset()
    totalreward=0
    for _ in xrange(200):
        env.render()
        action=0 if np.matmul(parameters,observation)<0 else 1
        observation,reward,done,info=env.step(action)
        totalreward+=reward
        if done:
            break
    return totalreward
