from search import *

class MissCannibalsVariant(Problem):
    """ The problem of Missionaries and Cannibals. 
    N1 and N2 are the total number of missionaries and cannibals starting from the left bank.
    A state is represented as a 3-tuple, two numbers and a boolean:
    state[0] is the number of missionaries on the left bank (note: the number of missionaries on the right bank is N1-m)
    state[1] is the number of cannibals on the left bank (note: the number of cannibals on the right bank is N2-c)
    state[2] is true if boat is at the left bank, false if at the right bank """

    def __init__(self, N1=4, N2=4, goal=(0, 0, False)):
        """ Define goal state and initialize a problem """
        initial = (N1, N2, True)
        self.N1 = N1
        self.N2 = N2
        super().__init__(initial, goal)
    
    def goal_test(self, state):
        if isinstance(self.goal, list):
            return is_in(state, self.goal)
        else:
            return state == self.goal
    
    def actions(self, state):
        
        possible_actions = ['M', 'C', 'MM', 'MC', 'CC', 'MMM', 'MMC', 'CCC']
        
        boatIsAtLeftBank = state[2]
        missionariesOnLeftBank = state[0]
        cannibalsOnLeftBank = state[1]

        missionariesOnRightBank = self.N1 - state[0]
        cannibalsOnRightBank = self.N2 - state[1]

        """ 1st: Remove actions that have a greater number of Missionaries or Cannibals than actually available"""
        if boatIsAtLeftBank:
            for action in possible_actions[:]:
                if action.count('M') > missionariesOnLeftBank and action in possible_actions:
                    possible_actions.remove(action)
                if action.count('C') > cannibalsOnLeftBank and action in possible_actions:
                    possible_actions.remove(action)
        else:
            for action in possible_actions[:]:
                if action.count('M') > missionariesOnRightBank and action in possible_actions:
                    possible_actions.remove(action)
                if action.count('C') > cannibalsOnRightBank and action in possible_actions:
                    possible_actions.remove(action)
        
        """2nd: Remove actions that would make MissonariesOnRightBank < CannibalsOnRightBank or MissionariesOnLeftBank < CannibalsOnLeftBank"""
        if boatIsAtLeftBank:
            for action in possible_actions[:]:
                """Checking if the number of cannibals to be sent to the right bank will out number the missionaries on the right bank but its okay if missionaries == 0 at right bank after action"""
                if action.count('C') + cannibalsOnRightBank > missionariesOnRightBank + action.count('M') and missionariesOnRightBank!= 0 and action in possible_actions:
                    possible_actions.remove(action)
                """Checking if the number of missionaries remaining on the left bank will be outnumbered by the cannibals on the left bank, but its okay if missionaries == 0 after action"""
                if missionariesOnLeftBank - action.count('M') < cannibalsOnLeftBank - action.count('C') and missionariesOnLeftBank - action.count('M') != 0 and action in possible_actions:
                    possible_actions.remove(action)
        else:
            for action in possible_actions[:]:
                """Checking to see if the cannibals to be sent back to the left bank will out number the missionaries on the left bank"""
                if (action.count('C') + cannibalsOnLeftBank) > (missionariesOnLeftBank + action.count('M')) and missionariesOnLeftBank != 0 and action in possible_actions:
                    possible_actions.remove(action)
                """Checking to see if the number missionaries remaining on the right bank will be outnumbered by the cannibals on the right bank"""
                if (missionariesOnRightBank - action.count('M') < cannibalsOnRightBank - action.count('C')) and missionariesOnRightBank - action.count('M') != 0 and action in possible_actions:
                    possible_actions.remove(action)
                
        return possible_actions


    def result(self, state, action):
        if state[2] == True:
            numOfMissionary = state[0] - action.count('M')
            numOfCannibal = state[1] - action.count('C')
        else:
            numOfMissionary = state[0] + action.count('M')
            numOfCannibal = state[1] + action.count('C')

        boatLocation = not state[2]

        newState = (numOfMissionary, numOfCannibal, boatLocation)

        return newState


if __name__ == '__main__':
    mc = MissCannibalsVariant(4,4)
    #print(mc.actions((3, 3, True))) # Test your code as you develop! This should return  ['MC', 'MMM']

    # path = depth_first_graph_search(mc).solution()
    # print(path)
    path = breadth_first_graph_search(mc).solution()
    print(path)

    