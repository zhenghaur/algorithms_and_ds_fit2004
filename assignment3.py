"""
Name: Lim Zheng Haur
Student ID: 32023952
Assignment 3
FIT2004
"""
#%%
# =================================================================
# Question 01
# =================================================================

def best_revenue(revenue, travel_days, start): 
    """
    This function computes the maximum possible revenue as a travelling salesman.

    Input:
        revenue: a day x city matrix containing the revenue of each city on each day
        travel_days: a city x city matrix containing the number of days to travel from each
                     city to another city or -1 indicating no direct road
        start: the starting city at day 0

    Return:
        the maximum possible revenue by the last day

    Time complexity: 
        Best: O(N^2 * D) where N = number of city, D = number of days
        Worst: O(N^2 * D) where N = number of city, D = number of days

    Space complexity: 
        Input: O(N(N + D)) where N = number of city, D = number of days
        Aux: O(N^2 * D) where N = number of city, D = number of days

    """
    def best_revenue_arg(day, city):
        """
        This is the recursive function to calculate the maximum revenue possible

        This function will recursively call itself until the it is the final day or the travel duration
        is more than the final day. Then it will use the values to make decisions to compare and compute the 
        maximum amount possibly earned on that day.

        Input: 
            day: the day to generate revenue
            city: the city to generate revenue 

        Return:
            The maximum amount of revenue possibly generated at that city on that day.

        Time complexity: 
            Best: O(N^2 * D) where N = number of city, D = number of days
            Worst: O(N^2 * D) where N = number of city, D = number of days

        Space complexity: 
            Input: O(1) 
            Aux: O(N^2 * D) where N = number of city, D = number of days

        """
        # base case (day out of consideration)
        if day > len(revenue) - 1:
            return 0

        # base case (last day)
        elif day == len(revenue) - 1:
            return revenue[day][city]

        else:
            # profit generated by staying at the same city
            profit = [revenue[day][city] + best_revenue_arg(day + 1, city)]

            # append profit generated if travelling to any possible city
            for next in range(len(travel_days)):
                if travel_days[city][next] != -1:
                    profit.append(best_revenue_arg(day + travel_days[city][next], next))

            # return maximum amount possible
            return max(profit)

    return best_revenue_arg(0, start)


# =================================================================
# Question 02
# =================================================================


def binary_search(attacks, index):
    """
    This function searches for the latest possible attack before the attack at input index

    This function will split the list in half each iteration to find the target. Therefore,
    the search space will decrease by half each iteration and the time complexity would be logN
    where N is the len(attacks)

    Input:
        attacks: a list of attacks (as a list of [multiverse, start, end, clones])
        index: the attack index to search latest possible attacks before

    Return:
        c: index of the latest possible attack
        None: if no possible attack

    Time complexity: 
        Best: O(logN) where N = len(attacks)
        Worst: O(logN) where N = len(attacks)

    Space complexity: 
        Input: O(N) where N = len(attacks)
        Aux: O(1)

    """
    a = 0
    b = index - 1
    while a <= b:
        c = (a + b)//2
        if attacks[c][2] < attacks[index][1]:
            if attacks[c + 1][2] < attacks[index][1]:
                a = c + 1
            else:
                return c
        else:
            b = c - 1
    return None


def hero(attacks):
    """
    Reference from https://www.geeksforgeeks.org/weighted-job-scheduling-log-n-time/

    This function returns a list of attacks that defeats the maximum amount of clones.

    This function first sorts the attacks list by the end day. Then a memo list is initialized
    and each iteration of attacks will store the maximum amount of clones killed, which multiverse 
    to attack, the previous multiverse to attack in a tuple. Using this, the path could be traced by 
    backtracking from the last tuple of memo.

    Input:
        attacks: a list of attacks (as a list of [multiverse, start, end, clones])

    Return:
        path: a list of attacks to defeat the maximum amount of clones

    Time complexity: 
        Best: O(NlogN) where N = len(attacks)
        Worst: O(NlogN) where N = len(attacks)
        
    Space complexity: 
        Input: O(N) where N = len(attacks)
        Aux: O(N) where N = len(attacks)

    """
    # sort attacks by end day
    attacks = sorted(attacks, key = lambda x: x[2])

    # initialize memo
    memo = [None] * len(attacks)

    # initialize first iteration of memo (no choices or decisions)
    memo[0] = (attacks[0][3], 0, None)

    for i in range(1, len(attacks)):
        # kills in that attack
        kills = attacks[i][3]

        # finding for previous possible attacks
        previous = binary_search(attacks, i)
        if previous != None:
            kills += memo[previous][0]
            previous = memo[previous][1]
        
        # decision (comparing)
        if kills > memo[i-1][0]:
            memo[i] = (kills, i, previous)
        else:
            memo[i] = memo[i - 1]

    # backtracking path rebuilding
    path = []
    previous = memo[-1][1]
    while previous != None:
        path.append(attacks[previous])
        previous = memo[previous][2]

    return path

if __name__ == "__main__":
    # something here

    travel_days = [[-1, 1, 1], [1, -1, 1], [1, 2, -1]]
    revenue = [[1, 2, 1], [3, 3, 1], [1, 1, 100]]
    start = 0
    profit = best_revenue(revenue, travel_days, start)

    attacks = [[1,1,2,50],[2,3,5,20],[3,6,19,100],[4,2,100,200],[5,20,30,120],[6,30,50,50],[7,25,60,150]]
    res = hero(attacks)
    res_total = 0
    for i in res:
        res_total+= i[3]
    
    if profit == 101 and res_total == 320:
        print("working")