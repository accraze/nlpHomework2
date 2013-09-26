#!/usr/bin/env python

from numpy import zeros, float32
import sys, hmmtrain
import itertools

class hmm:        
    def __init__(self):
        priors, transitions, emissions, states, symbols = hmmtrain.train()
        self.priors = priors
        self.transitions = transitions
        self.emissions = emissions
        self.states = states
        self.symbols = symbols
    
    ####
    # ADD METHODS HERE
    ####

    def exhaustive(self, o):
        sent = []
        for word in o.split():
            sent.append(word)
        print sent
        total = 0
        selected_states = []
        
        #load list... 17 HIDDEN STATES
        selected_states.append(self.states[2])
        selected_states.append(self.states[7])
        selected_states.append(self.states[9])
        selected_states.append(self.states[11])
        selected_states.append(self.states[12])
        selected_states.append(self.states[14])
        selected_states.append(self.states[16])
        selected_states.append(self.states[17])
        selected_states.append(self.states[19])
        selected_states.append(self.states[21])
        selected_states.append(self.states[22])
        selected_states.append(self.states[25])
        selected_states.append(self.states[26])
        selected_states.append(self.states[27])
        selected_states.append(self.states[29])
        selected_states.append(self.states[37])
        selected_states.append(self.states[44])
        selected_states.append(self.states[45])

        mle = {}
        count = 0
        
        
        for item in sent:
            for state in selected_states:
                
                temp = self.emissions[state].prob(item) * self.priors.prob(state)
    
                if temp > total:
                    total = temp
                    mle.update({item:state})
                count+=1
        count = 0
        total = 0
        print mle


            



    # def decode(self, sequence):
    #     sent = sequence.split()
    #     print viterbi_parser = nltk.viterbi_parser
    # def tagViterbi (self,sentence):
    #     #Return the best path, given an HMM model and a sequence of observations"""
    #     # A - initialise stuff
    #     nSamples = len(observations[0])
    #     nStates = self.transition.shape[0] # number of states
    #     c = np.zeros(nSamples) #scale factors (necessary to prevent underflow)
    #     viterbi = np.zeros((nStates,nSamples)) # initialise viterbi table
    #     psi = np.zeros((nStates,nSamples)) # initialise the best path table
    #     best_path = np.zeros(nSamples); # this will be your output

    #     # B- appoint initial values for viterbi and best path (bp) tables - Eq (32a-32b)
    #     viterbi[:,0] = self.priors.T * self.emission[:,observations(0)]
    #     c[0] = 1.0/np.sum(viterbi[:,0])
    #     viterbi[:,0] = c[0] * viterbi[:,0] # apply the scaling factor
    #     psi[0] = 0;

    #     # C- Do the iterations for viterbi and psi for time>0 until T
    #     for t in range(1,nSamples): # loop through time
    #         for s in range (0,nStates): # loop through the states @(t-1)
    #             trans_p = viterbi[:,t-1] * self.transition[:,s]
    #             psi[s,t], viterbi[s,t] = max(enumerate(trans_p), key=operator.itemgetter(1))
    #             viterbi[s,t] = viterbi[s,t]*self.emission[s,observations(t)]

    #         c[t] = 1.0/np.sum(viterbi[:,t]) # scaling factor
    #         viterbi[:,t] = c[t] * viterbi[:,t]

    #     # D - Back-tracking
    #     best_path[nSamples-1] =  viterbi[:,nSamples-1].argmax() # last state
    #     for t in range(nSamples-1,0,-1): # states of (last-1)th to 0th time step
    #         best_path[t-1] = psi[best_path[t],t]

    #     return best_path
    


def main():
    # Create an instance
    model = hmm()

    model.exhaustive('big cats and dogs')


if __name__ == '__main__':
    main()
