import gym
import numpy as np

# env=gym.make('CartPole-v0')
def run_episode(env,parameters):
    observation=env.reset()
    totalreward=0
    # again for 200 timesteps
    for k in xrange(200):
        env.render()
        action = 0 if np.matmul(parameters,observation<0) else 1
        observation,reward,done,info=env.step(action)
        totalreward+=reward
        if done:
            timesteps=k
            print "pole died after %d timesteps"%timesteps
            break
    return totalreward,timesteps

def train(submit):
    env=gym.make('CartPole-v0')
    scaling=0.1
    parameters_old=np.random.rand(4)*2-1
    timesteps=0
    bestreward=0
    # run it for 1000 episodes
    for i in xrange(1000):
        newparams=parameters_old+(np.random.rand(4)*2-1)*scaling
        reward_old,timesteps_old=run_episode(env,parameters_old)
        reward_new,timesteps_new=run_episode(env,newparams)
        print "reward_old = %d reward_new = %d"%(reward_old,reward_new)
        if reward_new>=reward_old:
            parameters_old=newparams
            timesteps_old=timesteps_new
            if(reward_new>bestreward):
                bestreward=reward_new
        else:
            if(reward_old>bestreward):
                bestreward=reward_old
        if bestreward==200:
            print "max reward attained. Exit"
            break
        print "episode ended in %d timesteps, bestreward = %d"%(timesteps_old,bestreward),i

r = train(submit=False)
print r



def naive_run(env):
    # for 20 episodes.
    for episodes in xrange(20):
        observation=env.reset()
        # for 200 timesteps. Upper limit is 200, our episode may terminate before 200 steps also
        for _ in xrange(200):
            env.render()
            print observation
            action=env.action_space.sample()
            observation, reward, done, info=env.step(action)
            if done:
                print "yo we is done"
                break
