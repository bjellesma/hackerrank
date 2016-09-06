import math
import gc

gc.set_threshold(0)
#get the number of steps
steps = raw_input('')
step = []
sum = 0
for i in range(0, int(steps)):
    step.append(raw_input(''))
#prob of a coin is 50%
coin_outcomes = 2
possibe_outcomes = pow(coin_outcomes, int(steps))
print 'Here are the possibe outcomes: %s' % possibe_outcomes
coin_prob = 1.0/float(possibe_outcomes)
print 'prob: %s' % coin_prob
step_sums = []
memory_addresses = []
subsumaddresses = []
for s1 in step:
    step_sums.append(int(s1))
    # pair s1 with each of the other
    subsum = 0
    subsumaddress = 0
    for s2 in step:
        if id(s1) != id(s2):
            print 'testing numbers: %s and %s' % (s1,s2)

            subsumaddress += hash(id(s2))
            print 'subsumaddress: %s' % subsumaddress
            memory_address = hash(id(s1)) + hash(id(s2))
            print 'memory_address: %s' % memory_address
            if memory_address not in memory_addresses:
                print 'memory_address not found in memory_addresses'
                print "adding %s and %s" % (s1, s2)
                step_sums.append(int(s1)+int(s2))
                #mark that we did this
                memory_addresses.append(memory_address)
                subsum += int(s2)
                print 'subsum: %s' % subsum

            if subsum != int(s2) and subsum != 0 and subsumaddress not in subsumaddresses:
                print 'subsum not s2 and subsumaddress not found in memory_addresses'
                print "adding %s and %s" % (s1, subsum)
                step_sums.append(int(s1)+int(subsum))
                subsumaddresses.append(subsumaddress)
print 'Here are the numbers we have now'
for s in step_sums:
    print s
expected_value = 0
for p in step_sums:
    expected_value += p * coin_prob
print expected_value
