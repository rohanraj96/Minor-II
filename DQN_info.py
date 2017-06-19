import gym

env=gym.make('CartPole-v0')
print env.observation_space.shape[0]
print env.action_space.n
