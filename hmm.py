#!/usr/bin/env python

from numpy import zeros, float32
from pprint import pprint
import sys, hmmtrain, itertools

class hmm:        
    def __init__(self):
        priors, transitions, emissions, states, symbols = hmmtrain.train()
        self.priors = priors
        self.transitions = transitions
        self.emissions = emissions
        self.states = states
        self.symbols = symbols
    
    #takes a sentence o and exhaustively computes the 
    #most likely tag sequence. This method should compute 
    #the probability,for each possible tag sequence.
    #It should return the most likely tag
    #sequence and its associated probability.
    def exhaustive(self, o):
        sent = []
        for word in o.split():
            sent.append(word)
        # print sent
        total = 0
        prevTotal = 0
        bestTotal = 0
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

        sequence = []
        
        #go through each permutation
        for p in list(itertools.permutations(selected_states)):
            
            prevTotal = total
            
            for word in sent:
                #multiply the prior and the emission
                temp = self.priors.prob(p[count]) * \
                self.emissions[p[count]].prob(word)
                sequence.append(p[count])
                #multiply the current calculation against
                #the rest of this permutation
                total*= temp
                count+= 1

            #check to see if this is the most likely sequence
            if total < prevTotal:
                total = bestTotal
                bestSequence = sequence

            #output the most likely tag sequence
            #and its probability
            print "Most likely tag sequence: "
            print bestSequence
            print "Probability: "
            print bestTotal


    # performs Viterbi decoding to find the
    # most likely tag sequence for a given word sequence
    def decode(self, symbols):
        # VITERBI DECODING
        T = len(symbols)
        N = len(self.states)
        V = zeros((T, N), float32)
        B = {}


        for t in range(T):
            symbol = symbols[t]
            
            #initialization step
            if t == 0:
                for i in xrange(N):
                    state = self.states[i]
                    V[t, i] = self.priors.prob(state) * \
                              self.emissions[state].prob(symbol)
                    B[t, state] = None
            else:
                #recursion step
                for j in xrange(N):
                    sj = self.states[j]
                    best = None
                    for i in range(N):
                        si = self.states[i]
                        va = V[t-1, i] * self.transitions[si].prob(sj)
                        if not best or va > best[0]:
                            best = (va, si)
                    #termination steps
                    V[t, j] = best[0] * self.emissions[sj].prob(symbol)
                    B[t, sj] = best[1]

        best = None
        for i in xrange(N):
            val = V[T-1, i]
            if not best or val > best[0]:
                best = (val, self.states[i])


        current = best[1]
        sequence = [current]
        for t in xrange(T-1, 0, -1):
            last = B[t, current]
            sequence.append(last)
            current = last

        sequence.reverse()
        return sequence

    # takes a file with one (tokenized) sentence per line
    # as input and tags the words in the sentence using 
    # Viterbi decoding
    def tagViterbi(self, fname):
        content = []
        tagged_content = []
        count = 0
        
        #read in file with one tokenized sentence per line
        with open(fname) as f:
            content = f.readlines()

        # process each sentence/line
        for line in content:

            # decode the line using viterbi decoding
            tokens = line.split()
            best_sequence = self.decode(tokens)
            
            print "The best sequence is: "
            print pprint(best_sequence)
        
            
            # tag each word and store in tag list
            for word in tokens:
                
                #add tag to token
                word += "/"
                word += best_sequence[count]
                
                #add newly tagged word to array
                tagged_content.append(word)
                count += 1

        #convert list to string for printing display
        print " " .join(tagged_content)


def main():
    # Create an instance
    model = hmm()
    
    #model.exhaustive('You look around at professional ballplayers and nobody blinks an eye.')

    model.tagViterbi('sentences.txt')

    



if __name__ == '__main__':
    main()
