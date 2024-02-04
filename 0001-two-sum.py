class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numMap = {}
        for index, num in enumerate(nums):
            if numMap.get(num) != None:
                return [index, numMap[num]]
            else:
                curr = target - num
                numMap[curr] = index
                print(numMap)
        
        # other version
        # if num in numMap:

class main():
  solution = Solution()
  print(solution.twoSum([3, 2, 3], 6))
  
  """_summary_
  Passa no vetor "assimilando" o maximo de informacao em uma percorrida só
  Salva o valor que eu quero encontrar e a posicao em um hashmap (pq a checagem é instantanea)
  E no proximo numero checa se o numero é um valor que eu quero (ou seja, se existe no hashmap)
  Very clever!
  """