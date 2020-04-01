import math


seen_primes = set()
num_hits = 0
num_seeks = 0
def is_prime(subj):
    global num_hits
    global num_seeks
    if subj in seen_primes:
        num_hits += 1
        return True
    num_seeks += 1
    frac, whole = math.modf(subj)
    if frac:
        return False
    if subj in [1,2]:
        seen_primes.add(subj)
        return True
    if subj % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(subj))+1, 2):
        if subj % i == 0:
            return False
    # print("I think {} is prime".format(subj))
    seen_primes.add(subj)
    return True

num_factorizations = 0
seen_subjects = {}

def prime_factors(subj, max_N = None):
    global num_factorizations
    
    str_subj = str(subj)
    if str_subj in seen_subjects:
        return seen_subjects[str_subj]
    num_factorizations += 1
    if not max_N:
        max_N = subj
    upper_bound = int(math.sqrt(subj))+1
    upper_bound = min(upper_bound, max_N)
    if upper_bound %2 == 0:
        upper_bound -= 1
    # print("factoring {}, limiting to < {}".format(subj, upper_bound))
    for divisor in range(upper_bound, 2, -2):
        quotient = subj / divisor
        frac, whole = math.modf(quotient)
        if frac:
            continue
        if not is_prime(divisor):
            continue
        if not is_prime(quotient):
            continue
        # print("Factors for {} found to be {} x {}".format(subj, divisor, quotient))
        result =  (int(divisor), int(quotient))
        seen_subjects[str_subj] = result
        return result
    raise Exception("there were no prime factors for {}".format(subj))

def main():
    global num_factorizations
    global num_seeks
    global num_hits
    
    num_cases = input()
    output_chars = [c for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
    for c in range(1, int(num_cases) + 1):
        # print("\n\nCASE {}\n=========\n".format(c))
        max_N, num_cipherwords = map(int, input().split(" "))
        ciphers = [i for i in map(int, input().split(" "))]
        last_finds = (None, None)
        output = []
        discovered_factors = set()
        for i in range(0, num_cipherwords):
            word = ciphers[i]
            # print("Working on word: {}".format(word))
            last_div, last_quo = last_finds
            if last_div and last_quo:
                if i+1 == num_cipherwords:
                    # print("last word... still thinking... ")
                    pass
                if len(output) == 0:
                    # print("no output discovered yet...")
                    # FIRST WORD... we need to find the order 
                    # try DIV+QUO first
                    candidate_quo_lr = word / last_div
                    candidate_quo_rl = word / last_quo
                    if is_prime(candidate_quo_lr):
                        # this means the quotient comes first in the previous factors
                        output.append(last_quo)
                        output.append(last_div)
                        output.append(candidate_quo_lr)
                        last_finds = (last_div, candidate_quo_lr)
                        discovered_factors.add(candidate_quo_lr)
                    elif is_prime(candidate_quo_rl):
                        # this means the divisor comes first...
                        output.append(last_div)
                        output.append(last_quo)
                        output.append(candidate_quo_rl)
                        last_finds = (last_quo, candidate_quo_rl)
                        discovered_factors.add(candidate_quo_rl)
                    else:
                        pass
                else:
                    # we should be able to just "factor forward..."
                    new_quo = word / last_quo
                    if not is_prime(new_quo):
                        pass
                    else:
                        output.append(new_quo)
                        discovered_factors.add(new_quo)
                        last_finds = (last_quo, new_quo)
            else:
                divisor, quotient = prime_factors(word, max_N)
                last_finds = (divisor, quotient)
                discovered_factors.add(divisor)
                discovered_factors.add(quotient)
        foo = sorted([int(factor) for factor in discovered_factors])
        out = [output_chars[foo.index(ch)] for ch in output]
        print("Case #{0}: {1}".format(c, "".join(out)))
        num_factorizations = 0
        num_seeks = 0
        num_hits = 0

if __name__ == "__main__":
    main()
