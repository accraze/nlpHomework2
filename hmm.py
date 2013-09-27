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
        # print sent
        total = 0
        count = 0
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

       #  permutations = list(itertools.permutations(selected_states))

       # for item in permutations:
       #      for item in sent:
       #          temp self.emissions[]

        # for item in sent:
        #     for state in selected_states:
                
        #         temp = self.emissions[state].prob(item) * self.priors.prob(state)
    
        #         if temp > total:
        #             total = temp
        #             mle.update({item:state})
        #         count+=1
        # count = 0
        # total = 0
        # print mle


    def decode(self, symbols):
        # VITERBI DECODING
        T = len(symbols)
        N = len(self.states)
        V = zeros((T, N), float32)
        B = {}

        for t in range(T):
            symbol = symbols[t]
            if t == 0:
                for i in range(N):
                    state = self.states[i]
                    V[t, i] = self.priors.prob(state) * \
                              self.emissions[state].prob(symbol)
                    B[t, state] = None
            else:
                for j in range(N):
                    sj = self.states[j]
                    best = None
                    for i in range(N):
                        si = self.states[i]
                        va = V[t-1, i] * self.transitions[si].prob(sj)
                        if not best or va > best[0]:
                            best = (va, si)
                    V[t, j] = best[0] * self.emissions[sj].prob(symbol)
                    B[t, sj] = best[1]

        #print 'V', V
        #print 'B', B

        best = None
        for i in range(N):
            val = V[T-1, i]
            if not best or val > best[0]:
                best = (val, self.states[i])

        #print 'best', best

        current = best[1]
        sequence = [current]
        for t in range(T-1, 0, -1):
            last = B[t, current]
            sequence.append(last)
            current = last

        sequence.reverse()
        return sequence

    def tagViterbi(self, fname):
        content = []
        tagged_content = []
        with open(fname) as f:
            content = f.readlines()

        for line in content:
            print line
            # decode the line using viterbi decoding
            best_sequence = self.decode(line)
            count = 0
            for word in line :
                word += ("/" + best_sequence[count])
                count += 1

        for line in content:
            print line


        


            




    
    

def main():
    # Create an instance
    model = hmm()
    model.tagViterbi('test.txt')

    #model.exhaustive('big cats and dogs')



if __name__ == '__main__':
    main()
