class Solution(object):
    def minMovesToSeat(self, seats, students):
        """
        :type seats: List[int]
        :type students: List[int]
        :rtype: int
        """
        seats.sort()
        students.sort()
        count=0
        length=len(seats)
        for i in range(length):
            step=abs(seats[i]-students[i])
            count=count+step

        return count
