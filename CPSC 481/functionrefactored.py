"""Key Improvements
	1.	Encapsulation of Logic
	•	Extracted the validity checks into a helper function is_valid(action), making the code modular and easier to follow.
	2.	Eliminated Redundant Loops
	•	Instead of iterating over possible_actions multiple times and removing elements, we filter the list using list comprehension.
	3.	Removed Unnecessary Checks
	•	Avoided checking action in possible_actions before removing it.
	•	Combined checks logically to prevent unnecessary repeated calculations.
	4.	Better Readability & Naming Conventions
	•	Used boat_is_at_left for better clarity.
	•	Used m_count and c_count instead of repeated action.count('M')."""

def actions(self, state):
    possible_actions = ['M', 'C', 'MM', 'MC', 'CC', 'MMM', 'MMC', 'CCC']
    
    boat_is_at_left = state[2]
    missionaries_left = state[0]
    cannibals_left = state[1]
    
    missionaries_right = self.N1 - missionaries_left
    cannibals_right = self.N2 - cannibals_left

    def is_valid(action):
        """Check if an action is valid given the current state."""
        m_count = action.count('M')
        c_count = action.count('C')

        # Determine the number of missionaries and cannibals after moving
        if boat_is_at_left:
            m_left_new, c_left_new = missionaries_left - m_count, cannibals_left - c_count
            m_right_new, c_right_new = missionaries_right + m_count, cannibals_right + c_count
        else:
            m_left_new, c_left_new = missionaries_left + m_count, cannibals_left + c_count
            m_right_new, c_right_new = missionaries_right - m_count, cannibals_right - c_count

        # Ensure we are not taking more than available
        if m_count > missionaries_left if boat_is_at_left else m_count > missionaries_right:
            return False
        if c_count > cannibals_left if boat_is_at_left else c_count > cannibals_right:
            return False

        # Ensure missionaries are never outnumbered by cannibals (unless zero missionaries)
        if (m_right_new < c_right_new and m_right_new != 0) or (m_left_new < c_left_new and m_left_new != 0):
            return False

        return True

    return [action for action in possible_actions if is_valid(action)]