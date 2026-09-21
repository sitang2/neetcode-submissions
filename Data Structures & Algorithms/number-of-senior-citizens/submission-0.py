class Solution:
    def countSeniors(self, details: List[str]) -> int:
        ages = []

        for detail in details:
            ages.append(detail[11:13])

        count = 0
        for age in ages:
            if int(age) > 60:
                count += 1
        
        return count
